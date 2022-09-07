from itertools import count
import formatter as ft


def answer_inp() -> list[int]:
    answers_lst: list[int] = list()
    answ = None
    q_num = count(start=1, step=1)
    print("Enter the patient's answers:")
    while len(answers_lst) < 40:
        try:
            answ = input(f"{next(q_num)}) ")
            answers_lst.append(int(answ))
        except ValueError:
            if answ == "q":
                exit("Shutting down...")
            elif not isinstance(answ, int):
                print("Must input a number.")
    else:
        return answers_lst


def main():
    p_name = input("Name of the patient: ")
    while len(p_name) < 1:
        print("Must enter a name:")
        p_name = input("> ")
    with open(f"{p_name}.csv", "w", encoding="utf-8", newline="") as new_f:
        t_formatter = ft.TestFormatter(new_f)
        t_formatter.load_json()
        t_formatter.write_csv(answer_inp())


if __name__ == "__main__":
    main()
