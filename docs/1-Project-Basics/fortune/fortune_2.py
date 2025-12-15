"""fortune_2

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

input("What answers do you seek, child?\n")
print(random.choice(fortunes))
