import csv
import json


DFLT_FIELDNAMES: tuple[str, ...] = ("question_number", "item_factor", "answer")


class AnswerFormatter(csv.DictWriter):
    """
    Custom class meant to join json reading and csv writing operations in a
    single object.
    """

    def __init__(self, file, fieldnames=DFLT_FIELDNAMES, dialect="excel"):
        super().__init__(file, fieldnames=fieldnames, dialect=dialect)
        with open("item_factors.json") as jsonfile:
            self.__i_factors = json.load(jsonfile)["factors"]

    def write_answers(self, answers: list[int]) -> None:
        fields: dict = dict().fromkeys(self.fieldnames)
        self.writeheader()

        for index, answer in enumerate(answers, start=1):
            for factor, question_numbers in self.__i_factors.items():
                if index in question_numbers:
                    fields.update(
                        {
                            "question_number": index,
                            "item_factor": factor,
                            "answer": answer,
                        }
                    )
                    self.writerow(fields)


def answer_input() -> list[int]:
    answers: list[int] = []
    q_num: int = 1
    print("Enter the user's answers (number between 1-6):")
    while len(answers) < 40:
        try:
            answer: int = int(input(f"{q_num}) "))
            if not 1 <= answer <= 6:
                raise ValueError
            answers.append(answer)
            q_num += 1
        except ValueError:
            print("Must input a number between 1-6:")
    return answers


def compute_results(file: str) -> dict:
    results: dict = {
        "low_selfesteem": 0,
        "conflict_resolution": 0,
        "expressiveness": 0,
        "self_sufficiency": 0,
    }
    with open(file, "r", encoding="utf-8", newline="") as user_file:
        scores = csv.DictReader(user_file, dialect="excel")
        for score in scores:
            results[score["item_factor"]] += int(score["answer"])
    return results
