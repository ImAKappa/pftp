"""birthday

This script celebrates birthdays

1. User enters their birth year, month, and day
2. If today is their birthday, print the happy birthday song!
3. If it's not their birthday, count how many days until their next birthday
"""
from datetime import date
import time

def ask_birthday() -> str:
    """Asks the user to input their birthday"""
    year = int(input("What year were you born? [YYYY] "))
    month = int(input("And the month? [MM] "))
    day = int(input("Finally, what day? [DD] "))
    return date(year, month, day)

def count_days_until_next_bday(birthday: date) -> int:
    """Counts the number of days until the user's next birthday"""
    today = date.today()
    next_bday = date(today.year, birthday.month, birthday.day)
    # Wait, but what if your birthday this year has already passed?
    if today > next_bday:
        next_bday = date(next_bday.year + 1, next_bday.month, next_bday.day)
    days = (next_bday - today).days
    return days

def sing_happy_bday(name: str, inv_speed: int = 0.1) -> None:
    """Sing happy birthday at a specified speed
    
    :param name: the name of the birthday person
    :param inv_speed: inverse speed; higher number means slower song
    """
    song = "Happy Birthday to you!\n" * 2
    song += f"Happy Birthday dear {name}\n"
    song += "Happy Birthday to you!\n"
    print()
    for c in song:
        print(c, end="", flush=True)
        # This gives a typing effect
        time.sleep(inv_speed)
    print()
    return

def main():
    name = input("What's your name? ")
    birthday = ask_birthday()
    today = date.today()

    if today.month == birthday.month and today.day == birthday.day:
        sing_happy_bday(name)
    else:
        num_days_left = count_days_until_next_bday(birthday)
        print(f"Only {num_days_left} {'day' if num_days_left == 1 else 'days'} until your next birthday!")

main()