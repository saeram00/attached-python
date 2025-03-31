import csv
import json

from pathlib import Path

FACTORS_FILE: Path = Path("item_factors.json")
FIELDNAMES: tuple[str, ...] = ("question_number", "item_factor", "answer")


class AnswerFormatter(csv.DictWriter):
    """
    Custom class meant to join json reading and csv writing operations in a
    single object.

    Attributes:
    scores_file: FileObject: a file to write the scores to in csv format.
    fieldnames: Iterable[str]: an iteralble of strings containing the names of
    the fields for each csv column.
    dialect: str: the csv dialect to write in. Defaults to excel.
    __i_factors: dict[str, list]: the attachment factors extracted from a json
    file to determine the item factor of each test question.
    """

    def __init__(self, scores_file, fieldnames=FIELDNAMES, dialect="excel"):
        super().__init__(scores_file, fieldnames=fieldnames, dialect=dialect)
        with open(FACTORS_FILE) as factors:
            self.__i_factors = json.load(factors)["factors"]

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


class ScoreCalculator(object):
    """
    A class meant to calculate the sum of the scores obtained in the test and
    detect the attachment style given the results.

    Attributes:
    scores_file: FileObject: a file where the test scores are stored in csv
    format.
    dialect: str: the csv dialect to pass to the reader. Defaults to excel.
    __i_factors: dict[str, list]: the attachment factors extracted from a json
    file to determine the item factor of each test question.
    """

    def __init__(self, scores_file, dialect="excel"):
        self.__score_reader = csv.DictReader(scores_file, dialect=dialect)
        with open(FACTORS_FILE) as factors:
            self.__i_factors = json.load(factors)["factors"]

    def compute_results(self) -> dict:
        results: dict = dict.fromkeys(self.__i_factors.keys(), 0)
        for score in self.__score_reader:
            results[score[FIELDNAMES[1]]] += int(score[FIELDNAMES[2]])
        return results


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
