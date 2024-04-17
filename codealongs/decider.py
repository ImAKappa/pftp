"""decider

Module for 'Decider' program code-along
"""
from typing import Self
from pathlib import Path
from pftp.codealong import CodeAlong, CodeAlongWriter

class Decider(CodeAlong):

    def __init__(self) -> Self:
        super().__init__("Decider")

    def decider_0(self) -> None:
        """Hard-coded list of suggestions (Part 0)"""

        things_i_could_be_doing = [
            "Exercise",
            "Study",
            "Walk the dog",
            "Party",
            "Watch anime",
            "Watch a movie",
            "Hang out with friends",
            "Start a business",
            "Doomscroll on TikTok",
            "Play volleyball"
        ]

        print(things_i_could_be_doing)

    def decider_1(self) -> None:
        """Module for solving your indecision. Computer, take the wheel 🙏 (Part 1)"""

        import random

        def decide(l: list) -> str:
            return random.choice(l)

        num_suggestions = 3
        print(f"{num_suggestions} things you could do right now:")
        print()

        things_i_could_be_doing = [
            "Exercise",
            "Study",
            "Walk the dog",
            "Party",
            "Watch anime",
            "Watch a movie",
            "Hang out with friends",
            "Start a business",
            "Doomscroll on TikTok",
            "Play volleyball"
        ]

        for i in range(num_suggestions):
            print(f"{i+1}. {decide(things_i_could_be_doing)}")

if __name__ == "__main__":
    print("Hi")
    writer = CodeAlongWriter(Decider())
    output = Path("./docs/0-The-Decider/decider")
    writer.write(output)