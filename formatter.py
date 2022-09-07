import csv
import json


class TestFormatter(csv.DictWriter):
    """
    Custom class meant to join json reading and csv writing operations in a
    single object.
    """

    default_fieldnames: tuple[str, ...] = (
        "question_number",
        "item_factor",
        "answer"
    )

    def __init__(self, file, fieldnames=default_fieldnames, dialect="excel"):
        super().__init__(file, fieldnames, dialect)

    def load_json(self):
        with open("item_factors.json") as jsonfile:
            self.__i_factors = json.load(jsonfile)["factors"]

    def write_csv(self, answ_list: list[int]) -> None:
        field_dict: dict = dict().fromkeys(self.fieldnames)
        super().writeheader()

        for index in range(len(answ_list)):
            for factor, q_nums in self.__i_factors.items():
                if index+1 in q_nums:
                    field_dict.update({
                        "question_number": index+1,
                        "item_factor": factor,
                        "answer": answ_list[index]
                    })
                    super().writerow(field_dict)
