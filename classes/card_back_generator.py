from PIL import Image, ImageDraw, ImageFont
from utils import utils

class CardBackGenerator:
    def __init__(self, staff_member):
        self.staff_member = staff_member
        self.canvas = Image.new(
            "RGB", (utils.CARD_WIDTH, utils.CARD_HEIGHT), color=utils.PALLETES[self.staff_member.department]["border_color"]
        )
        
    def get_card_back(self):
        # create canvas to build everything on
        canvas = Image.new(
            "RGB", (utils.CARD_WIDTH, utils.CARD_HEIGHT), color=utils.PALLETES[self.staff_member.department]["border_color"]
        )
        
        # add the logo
        LOGO_WIDTH = 450
        logo = Image.open(utils.LOGO_PATH)
        logo = logo.resize((LOGO_WIDTH, 112))
        paste_alpha = logo.split()[-1]
        canvas.paste(logo, (round(utils.CARD_WIDTH / 2) - round(LOGO_WIDTH / 2), 40), mask=paste_alpha)
        
        # add questions and answers
        canvas = self._add_questions(canvas)
        
        return canvas
    
    def _add_questions(self, canvas):
        LINE_SPACING = 50
        PAR_SPACING = 20
        INDENT = 20
        pos_y = 200
        canvas = self._add_question_text(canvas, self.staff_member.questions[0]["question"], pos_y)
        pos_y += LINE_SPACING
        canvas = self._add_response_text(canvas, self.staff_member.questions[0]["answer"], pos_y, INDENT)
        
        return canvas
    
    def _add_question_text(self, canvas, text, pos_y, indent=0):
        font = utils.get_question_font(26)
        draw = ImageDraw.Draw(canvas)
        bbox = draw.textbbox((0, 0), text, font=font)
        
        draw.text(
            (utils.BACK_MARGIN + indent, pos_y),
            text,
            font=font,
            fill=(255, 255, 255)
        )
        
        return canvas
    
    def _add_response_text(self, canvas, text, pos_y, indent=0):
        font = utils.get_question_font(20)
        draw = ImageDraw.Draw(canvas)
        bbox = draw.textbbox((0, 0), text, font=font)
        
        draw.text(
            (utils.BACK_MARGIN + indent, pos_y),
            text,
            font=font,
            fill=(255, 255, 255)
        )
        
        return canvas
    