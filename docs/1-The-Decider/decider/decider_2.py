"""decider_2

This time, let's make use of `random.choices` method
"""

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
