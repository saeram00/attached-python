#!/usr/bin/env python3
import sys

from pathlib import Path

import attached.attached as at

SCRIPT_ROOT = Path(__file__).parent


def main() -> int:
    if len(sys.argv) > 2:
        sys.exit("Must invoke with 0 or 1 arguments [user_name].")
    user_name: str = (
        sys.argv[1]
        if len(sys.argv) == 2
        else input("Enter the name of the user (enter 'q' to quit): ")
    )
    while not user_name.isalpha():
        print("Must enter a name:")
        user_name = input("> ")
    if user_name == "q":
        print("Shutting down...")
        sys.exit(2)
    SCRIPT_ROOT.joinpath("user_scores").mkdir(exist_ok=True)
    SCORES_DIR = SCRIPT_ROOT.joinpath("user_scores")
    user_answers = SCORES_DIR.joinpath(f"{user_name}.csv")
    with open(user_answers, "w", encoding="utf-8", newline="") as answers:
        a_formatter = at.AnswerFormatter(answers)
        a_formatter.write_answers(at.answer_input())
    with open(user_answers, "r", encoding="utf-8", newline="") as scores:
        score_calc = at.ScoreCalculator(scores)
        results: dict = score_calc.compute_results()
        print(results)
    sys.exit(0)


if __name__ == "__main__":
    main()
