from classes.card_app import CardApp

app = CardApp("staff-2024-final.csv", "output", generate_pdfs=True, use_print_layout=True)

app.run()
