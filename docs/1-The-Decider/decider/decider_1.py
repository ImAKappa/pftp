"""decider_1

Module for solving your indecision. Computer, take the wheel 🙏 (Part 1)
"""

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
