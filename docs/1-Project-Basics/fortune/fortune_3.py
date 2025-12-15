"""fortune_3

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

prompt = input("What answers do you seek, child?\n")

if prompt.endswith("?"):
    print(random.choice(fortunes))
else:
    print("That is a statement.")
