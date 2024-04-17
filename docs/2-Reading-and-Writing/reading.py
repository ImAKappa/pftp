# md ### Variables

def variables():
    """There are 60 seconds per minute, and 60 minutes per hour, so there
    are 60 * 60 = 3600 seconds in one hour
    """
    seconds_per_minute = 60
    minutes_per_hour = 60

    seconds_per_hour = seconds_per_minute * minutes_per_hour

    print(f"There are {seconds_per_hour} seconds in one hour")

# md ### Control Flow


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

def if_elif_else():
    """Write a program that will calculate income before and after taxes based on this bracketed tax scheme:

    | Tax bracket | Percent tax |
    | --- | --- |
    | > $220,000 | 33% |
    | > $150,000 | 29% |
    | > $100,000 | 26% |
    | > $50,000 | 20% |
    | <= $50,000 | 15% |
    """
    income = 57456.34
    tax = None

    if income > 220_000:
        tax = 0.33
    elif income > 150_000:
        tax = 0.29
    elif income > 100_000:
        tax = 0.26
    elif income > 50_000:
        tax = 0.20
    elif income >= 0:
        tax = 0.15
    else:
        print("Invalid income!")

    if tax:
        print(f"Income before taxes: {income}")
        print(f"Income after deducting {tax*100}% taxes: {income * (1.0 - tax)}")

def for_loop():
    """Honey, can you get the groceries? We need:
    
    | Item| Amount |
    | --- | --- |
    | Milk | 2 bags |
    | Eggs | 1 carton |
    | Strawberry Shortcake | 1 cake |

    Oh, and do keep the cake a surprise!
    """
    groceries = {
        "milk": "2 bags",
        "eggs": "1 carton",
        "strawberry shortcake": "1",
    }

    print("Honey, we need:")

    for item, amount in groceries.items():
        print(f" {amount} {item}")
        if "cake" in item:
            print("(Keep it a surprise!)")

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


# md ### Functions

def functions():
    """I have an audio speaker, and if the volume is over 100 dBs it's super loud.
    Over 70 dBs is still pretty loud.
    Just be careful not to go over 120, it will definitely distort the audio.

    Oh, and make sure the speaker is actually on before you use it!
    """
    import random
    
    def jumble(s: str) -> str:
        """Jumbles each word in a string
        
        :param s: the input string
        """
        return " ".join([
            ''.join(random.sample(word, len(word))) for word in s.split(" ")
        ])

    def speaker(audio: str, volume=40.0, on=True) -> None:
        """Simulates a speaker
        
        :param audio: The audio to play
        :param volume: In decibels (dBs)
        :param on: The state of the speaker (on or off)
        """
        if not on:
            return
        dB = 1
        DISTORTION = 120.0*dB
        SUPER_LOUD = 100.0*dB
        LOUD = 70.0*dB

        if volume > DISTORTION:
            print(jumble(audio))
        elif volume > SUPER_LOUD:
            print(" ".join(list(audio.upper())) + " ! ! !")
        elif volume > LOUD:
            print(audio.upper())
        else:
            print(audio.lower())

    speaker("Hello is this thing on?", on=False)
    speaker("Oh, wait, now it's working!")
    speaker("Never gonna give you up...", volume=65.0)
    speaker("Never gonna let you down...", volume=20.2)
    speaker("Never gonna run around and desert you", volume=9001.0)
