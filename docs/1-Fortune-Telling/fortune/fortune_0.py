"""fortune_0

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
    "Um, you don't want to know"
]

print(random.choice(fortunes))
