import csv
import json


DFLT_FIELDNAMES: tuple[str, ...] = (
    "question_number",
    "item_factor",
    "answer"
)


class AnswerFormatter(csv.DictWriter):
    """
    Custom class meant to join json reading and csv writing operations in a
    single object.
    """

    def __init__(self, file, fieldnames=DFLT_FIELDNAMES, dialect="excel"):
        super().__init__(file, fieldnames=fieldnames, dialect=dialect)
        with open("item_factors.json") as jsonfile:
            self.__i_factors = json.load(jsonfile)["factors"]

    def write_answers(self, answ_list: list[int]) -> None:
        field_dict: dict = dict().fromkeys(self.fieldnames)
        self.writeheader()

        for index, answer in enumerate(answ_list, start=1):
            for factor, q_nums in self.__i_factors.items():
                if index in q_nums:
                    field_dict.update({
                        "question_number": index,
                        "item_factor": factor,
                        "answer": answer
                    })
                    self.writerow(field_dict)


class ScoreCalculator(csv.DictReader):
    """
    Custom class meant to compute the results from the test.
    """

    def __init__(self, file, fieldnames=DFLT_FIELDNAMES, dialect="excel"):
        super().__init__(file, fieldnames=fieldnames, dialect=dialect)
        with open("item_factors.json") as jsonfile:
            self.__i_factors = json.load(jsonfile)["factors"]

    def compute_answers(self) -> None:
        field_dict: dict = dict().fromkeys(self.fieldnames)


def answer_input() -> list[int]:
    answers_list: list[int] = []
    q_num: int = 1
    print("Enter the user's answers (number between 1-6):")
    while len(answers_list) < 40:
        try:
            answer: int = int(input(f"{q_num}) "))
            if not 1 <= answer <= 6:
                raise ValueError
            answers_list.append(answer)
            q_num += 1
        except ValueError:
            print("Must input a number between 1-6:")
    return answers_list
