"""decider

Module for 'Decider' program code-along
"""
from typing import Self
from pathlib import Path
from pftp.codealong import CodeAlong, CodeAlongWriter, CodeAlongTester

class FortuneTeller(CodeAlong):

    def __init__(self) -> Self:
        super().__init__("Fortune Teller",
            sections=[
                self.fortune_0,
                self.fortune_1,
                self.fortune_2,
                self.fortune_3,
            ]     
        )

    def fortune_0(self) -> None:
        """Tell my fortune, oh great Pythia"""

        import random

        fortunes = [
            "'Tis certain",
            "Yes, indubitubly.",
            "Most likely",
            "Very doubtful",
            "My sources say no",
            "Reply hazy, try again.",
            "Um, you don't want to know"
        ]

        print(random.choice(fortunes))

    def fortune_1(self) -> None:
        """Tell my fortune, oh great Pythia"""

        import random

        fortunes = [
            "'Tis certain",
            "Yes, indubitubly.",
            "Most likely",
            "Very doubtful",
            "My sources say no",
            "Reply hazy, try again.",
            "Um, you don't want to know"
        ]

        input("What answers do you seek, child?\n")
        print(random.choice(fortunes))


    def fortune_2(self) -> None:
        """Tell my fortune, oh great Pythia"""

        import random

        fortunes = [
            "'Tis certain",
            "Yes, indubitubly.",
            "Most likely",
            "Very doubtful",
            "My sources say no",
            "Reply hazy, try again.",
            "Um, you don't want to know"
        ]

        prompt = input("What answers do you seek, child?\n")

        if prompt.endswith("?"):
            print(random.choice(fortunes))
        else:
            print("That is a statement.")

    def fortune_3(self) -> None:
        """Tell my fortune, oh great Pythia"""

        import random

        fortunes = [
            "'Tis certain",
            "Yes, indubitubly.",
            "Most likely",
            "Very doubtful",
            "My sources say no",
            "Reply hazy, try again.",
            "Um, you don't want to know"
        ]

        while True:
            prompt = input("What answers do you seek, child?\n")
            if prompt.endswith("?"):
                print(random.choice(fortunes))
            elif prompt == "Goodbye":
                print("Until next time 🐍")
                break
            else:
                print("That is a statement.")
            print()

if __name__ == "__main__":

    tester = CodeAlongTester()
    tester.test_for_errors(FortuneTeller())

    writer = CodeAlongWriter()
    output = Path("./docs/1-Fortune-Telling/fortune")
    writer.write(output, FortuneTeller())