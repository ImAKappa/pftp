# md ### Control Flow


def greet():
    """Write a a hello message"""
    print("Hello, World!")


def while_loop():
    """It's a birthday tradition to repeatedly chant "Are you 1? Are you 2? Are you ..."
    all the way up to the actual age of the birthday-person.
    Write a program that simulates this.
    """
    age = 12
    age_chant = 1

    while age_chant < age:
        print(f"Are you {age_chant}?")
        age_chant = age_chant + 1

    print(f"Happy Birthday! You are {age_chant}!")


def structural_pattern_matching():
    """I have a list of files that I want to categorize. Write a program that will say the kind of each file."""
    files = [
        "cute-puppies.png",
        "national-security.pdf",
        "pinball3000.exe",
        "mywebsite.html",
        "birthday.py",
        "mysterious-file.cia",
    ]

    for file in files:
        match file.split("."):
            case [filename, ("png" | "jpg" | "webp" | "svg")]:
                print(f"'{filename}' is an image file")
            case [filename, ("csv" | "txt" | "md")]:
                print(f"'{filename}' is a plain-text file")
            case [filename, ("exe" | "pkg")]:
                print(f"'{filename}' is an executable")
            case [filename, ("pdf" | "docx")]:
                print(f"'{filename}' is a document file")
            case [filename, "py"]:
                print(f"'{filename}' is Python source code!")
            case _:
                print(f"Not sure what kind of file '{file}' is...")
