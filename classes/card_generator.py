class CardGenerator:
  def __init__(self, output_dir, use_pring_layout):
    self.output_dir = output_dir
    self.use_pring_layout = use_pring_layout
    
  def generate_card(self, staff_member):
    print(f"TODO: Generate card for {staff_member} in {self.output_dir} with print layout {self.use_pring_layout}")
    
  def add_print_layout(self, image):
    print(f"TODO: Add print layout to {image}")
    
  def save_card(self, image, file_name):
    print(f"TODO: Save {image} to {file_name}")
    
  def save_pdf(self, images):
    print(f"TODO: Save {images} to PDF")