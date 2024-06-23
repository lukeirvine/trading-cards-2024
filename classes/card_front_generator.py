from PIL import Image, ImageDraw
import os
import svgwrite
from io import BytesIO
import cairosvg
from utils import utils
import datetime

class CardFrontGenerator:
    def __init__(self, staff_member):
        self.staff_member = staff_member

    def get_card_face(self):
        # create canvas to build everything on
        canvas = Image.new(
            "RGB", (utils.CARD_WIDTH, utils.CARD_HEIGHT), color=(255, 255, 255)
        )

        # add main image to card
        image = Image.open(os.path.join("images", self.staff_member.image_path))
        image = self._resize_and_crop_image(
            image, utils.CARD_WIDTH, utils.CARD_HEIGHT + 20
        )
        canvas.paste(image, (0, 0))

        # add border to card
        border_color = utils.PALLETES[self.staff_member.department]["border_color"]
        border_image = self._process_svg("materials/border.svg", border_color)
        border_image = self._resize_border_image(
            border_image, utils.CARD_WIDTH + 2, utils.CARD_HEIGHT + 2
        )
        canvas.paste(border_image, (-1, -1), border_image)

        # add text containers to card
        c2_color = utils.PALLETES[self.staff_member.department]["secondary"]
        c2_image = self._process_svg("materials/job_container.svg", c2_color)
        c2_image = self._extend_text_container(c2_image, c2_image.width)
        # print(f"CONT 1 image height: {c1_image.height}")
        # print(f"CONT 2 image height: {c2_image.height}")
        print(f"CONT 2 image width: {c2_image.width}")
        canvas.paste(c2_image, (-1, utils.CONT_2_TOP), c2_image)

        # add stars
        canvas = self._add_stars(canvas)
        
        # add name and position text
        canvas = self._add_h1_text(canvas)
        canvas = self._add_h2_text(canvas)
        
        # add year to top of card
        canvas = self._add_year_text(canvas)
        
        # add logo to top left of card
        canvas = self._add_logo(canvas)

        return canvas

    def get_palletes(self):
        return utils.PALLETES

    def _resize_and_crop_image(self, image, new_width, new_height):
        # Get the current width and height
        current_width, current_height = image.size

        # Calculate the aspect ratios
        current_aspect_ratio = current_width / current_height
        new_aspect_ratio = new_width / new_height

        # Calculate the scale factor to resize the image
        if new_aspect_ratio > current_aspect_ratio:
            scale_factor = new_height / current_height
        else:
            scale_factor = new_width / current_width

        # Calculate the new size with the preserved aspect ratio
        resized_width = int(current_width * scale_factor)
        resized_height = int(current_height * scale_factor)

        # Resize the image while maintaining the aspect ratio
        resized_image = image.resize(
            (resized_width, resized_height), Image.Resampling.LANCZOS
        )

        # Calculate the coordinates for cropping
        left = (resized_width - new_width) / 2
        top = (resized_height - new_height) / 2
        right = (resized_width + new_width) / 2
        bottom = (resized_height + new_height) / 2

        # Crop the image to the desired dimensions
        cropped_image = resized_image.crop((left, top, right, bottom))

        return cropped_image

    def _process_svg(self, svg_path, color):
        # Convert SVG to PNG
        image = utils.convert_svg_to_png(svg_path)

        # Recolor the image
        image = self._recolor_image(image, color)

        return image

    def _recolor_image(self, image, new_color):
        # Ensure the image is in RGBA mode
        image = image.convert("RGBA")
        data = image.getdata()

        # Replace all non-transparent pixels with the new color
        new_data = []
        for item in data:
            # Change all white (also checking alpha) pixels to the new color
            if item[3] > 0:  # Check alpha
                new_data.append(new_color + (item[3],))
            else:
                new_data.append(item)

        image.putdata(new_data)
        return image

    def _resize_border_image(self, image, new_width, new_height):
        # Resize the border image to fit the new dimensions without maintaining aspect ratio
        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    def _extend_text_container(self, image, new_width):
        # Extend the text container image to the new width
        return image.resize((new_width, image.height), Image.Resampling.LANCZOS)

    def _add_stars(self, canvas):
        star = self._process_svg("materials/star.svg", (255, 255, 255))
        star = self._recolor_image(
            star, utils.PALLETES[self.staff_member.department]["star"]
        )
        star_width = star.width
        canvas.paste(star, (utils.STAR_START_POS_X, utils.STAR_START_POS_Y), star)
        for i in range(0, self.staff_member.years_worked):
            offset = utils.STAR_ROW_OFFSET if (i // 7) % 2 == 1 else 0
            x = (
                utils.STAR_START_POS_X
                + (star_width + utils.STAR_SPACING_X) * (i % 7)
                + offset
            )
            y = utils.STAR_START_POS_Y + (star_width + utils.STAR_SPACING_Y) * (i // 7)
            canvas.paste(star, (x, y), star)

        return canvas

    def _add_h1_text(self, canvas):
        INDENT = 30
        font_size = 70
        font_top_offset = round(font_size * 0.4)
        CONTAINER_CUSHION = 40
        font = utils.get_title_font(font_size)
        draw = ImageDraw.Draw(canvas)
        text = self.staff_member.name
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # adjust text width to fit the container
        while (text_width > utils.CONT_1_MAX_WIDTH - 2 * INDENT - CONTAINER_CUSHION):
            font_size -= 1
            font = utils.get_title_font(font_size)
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            font_top_offset = round(font_size * 0.4)
        
        c1_color = utils.PALLETES[self.staff_member.department]["primary"]
        c1_image = self._process_svg("materials/name_container.svg", c1_color)
        new_width = text_width + 2 * INDENT + CONTAINER_CUSHION
        if (new_width > utils.CONT_1_MAX_WIDTH):
            new_width = utils.CONT_1_MAX_WIDTH
        if (new_width < utils.CONT_1_MIN_WIDTH):
            new_width = utils.CONT_1_MIN_WIDTH
        c1_image = self._extend_text_container(c1_image, new_width)
        canvas.paste(c1_image, (-1, utils.CONT_1_TOP), c1_image)
        
        text_top = utils.CONT_1_TOP - font_top_offset + (c1_image.height - text_height) / 2
        draw.text(
            (INDENT, text_top),
            text,
            font=font,
            fill=(255, 255, 255),
        )
        
        return canvas

    def _add_h2_text(self, canvas):
        INDENT = 30
        font_size = 28
        font_top_offset = round(font_size * 0.4)
        CONTAINER_CUSHION = 40
        font = utils.get_title_font(font_size)
        draw = ImageDraw.Draw(canvas)
        text = self.staff_member.position
        max_width = utils.CONT_2_MAX_WIDTH - 2 * INDENT - CONTAINER_CUSHION

        def get_text_size(text, font):
            bbox = draw.textbbox((0, 0), text, font=font)
            return bbox[2] - bbox[0], bbox[3] - bbox[1]

        text_width, text_height = get_text_size(text, font)

        # Adjust text width to fit the container
        while text_width > max_width:
            # Check if we can split text into two lines
            words = text.split()
            wrapped_text = text
            for i in range(1, len(words)):
                line1 = ' '.join(words[:i])
                line2 = ' '.join(words[i:])
                width1, height1 = get_text_size(line1, font)
                width2, height2 = get_text_size(line2, font)
                if width1 <= max_width and width2 <= max_width:
                    wrapped_text = f"{line1}\n{line2}"
                    text_width = max(width1, width2)
                    text_height = height1 + height2
                    font_top_offset += 5
                    break

            # If still too wide, reduce the font size
            if text_width > max_width:
                font_size -= 1
                font = utils.get_title_font(font_size)
                text_width, text_height = get_text_size(wrapped_text, font)
                font_top_offset = round(font_size * 0.4)
            else:
                text = wrapped_text

        c2_color = utils.PALLETES[self.staff_member.department]["secondary"]
        c2_image = self._process_svg("materials/job_container.svg", c2_color)
        new_width = text_width + 2 * INDENT + CONTAINER_CUSHION
        if new_width > utils.CONT_2_MAX_WIDTH:
            new_width = utils.CONT_2_MAX_WIDTH
        c2_image = self._extend_text_container(c2_image, new_width)
        canvas.paste(c2_image, (-1, utils.CONT_2_TOP), c2_image)

        # Adjust text position to be centered
        text_top = utils.CONT_2_TOP - font_top_offset + (c2_image.height - text_height) / 2
        draw.text(
            (INDENT, text_top),
            text,
            font=font,
            fill=(255, 255, 255),
            spacing=5  # Add spacing between lines if wrapped
        )

        return canvas
    
    def _add_year_text(self, canvas):
        font = utils.get_title_font(28)
        draw = ImageDraw.Draw(canvas)
        text = str(datetime.datetime.now().year)
        char_spacing = 15  # Adjust this value to increase or decrease spacing between characters
        opacity = 150  # Adjust this value (0-255) to change the opacity

        # Create a transparent layer for the text
        text_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        text_draw = ImageDraw.Draw(text_layer)

        # Calculate the width of the entire text including character spacing
        text_width = sum(text_draw.textbbox((0, 0), char, font=font)[2] - text_draw.textbbox((0, 0), char, font=font)[0] + char_spacing for char in text) - char_spacing
        text_height = text_draw.textbbox((0, 0), text, font=font)[3] - text_draw.textbbox((0, 0), text, font=font)[1]

        # Start position for the text
        start_x = utils.CARD_WIDTH / 2 - text_width / 2
        start_y = 22

        # Draw each character with spacing on the transparent layer
        x = start_x
        for char in text:
            text_draw.text((x, start_y), char, font=font, fill=(255, 255, 255, opacity))
            char_width = text_draw.textbbox((0, 0), char, font=font)[2] - text_draw.textbbox((0, 0), char, font=font)[0]
            x += char_width + char_spacing

        # Composite the text layer onto the canvas
        canvas = Image.alpha_composite(canvas.convert("RGBA"), text_layer)

        return canvas
    
    def _add_logo(self, canvas):
        logo = Image.open("materials/logo.png")
        logo = logo.resize((142, 120))
        paste_alpha = logo.split()[-1]
        canvas.paste(logo, (15, 30), mask=paste_alpha)
        return canvas