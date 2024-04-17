"""decider

Module for 'Decider' program code-along
"""
from typing import Self
from pathlib import Path
from pftp.codealong import CodeAlong, CodeAlongWriter

class Decider(CodeAlong):

    def __init__(self) -> Self:
        super().__init__("Decider",
            sections=[
                self.decider_0,
                self.decider_1,
                self.decider_2,
            ]               
        )

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


    def decider_2(self) -> None:
        """This time, let's make use of `random.choices` method"""

        import random

        def decide(l: list, top_n: int = 3) -> str:
            return random.choices(l, k=top_n)
        
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

        for i, item in enumerate(decide(things_i_could_be_doing)):
            print(f"{i+1}. {item}")

if __name__ == "__main__":
    print("Decider")
    writer = CodeAlongWriter(Decider(), indent_amount=2)
    output = Path("./docs/0-The-Decider/decider")
    writer.write(output)