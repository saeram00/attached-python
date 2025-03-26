#!/usr/bin/env python3
import sys

import formatter as ft


def main() -> int:
    if len(sys.argv) > 2:
        sys.exit("Must invoke with 0 or 1 arguments [user_name].")
    user_name: str = sys.argv[1] if len(sys.argv) == 2 else input(
        "Enter the name of the user (enter 'q' to quit): "
    )
    while not user_name.isalpha():
        print("Must enter a name:")
        user_name = input("> ")
    if user_name == "q":
        sys.exit("Shutting down...")
    with open(f"{user_name}.csv", "w", encoding="utf-8", newline="") as new_f:
        t_formatter = ft.AnswerFormatter(new_f)
        t_formatter.write_answers(ft.answer_input())
    with open(f"{user_name}.csv", "r", encoding="utf-8", newline="") as p_file:
        t_calc = ft.ScoreCalculator(p_file)
        t_calc.compute_answers()
    sys.exit(0)


if __name__ == "__main__":
    main()
