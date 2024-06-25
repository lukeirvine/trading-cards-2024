from io import BytesIO
from PIL import Image, ImageFont
import cairosvg


class Utils:
    def __init__(self):
        # Limits ========================
        self.MAX_YEARS = 14

        # Layouts ========================
        self.CARD_WIDTH = 750
        self.CARD_HEIGHT = 1050
        # height is 149
        self.CONT_1_TOP = 741
        self.CONT_1_MIN_WIDTH = 482
        self.CONT_1_MAX_WIDTH = 650
        # height is 124
        self.CONT_2_TOP = 888
        self.CONT_2_MAX_WIDTH = 340
        self.STAR_START_POS_X = 340
        self.STAR_START_POS_Y = 935
        self.STAR_SPACING_X = 10
        self.STAR_SPACING_Y = 10
        self.STAR_ROW_OFFSET = -25
        self.PRINT_WIDTH = 825
        self.PRINT_HEIGHT = 1125
        
        self.BACK_MARGIN = 50
        
        # Misc ========================
        self.LOGO_PATH = "materials/full-logo.png"

        # Styling ========================
        self.PALLETES = {
            "leadership": {
                "border_color": (182, 70, 95),
                "primary": (76, 96, 133),
                "secondary": (51, 30, 56),
                "star": (201, 221, 255),
            },
            "extreme": {
                "border_color": (45, 48, 71),
                "primary": (147, 183, 190),
                "secondary": (224, 202, 60),
                "star": (255, 255, 61),
            },
            "housekeeping": {
                "border_color": (94, 128, 127),
                "primary": (157, 197, 187),
                "secondary": (23, 184, 144),
                "star": (255, 255, 61),
            },
            "office": {
                "border_color": (78, 89, 140),
                "primary": (255, 113, 91),
                "secondary": (8, 178, 227),
                "star": (255, 255, 61),
            },
            "waterfront": {
                "border_color": (7, 16, 19),
                "primary": (2, 169, 234),
                "secondary": (255, 1, 251),
                "star": (255, 255, 255),
            },
            "activities": {
                "border_color": (26, 101, 158),
                "primary": (255, 107, 53),
                "secondary": (247, 197, 159),
                "star": (239, 239, 208),
            },
            "art": {
                "border_color": (85, 62, 78),
                "primary": (255, 175, 197),
                "secondary": (158, 188, 158),
                "star": (255, 207, 210),
            },
            "challenge": {
                "border_color": (240, 113, 103),
                "primary": (63, 130, 109),
                "secondary": (154, 196, 248),
                "star": (253, 252, 220),
            },
            "comms": {
                "border_color": (190, 110, 70),
                "primary": (163, 191, 168),
                "secondary": (78, 76, 103),
                "star": (205, 231, 176),
            },
            "dt": {
                "border_color": (23, 48, 28),
                "primary": (116, 79, 198),
                "secondary": (55, 147, 146),
                "star": (79, 176, 198),
            },
            "equestrian": {
                "border_color": (174, 132, 126),
                "primary": (98, 131, 149),
                "secondary": (38, 42, 16),
                "star": (223, 213, 165),
            },
            "kitchen": {
                "border_color": (159, 183, 152),
                "primary": (127, 124, 175),
                "secondary": (159, 180, 199),
                "star": (238, 238, 255),
            },
            "maintenance": {
                "border_color": (215, 144, 123),
                "primary": (236, 200, 174),
                "secondary": (179, 103, 155),
                "star": (221, 255, 217),
            },
            "survival": {
                "border_color": (64, 42, 44),
                "primary": (124, 127, 101),
                "secondary": (128, 164, 237),
                "star": (188, 211, 242),
            },
            "ultimate": {
                "border_color": (42, 71, 71),
                "primary": (97, 208, 149),
                "secondary": (83, 134, 228),
                "star": (224, 186, 215),
            },
            "programming": {
                "border_color": (0, 124, 119),
                "primary": (76, 26, 87),
                "secondary": (255, 60, 199),
                "star": (240, 246, 0),
            },
            "null": {
                "border_color": (4, 8, 15),
                "primary": (125, 132, 145),
                "secondary": (192, 197, 193),
                "star": (255, 255, 61),
            },
        }

    def convert_svg_to_png(self, svg_path):
        png_data = cairosvg.svg2png(url=svg_path)
        image = Image.open(BytesIO(png_data))

        return image
    
    def get_title_font(self, desired_height):
        font_path = "fonts/PoetsenOne-Regular.ttf"
        size = 36
        font = ImageFont.truetype(font_path, size)

        # Measure the text height
        dummy_text = "A"
        bbox = font.getbbox(dummy_text)
        text_height = bbox[3] - bbox[1]

        # Adjust the font size to match the desired height
        adjusted_size = int(size * desired_height / text_height)
        return ImageFont.truetype(font_path, adjusted_size)
    
    def get_question_font(self, desired_height):
        font_path = "fonts/PoetsenOne-Regular.ttf"
        size = 36
        font = ImageFont.truetype(font_path, size)

        # Measure the text height
        dummy_text = "A"
        bbox = font.getbbox(dummy_text)
        text_height = bbox[3] - bbox[1]

        # Adjust the font size to match the desired height
        adjusted_size = int(size * desired_height / text_height)
        return ImageFont.truetype(font_path, adjusted_size)


utils = Utils()
