from PIL import Image
import os
import svgwrite
from io import BytesIO
import cairosvg
from utils import utils


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
            border_image, utils.CARD_WIDTH + 2, utils.CARD_HEIGHT
        )
        canvas.paste(border_image, (-1, 0), border_image)

        # add text containers to card
        c1_color = utils.PALLETES[self.staff_member.department]["primary"]
        c2_color = utils.PALLETES[self.staff_member.department]["secondary"]
        c1_image = self._process_svg("materials/name_container.svg", c1_color)
        c1_image = self._extend_text_container(c1_image, c1_image.width)
        c2_image = self._process_svg("materials/job_container.svg", c2_color)
        c2_image = self._extend_text_container(c2_image, c2_image.width)
        # print(f"CONT 1 image height: {c1_image.height}")
        # print(f"CONT 1 image width: {c1_image.width}")
        # print(f"CONT 2 image height: {c2_image.height}")
        print(f"CONT 2 image width: {c2_image.width}")
        canvas.paste(c1_image, (-1, utils.CONT_1_TOP), c1_image)
        canvas.paste(c2_image, (-1, utils.CONT_2_TOP), c2_image)

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

    # def _add_stars(self, image):
