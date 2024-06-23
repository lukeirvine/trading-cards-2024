from classes.card_front_generator import CardFrontGenerator
from classes.card_back_generator import CardBackGenerator
import os
from utils import utils
from PIL import Image, ImageFont, ImageDraw
import datetime


class CardGenerator:
    def __init__(self, output_dir, use_print_layout):
        self.output_dir = output_dir
        self.use_print_layout = use_print_layout

    def generate_card(self, staff_member):
        front_image = CardFrontGenerator(staff_member).get_card_face()
        
        back_image = CardBackGenerator(staff_member).get_card_back()

        return (front_image, back_image)

    def add_print_layout(self, image, staff_member, side="back"):
        canvas = Image.new('RGB', (utils.PRINT_WIDTH, utils.PRINT_HEIGHT), color=utils.PALLETES[staff_member.department]["border_color"])
        
        # add the print border
        border = Image.open("materials/print-border-5.png")
        border = border.resize((utils.PRINT_WIDTH, utils.PRINT_HEIGHT))
        paste_alpha = border.split()[-1]
        canvas.paste(border, (0, 0), mask=paste_alpha)
        
        # paste the image onto the canvas
        canvas.paste(image, ((utils.PRINT_WIDTH - utils.CARD_WIDTH) // 2, (utils.PRINT_HEIGHT - utils.CARD_HEIGHT) // 2))
        
        # design specific
        # add rectangles to left edge of canvas for text container bleed
        if side is "front":
            # get height of name_container.svg
            c1_image = CardFrontGenerator(staff_member).get_c1_image()
            draw = ImageDraw.Draw(canvas)
            top = utils.CONT_1_TOP + (utils.PRINT_HEIGHT - utils.CARD_HEIGHT) // 2 + 1
            draw.rectangle([0, top, 40, top + c1_image.height - 3], fill=utils.PALLETES[staff_member.department]["primary"])
            
            c2_image = CardFrontGenerator(staff_member).get_c2_image()
            top = utils.CONT_2_TOP + (utils.PRINT_HEIGHT - utils.CARD_HEIGHT) // 2 + 1
            draw.rectangle([0, top, 40, top + c2_image.height - 6], fill=utils.PALLETES[staff_member.department]["secondary"])
        
        return canvas

    def save_card(self, image, sub_dir, file_name):
        # create output_dir/sub_dir if it doesn't exist
        if not os.path.exists(f"{self.output_dir}/{sub_dir}"):
            os.makedirs(f"{self.output_dir}/{sub_dir}")
        image.save(f"{self.output_dir}/{sub_dir}/{file_name}")

    def save_pdf(self, images):
        print(f"TODO: Save {images} to PDF")
