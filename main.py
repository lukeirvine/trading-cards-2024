from classes.card_app import CardApp

app = CardApp("staff_input_one_each.csv", "output", generate_pdfs=False, use_print_layout=False)

app.run()
