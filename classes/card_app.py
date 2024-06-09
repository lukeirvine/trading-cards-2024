from classes.csv_reader import CSVReader
from classes.card_generator import CardGenerator


class CardApp:
    def __init__(self, csv_file_path, output_dir):
        self.csv_file_path = csv_file_path
        self.output_dir = output_dir

    def run(self):
        reader = CSVReader(self.csv_file_path)
        staff_members = reader.read_csv()

        # for staff_member in staff_members:
        #     staff_member.print_data()

        # use_print_layout = input("Would you like to use the print layout? (y/n): ").strip().lower() == 'y'

        print("=========================================")
        print("Generating cards...")
        print("=========================================")

        generator = CardGenerator(self.output_dir, False)
        generated_images = []

        for staff_member in staff_members:
            card_image = generator.generate_card(staff_member)
            file_name = f"{staff_member.name}.png"
            generator.save_card(card_image, staff_member.department, file_name)
            generated_images.append(file_name)
            print(f"Generated card for {staff_member.name}")

        generator.save_pdf(generated_images)
