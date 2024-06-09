from constants.template import CARD_HEIGHT, CARD_WIDTH
from PIL import Image, ImageDraw, ImageFont
import os
import svgwrite
from io import BytesIO
import cairosvg

class CardTemplate:
    def __init__(self, image_path="", department="null"):
        self.image_path = image_path
        self.department = department
        self.palletes = {
            "leadership": {
                "border_color": (60, 89, 115),
                "primary": (60, 89, 115),
                "secondary": (60, 89, 115),
            },
            "extreme": {
                "border_color": (56, 65, 42),
                "primary": (56, 65, 42),
                "secondary": (56, 65, 42),
            },
            "housekeeping": {
                "border_color": (59, 41, 58),
                "primary": (59, 41, 58),
                "secondary": (59, 41, 58),
            },
            "office": {
                "border_color": (49, 47, 89),
                "primary": (49, 47, 89),
                "secondary": (49, 47, 89),
            },
            "waterfront": {
                "border_color": (111, 166, 119),
                "primary": (111, 166, 119),
                "secondary": (111, 166, 119),
            },
            "activities": {
                "border_color": (177, 74, 53),
                "primary": (177, 74, 53),
                "secondary": (177, 74, 53),
            },
            "art": {
                "border_color": (146, 67, 83),
                "primary": (146, 67, 83),
                "secondary": (146, 67, 83),
            },
            "challenge": {
                "border_color": (89, 155, 152),
                "primary": (89, 155, 152),
                "secondary": (89, 155, 152),
            },
            "comms": {
                "border_color": (186, 118, 48),
                "primary": (186, 118, 48),
                "secondary": (186, 118, 48),
            },
            "dt": {
                "border_color": (126, 46, 46),
                "primary": (126, 46, 46),
                "secondary": (126, 46, 46),
            },
            "equestrian": {
                "border_color": (25, 89, 65),
                "primary": (25, 89, 65),
                "secondary": (25, 89, 65),
            },
            "kitchen": {
                "border_color": (76, 20, 17),
                "primary": (76, 20, 17),
                "secondary": (76, 20, 17),
            },
            "maintenance": {
                "border_color": (78, 78, 80),
                "primary": (78, 78, 80),
                "secondary": (78, 78, 80),
            },
            "survival": {
                "border_color": (140, 88, 58),
                "primary": (140, 88, 58),
                "secondary": (140, 88, 58),
            },
            "ultimate": {
                "border_color": (217, 109, 85),
                "primary": (217, 109, 85),
                "secondary": (217, 109, 85),
            },
            "programming": {
                "border_color": (0, 0, 0),
                "primary": (0, 0, 0),
                "secondary": (0, 0, 0),
            },
            "null": {
                "border_color": (50, 50, 50),
                "primary": (50, 50, 50),
                "secondary": (50, 50, 50),
            },
        }

    def get_template(self):
        # create canvas to build everything on
        canvas = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), color=(255, 255, 255))
        
        # add main image to card
        image = Image.open(os.path.join("images", self.image_path))
        image = self._resize_and_crop_image(image, CARD_WIDTH, CARD_HEIGHT + 20)
        canvas.paste(image, (0, 0))
        
        # add border to card
        border_color = self.palletes[self.department]["border_color"]
        border_image = self._process_svg_border("materials/border.svg", border_color)
        border_image = self._resize_border_image(border_image, CARD_WIDTH + 2, CARD_HEIGHT)
        
        #combine the image with the border
        canvas.paste(border_image, (-1, 0), border_image)

        return canvas

    def get_palletes(self):
        return self.palletes

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

    def _process_svg_border(self, svg_path, border_color):
        # Convert SVG to PNG
        png_data = cairosvg.svg2png(url=svg_path)
        border_image = Image.open(BytesIO(png_data))

        # Recolor the border image
        border_image = self._recolor_image(border_image, border_color)

        return border_image

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