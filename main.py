from itertools import count
from typing import List

import csv


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
    with open(f"{f_name}.csv", "w", encoding="utf-8", newline="") as patient:
        csv_writer = csv.writer(patient, dialect="excel")
        for item in tuple(enumerate(answ_list, start=1)):
            csv_writer.writerow(item)


def main():
    p_name = input("Name of the patient: ")
    while len(p_name) < 1:
        print("Must enter a name:")
        p_name = input("> ")
    create_file(p_name, answer_inp())


if __name__ == '__main__':
    main()

