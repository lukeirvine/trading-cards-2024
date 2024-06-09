from constants.template import CARD_HEIGHT, CARD_WIDTH
from PIL import Image, ImageDraw, ImageFont
import os

class CardTemplate:
    def __init__(self, image_path='', department='null'):
        self.image_path = image_path
        self.department = department
        self.palletes = {
            'leadership': {
                'border_color': (60, 89, 115),
                'primary': (60, 89, 115),
                'secondary': (60, 89, 115),
            },
            'extreme': {
                'border_color': (56, 65, 42),
                'primary': (56, 65, 42),
                'secondary': (56, 65, 42),
            },
            'housekeeping': {
                'border_color': (59, 41, 58),
                'primary': (59, 41, 58),
                'secondary': (59, 41, 58),
            },
            'office': {
                'border_color': (49, 47, 89),
                'primary': (49, 47, 89),
                'secondary': (49, 47, 89),
            },
            'waterfront': {
                'border_color': (111, 166, 119),
                'primary': (111, 166, 119),
                'secondary': (111, 166, 119),
            },
            'activities': {
                'border_color': (177, 74, 53),
                'primary': (177, 74, 53),
                'secondary': (177, 74, 53),
            },
            'art': {
                'border_color': (146, 67, 83),
                'primary': (146, 67, 83),
                'secondary': (146, 67, 83),
            },
            'challenge': {
                'border_color': (89, 155, 152),
                'primary': (89, 155, 152),
                'secondary': (89, 155, 152),
            },
            'comms': {
                'border_color': (186, 118, 48),
                'primary': (186, 118, 48),
                'secondary': (186, 118, 48),
            },
            'dt': {
                'border_color': (126, 46, 46),
                'primary': (126, 46, 46),
                'secondary': (126, 46, 46),
            },
            'equestrian': {
                'border_color': (25, 89, 65),
                'primary': (25, 89, 65),
                'secondary': (25, 89, 65),
            },
            'kitchen': {
                'border_color': (76, 20, 17),
                'primary': (76, 20, 17),
                'secondary': (76, 20, 17),
            },
            'maintenance': {
                'border_color': (78, 78, 80),
                'primary': (78, 78, 80),
                'secondary': (78, 78, 80),
            },
            'survival': {
                'border_color': (140, 88, 58),
                'primary': (140, 88, 58),
                'secondary': (140, 88, 58),
            },
            'ultimate': {
                'border_color': (217, 109, 85),
                'primary': (217, 109, 85),
                'secondary': (217, 109, 85),
            },
            'programming': {
                'border_color': (0, 0, 0),
                'primary': (0, 0, 0),
                'secondary': (0, 0, 0),
            },
            'null': {
                'border_color': (50, 50, 50),
                'primary': (50, 50, 50),
                'secondary': (50, 50, 50),
            },
        }

    def get_template(self):
        canvas = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), color=(255, 255, 255))
        image = Image.open(os.path.join("images", self.image_path))
        image = self._resize_and_crop_image(image, CARD_WIDTH, CARD_HEIGHT + 20)
        canvas.paste(image, (0, 0))
        
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
        resized_image = image.resize((resized_width, resized_height), Image.Resampling.LANCZOS)

        # Calculate the coordinates for cropping
        left = (resized_width - new_width) / 2
        top = (resized_height - new_height) / 2
        right = (resized_width + new_width) / 2
        bottom = (resized_height + new_height) / 2

        # Crop the image to the desired dimensions
        cropped_image = resized_image.crop((left, top, right, bottom))
        
        return cropped_image
