from PIL import Image, ImageDraw
import os
from utils import utils

class CardBackGenerator:
    def __init__(self, staff_member):
        self.staff_member = staff_member
        
    def get_card_back(self):
        # create canvas to build everything on
        canvas = Image.new(
            "RGB", (utils.CARD_WIDTH, utils.CARD_HEIGHT), color=utils.PALLETES[self.staff_member.department]["border_color"]
        )
        
        return canvas