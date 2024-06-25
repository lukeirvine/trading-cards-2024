import csv
import re

def add_spaces_around_slashes(text):
    # Add spaces around '/' if they don't already have spaces
    return re.sub(r'(?<! )/(?! )', ' / ', text)

def process_csv(input_csv, output_csv):
    with open(input_csv, mode='r', newline='') as infile, open(output_csv, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in reader:
            if 'position' in row:
                row['position'] = add_spaces_around_slashes(row['position'])
            writer.writerow(row)

def main():
    input_csv = 'staff-2024-final.csv'  # Replace with your input CSV file path
    output_csv = 'output.csv'  # Replace with your desired output CSV file path
    
    process_csv(input_csv, output_csv)
    print(f"Processed data has been written to {output_csv}")

if __name__ == "__main__":
    main()
