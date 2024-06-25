import csv
from classes.staff_member import StaffMember
from classes.card_front_generator import CardFrontGenerator
import os
from utils import utils


class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        staff_members = []

        with open(self.file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                staff_member = StaffMember(
                    image_path=row["image_path"],
                    name=row["name"],
                    position=row["position"],
                    years_worked=row["years_worked"],
                    department=row["department"],
                    bible_verse=row["answer"],
                    question_1=row["question_1"],
                    answer_1=row["answer_1"],
                    question_2=row["question_2"],
                    answer_2=row["answer_2"],
                    question_3=row["question_3"],
                    answer_3=row["answer_3"],
                )
                staff_members.append(staff_member)

        self._check_data(staff_members)
        return staff_members

    def _check_data(self, staff_members):
        i = 0
        errors = []
        for sm in staff_members:
            # check that the image exists
            if not os.path.exists("images/" + sm.image_path):
                errors.append(
                    f'IMAGE ERROR {i + 2}: The image "{sm.image_path}" for {sm.name} doesn\'t exist. Check line {i + 2} in the csv file.'
                )

            # check that name is valid
            if "/" in sm.name:
                errors.append(f"The name column on row {i + 2} should not contain '/'")

            # check that department is valid
            palletes = utils.PALLETES
            if sm.department not in palletes.keys():
                error = f'The department "{sm.department}" is not valid. Valid departments are:\n'
                for dep in palletes.keys():
                    error += dep + ", "
                error += "\n"
                error += f"This error occurred in line {i + 2} of the csv file."
                errors.append(error)

            i += 1

        if len(errors) > 0:
            error_str = "\n".join(errors)
            raise RuntimeError(
                f"There were {len(errors)} errors with your data:\n" + error_str
            )
