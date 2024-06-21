from PIL import Image, ImageDraw, ImageFont
from utils import utils
import textwrap

class CardBackGenerator:
    def __init__(self, staff_member):
        self.staff_member = staff_member
        self.canvas = Image.new(
            "RGB", (utils.CARD_WIDTH, utils.CARD_HEIGHT), color=(0, 0, 0)
        )
        self.pos_y = 200
        self.question_size = 26
        self.answer_size = 20
        
        self.LINE_SPACING = 8
        self.PAR_SPACING = 8
        self.GROUP_SPACING = 10
        self.INDENT = 20
        
    def get_card_back(self):
        while (True):
            if self.answer_size < 12:
                # throw error
                raise Exception(f"Text too long for card: {self.staff_member.name}")
            
            # add a rectangle that fills the whole card
            draw = ImageDraw.Draw(self.canvas)
            draw.rectangle([0, 0, utils.CARD_WIDTH, utils.CARD_HEIGHT], fill=utils.PALLETES[self.staff_member.department]["border_color"])
            
            # add the logo
            LOGO_WIDTH = 450
            logo = Image.open(utils.LOGO_PATH)
            logo = logo.resize((LOGO_WIDTH, 112))
            paste_alpha = logo.split()[-1]
            self.canvas.paste(logo, (round(utils.CARD_WIDTH / 2) - round(LOGO_WIDTH / 2), 40), mask=paste_alpha)
            
            # add questions and answers
            self._add_questions()
            
            if self.pos_y < utils.CARD_HEIGHT - 50:
                break
            
            self.question_size -= 2
            self.answer_size -= 2
            self.pos_y = 200
        
        return self.canvas
    
    def _add_questions(self):
        for i in range (0, 4):
            self._add_text(self.staff_member.questions[i]["question"], self.question_size)
            self.pos_y += self.LINE_SPACING + self.PAR_SPACING
            self._add_text(self.staff_member.questions[i]["answer"], self.answer_size, self.INDENT)
            self.pos_y += self.LINE_SPACING + self.PAR_SPACING + self.GROUP_SPACING
    
    def _add_text(self, text, font_size, indent=0):
        font = utils.get_question_font(font_size)
        draw = ImageDraw.Draw(self.canvas)
        max_width = utils.CARD_WIDTH - utils.BACK_MARGIN * 2

        def get_text_size(text, font):
            bbox = draw.textbbox((0, 0), text, font=font)
            return bbox[2] - bbox[0], bbox[3] - bbox[1]

        # Function to calculate an approximate number of characters per line
        def calculate_wrap_width(text, font, max_width):
            avg_char_width = get_text_size("W" * 10, font)[0] / 10  # Approximate average character width
            return max_width // avg_char_width - 1

        # Calculate wrap width
        wrap_width = calculate_wrap_width(text, font, max_width)

        # Wrap the text using textwrap
        wrapped_lines = textwrap.wrap(text, width=wrap_width * 2)

        # Calculate height of the text block
        text_height = sum(get_text_size(line, font)[1] for line in wrapped_lines)

        # Draw each line with the calculated position
        for line in wrapped_lines:
            draw.text(
                (utils.BACK_MARGIN + indent, self.pos_y),
                line,
                font=font,
                fill=(255, 255, 255)
            )
            self.pos_y += get_text_size(line, font)[1] + self.LINE_SPACING

        return self.canvas
    