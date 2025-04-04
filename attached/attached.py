import csv

FIELDNAMES: tuple[str, ...] = "question_number", "item_factor", "answer"
ITEM_FACTORS: dict[str, frozenset] = {
    "low_selfesteem": frozenset((14, 26, 18, 30, 21, 23, 8, 10, 12, 34, 39, 37, 3)),
    "conflict_resolution": frozenset((4, 2, 36, 7, 29, 20, 24, 31, 9, 17, 13)),
    "expressiveness": frozenset((1, 38, 32, 40, 16, 27, 5, 11, 35)),
    "self_sufficiency": frozenset((28, 22, 6, 25, 19, 15, 33)),
}


class AnswerFormatter(csv.DictWriter):
    """
    Custom class meant to join json reading and csv writing operations in a
    single object.

    Attributes:
    scores_file: TextIOWrapper: a file to write the scores to in csv format.
    fieldnames: Iterable[str]: an iteralble of strings containing the names of
    the fields for each csv column.
    dialect: str: the csv dialect to write in. Defaults to excel.
    """

    def __init__(self, scores_file, fieldnames=FIELDNAMES, dialect="excel"):
        super().__init__(scores_file, fieldnames=fieldnames, dialect=dialect)

    def write_answers(self, answers: list[int]) -> None:
        fields: dict = dict.fromkeys(self.fieldnames)
        self.writeheader()

        for index, answer in enumerate(answers, start=1):
            for factor, question_numbers in ITEM_FACTORS.items():
                if index in question_numbers:
                    fields.update(
                        {
                            FIELDNAMES[0]: index,
                            FIELDNAMES[1]: factor,
                            FIELDNAMES[2]: answer,
                        }
                    )
                    self.writerow(fields)
                    break


class ScoreCalculator:
    """
    A class meant to calculate the sum of the scores obtained in the test and
    detect the attachment style given the results.

    Attributes:
    scores_file: TextIOWrapper: a file where the test scores are stored in csv
    format.
    dialect: str: the csv dialect to pass to the reader. Defaults to excel.
    """

    def __init__(self, scores_file, dialect="excel"):
        self.__score_reader = csv.DictReader(scores_file, dialect=dialect)

    def compute_results(self) -> dict:
        results: dict = dict.fromkeys(ITEM_FACTORS, 0)
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
