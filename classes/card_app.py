class CardApp:
  def __init__(self, csv_file_path, output_dir):
    self.csv_file_path = csv_file_path
    self.output_dir = output_dir
  
  def run(self):
    print(f"Running with {self.csv_file_path} and {self.output_dir}")