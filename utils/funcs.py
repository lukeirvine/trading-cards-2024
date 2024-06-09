from io import BytesIO
from PIL import Image
import cairosvg


def convert_svg_to_png(svg_path):
    png_data = cairosvg.svg2png(url=svg_path)
    image = Image.open(BytesIO(png_data))

    return image
