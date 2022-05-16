from itertools import count
from typing import List, Tuple

import csv
import json


def answer_inp() -> List[int]:
    answers_lst: List[int] = list()
    answ = None
    q_num = count(start=1, step=1)
    print("Enter the patient's answers:")
    while len(answers_lst) < 15: # Set to 40 when merging into main
        try:
            answ = input(f"{next(q_num)}) ")
            answers_lst.append(int(answ))
        except ValueError:
            if answ == "q":
                exit("Shutting down...")
            elif not isinstance(answ, int) and answ not in range(1, 7):
                print("Must input a number.")
    else:
        return answers_lst


def create_file(f_name: str, answ_list: List[int]):
    with open("item_factors.json") as jsonfile:
        i_factors = json.load(jsonfile)["factors"]

    with open(f"{f_name}.csv", "w", encoding="utf-8", newline="") as patient:
        fieldnames: Tuple[str, ...] = ("item_factor", "question_number", "answer")
        field_dict = dict().fromkeys(fieldnames)
        csv_writer = csv.DictWriter(patient, fieldnames=fieldnames, dialect="excel")
        csv_writer.writeheader()
        for index in range(len(answ_list)):
            for factor, q_nums in i_factors.items():
                if index+1 in q_nums:
                    field_dict["item_factor"] = factor
                    field_dict["question_number"] = index+1
                    field_dict["answer"] = answ_list[index]
                    csv_writer.writerow(field_dict)


def main():
    p_name = input("Name of the patient: ")
    while len(p_name) < 1:
        print("Must enter a name:")
        p_name = input("> ")
    create_file(p_name, answer_inp())


if __name__ == "__main__":
    main()

