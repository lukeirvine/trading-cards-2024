from io import BytesIO
from PIL import Image
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
        self.CONT_1_MAX_WIDTH = 650
        # height is 124
        self.CONT_2_TOP = 888
        self.CONT_2_MAX_WIDTH = 340
        self.STAR_START_POS_X = 340
        self.STAR_START_POS_Y = 935
        self.STAR_SPACING_X = 10
        self.STAR_SPACING_Y = 10
        self.STAR_ROW_OFFSET = -25

        # Styling ========================
        self.PALLETES = {
            "leadership": {
                "border_color": (60, 89, 115),
                "primary": (60, 89, 115),
                "secondary": (60, 89, 115),
                "star": (255, 255, 61),
            },
            "extreme": {
                "border_color": (56, 65, 42),
                "primary": (56, 65, 42),
                "secondary": (56, 65, 42),
                "star": (255, 255, 61),
            },
            "housekeeping": {
                "border_color": (59, 41, 58),
                "primary": (59, 41, 58),
                "secondary": (59, 41, 58),
                "star": (255, 255, 61),
            },
            "office": {
                "border_color": (49, 47, 89),
                "primary": (49, 47, 89),
                "secondary": (49, 47, 89),
                "star": (255, 255, 61),
            },
            "waterfront": {
                "border_color": (117, 0, 255),
                "primary": (105, 186, 201),
                "secondary": (201, 114, 105),
                "star": (255, 255, 61),
            },
            "activities": {
                "border_color": (177, 74, 53),
                "primary": (177, 74, 53),
                "secondary": (177, 74, 53),
                "star": (255, 255, 61),
            },
            "art": {
                "border_color": (146, 67, 83),
                "primary": (146, 67, 83),
                "secondary": (146, 67, 83),
                "star": (255, 255, 61),
            },
            "challenge": {
                "border_color": (89, 155, 152),
                "primary": (89, 155, 152),
                "secondary": (89, 155, 152),
                "star": (255, 255, 61),
            },
            "comms": {
                "border_color": (186, 118, 48),
                "primary": (186, 118, 48),
                "secondary": (186, 118, 48),
                "star": (255, 255, 61),
            },
            "dt": {
                "border_color": (126, 46, 46),
                "primary": (126, 46, 46),
                "secondary": (126, 46, 46),
                "star": (255, 255, 61),
            },
            "equestrian": {
                "border_color": (25, 89, 65),
                "primary": (25, 89, 65),
                "secondary": (25, 89, 65),
                "star": (255, 255, 61),
            },
            "kitchen": {
                "border_color": (76, 20, 17),
                "primary": (76, 20, 17),
                "secondary": (76, 20, 17),
                "star": (255, 255, 61),
            },
            "maintenance": {
                "border_color": (78, 78, 80),
                "primary": (78, 78, 80),
                "secondary": (78, 78, 80),
                "star": (255, 255, 61),
            },
            "survival": {
                "border_color": (140, 88, 58),
                "primary": (140, 88, 58),
                "secondary": (140, 88, 58),
                "star": (255, 255, 61),
            },
            "ultimate": {
                "border_color": (217, 109, 85),
                "primary": (217, 109, 85),
                "secondary": (217, 109, 85),
                "star": (255, 255, 61),
            },
            "programming": {
                "border_color": (0, 0, 0),
                "primary": (0, 0, 0),
                "secondary": (0, 0, 0),
                "star": (255, 255, 61),
            },
            "null": {
                "border_color": (50, 50, 50),
                "primary": (50, 50, 50),
                "secondary": (50, 50, 50),
                "star": (255, 255, 61),
            },
        }

    def convert_svg_to_png(self, svg_path):
        png_data = cairosvg.svg2png(url=svg_path)
        image = Image.open(BytesIO(png_data))

        return image


utils = Utils()
