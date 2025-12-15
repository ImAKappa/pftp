"""fortune

Source code for 'Fortune Teller' code-along
"""

from pathlib import Path

from pftp import codealong as ca


def fortune_0() -> None:
    """Tell my fortune, oh great Pythia"""

    fortunes = [
        "'Tis certain",
        "Yes, indubitubly.",
        "Most likely",
        "Very doubtful",
        "My sources say no",
        "Reply hazy, try again.",
        "Um, you don't want to know",
    ]


def fortune_1() -> None:
    """Tell my fortune, oh great Pythia"""

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

    print(random.choice(fortunes))


def fortune_2() -> None:
    """Tell my fortune, oh great Pythia"""

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


def fortune_3() -> None:
    """Tell my fortune, oh great Pythia"""

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


def fortune_4() -> None:
    """Tell my fortune, oh great Pythia"""

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


if __name__ == "__main__":
    fortune_teller = ca.CodeAlong(
        "Fortune Telling",
        [
            ca.Snippet(fortune_0, ca.SnippetMetadata()),
            ca.Snippet(fortune_1, ca.SnippetMetadata()),
            ca.Snippet(fortune_2, ca.SnippetMetadata(prompts=["Will I go bald?"])),
            ca.Snippet(fortune_3, ca.SnippetMetadata(prompts=["Why"])),
            ca.Snippet(fortune_4, ca.SnippetMetadata(prompts=["Why?", "Goodbye"])),
        ],
    )

    fortune_teller.test()
    fortune_teller.write(Path("./docs/1-Project-Basics/fortune"))
