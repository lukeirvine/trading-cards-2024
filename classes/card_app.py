from classes.csv_reader import CSVReader
from classes.card_generator import CardGenerator


class CardApp:
    def __init__(self, csv_file_path, output_dir, generate_pdfs=False, use_print_layout=False):
        self.csv_file_path = csv_file_path
        self.output_dir = output_dir
        self.generate_pdfs = generate_pdfs
        self.use_print_layout = use_print_layout

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
            front_image, back_image = generator.generate_card(staff_member)
            
            if self.use_print_layout:
                front_image = generator.add_print_layout(front_image, staff_member, "front")
                back_image = generator.add_print_layout(back_image, staff_member, "back")
            
            front_file_name = f"{staff_member.name} - front.png"
            back_file_name = f"{staff_member.name} - back.png"
            generator.save_card(front_image, staff_member.department, front_file_name)
            generator.save_card(back_image, staff_member.department, back_file_name)
            
            generated_images.append({
                "front-file-name": front_file_name,
                "back-file-name": back_file_name,
                "department": staff_member.department,
                "years": staff_member.years_worked
            })
            print(f"Generated card for {staff_member.name}")

        if self.generate_pdfs:
            generator.save_pdfs(generated_images)
            
        print("=========================================")
