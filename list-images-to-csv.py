import os
import csv

def list_files_in_directory(directory):
    # List all files in the given directory and sort them alphabetically
    files = sorted([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
    return files

def write_files_to_csv(files, output_csv):
    # Write the list of files to a CSV file
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Filename"])  # Write the header
        for filename in files:
            writer.writerow([filename])

def main():
    photos_directory = 'images'  # Change this if your directory is different
    output_csv = 'file_list.csv'  # Output CSV file

    # Get list of files in the directory
    files = list_files_in_directory(photos_directory)

    # Write the files to a CSV
    write_files_to_csv(files, output_csv)

    print(f"List of files has been written to {output_csv}")

if __name__ == "__main__":
    main()
