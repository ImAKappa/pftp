"""nojumpscare

This module contains no jumpscares
"""
import time
import webbrowser

msgs = [
    "This is not a jump scare.",
    "It really isn't.",
    "No frightening thing will suddenly appear.",
    "You do not have to be on guard.",
    "No jump scare is imminent.",
    "Trust me. Relax.",
    "Now that we've gotten acquainted.",
    "You are almost getting tired of this game now, aren't you?",
    "'Yeah yeah, I get the point, are we gonna get this jump scare done or what?'",
    "Is that what you are thinking?",
    "I can't blame you. I really can't.",
    "But you are wrong.",
    "There is no jump scare here!",
]

SECONDS = 2

for msg in msgs:
    print()
    print(f"\r{msg}", end="")
    time.sleep(SECONDS)
    # Clear the screen
    blanks = " " * len(msg)
    print(f"\r{blanks}\r", end="")

print("See? Nothing to worry about :)")
time.sleep(3)
# Heh >:)
jumpscare = "https://wallpapercave.com/wp/wp7799608.jpg"
webbrowser.open(jumpscare)
