from classes.card_template import CardTemplate
import os


class CardGenerator:
    def __init__(self, output_dir, use_pring_layout):
        self.output_dir = output_dir
        self.use_pring_layout = use_pring_layout

    def generate_card(self, staff_member):
        template = CardTemplate(
            staff_member.image_path, staff_member.department
        ).get_template()

        return template

    def add_print_layout(self, image):
        print(f"TODO: Add print layout to {image}")

    def save_card(self, image, sub_dir, file_name):
        # create output_dir/sub_dir if it doesn't exist
        if not os.path.exists(f"{self.output_dir}/{sub_dir}"):
            os.makedirs(f"{self.output_dir}/{sub_dir}")
        image.save(f"{self.output_dir}/{sub_dir}/{file_name}")

    def save_pdf(self, images):
        print(f"TODO: Save {images} to PDF")
