from io import BytesIO
from PIL import Image
import cairosvg


class Utils:
    def __init__(self):
        # Limits
        self.MAX_YEARS = 14

        # Layouts
        self.CARD_WIDTH = 750
        self.CARD_HEIGHT = 1050
        # height is 149
        self.CONT_1_TOP = 741
        self.CONT_1_MAX_WIDTH = 650
        # height is 124
        self.CONT_2_TOP = 888
        self.CONT_2_MAX_WIDTH = 340

    def convert_svg_to_png(self, svg_path):
        png_data = cairosvg.svg2png(url=svg_path)
        image = Image.open(BytesIO(png_data))

        return image


utils = Utils()
