"""fortune_4

Tell my fortune, oh great Pythia
"""

import random

fortunes = [
    "'Tis certain",
    "Yes, indubitubly.",
    "Most likely",
    "Very doubtful",
    "My sources say no",
    "Reply hazy, try again.",
    "Um, you don't want to know",
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
