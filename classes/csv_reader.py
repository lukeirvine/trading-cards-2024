import csv
from classes.staff_member import StaffMember


class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        staff_members = []

        with open(self.file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                staff_member = StaffMember(
                    name=row["name"],
                    category=row["category"],
                    years_worked=int(row["years_worked"]),
                )
                staff_members.append(staff_member)

        return staff_members
