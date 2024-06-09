import json


class StaffMember:
    def __init__(
        self,
        image_path,
        name,
        position,
        years_worked,
        department,
        bible_verse,
        question_1,
        answer_1,
        question_2,
        answer_2,
        question_3,
        answer_3,
    ):
        self.image_path = image_path
        self.name = name
        self.position = position
        self.years_worked = int(years_worked)
        self.department = department
        self.questions = [
            {"question": "Favorite Bible Verse", "answer": bible_verse},
            {"question": question_1, "answer": answer_1},
            {"question": question_2, "answer": answer_2},
            {"question": question_3, "answer": answer_3},
        ]

    def print_data(self):
        data = {
            "image_path": self.image_path,
            "name": self.name,
            "position": self.position,
            "years_worked": self.years_worked,
            "department": self.department,
            "questions": self.questions,
        }
        print(json.dumps(data, indent=4))
