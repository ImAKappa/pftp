"""focus

This module helps me focus by showing me puppy photos after a focus period,
and a "time to to focus" message after a quick break.
"""
import time

def start_focus():
    SEC_PER_MIN = 60
    FOCUS_MIN = 25
    for second in range(SEC_PER_MIN * FOCUS_MIN):
        # Pause 1 second
        time.sleep(1)
        print(f"[FOCUS] {second+1} seconds has passed")

def start_break():
    SEC_PER_MIN = 60
    BREAK_MIN = 5
    for second in range(SEC_PER_MIN * BREAK_MIN):
        # Pause 1 second
        time.sleep(1)
        print(f"[BREAK] {second+1} seconds has passed")

def main():
    start = input("Start focus? [y]/n: ")
    if start == "y":
        start_focus()
        start_break()
    elif start == "n":
        print("Ok, stopping app")
    else:
        print(f"Expected 'y' or 'n', instead got {start}. Stopping app.")


if __name__ == "__main__":
    main()