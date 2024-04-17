"""focus

This module helps me focus by showing me puppy photos after a focus period,
and a "time to to focus" message after a quick break.
"""
import time
import webbrowser

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
    webbrowser.open("https://eyebleach.me/dogs/")
    for second in range(SEC_PER_MIN * BREAK_MIN):
        # Pause 1 second
        time.sleep(1)
        print(f"[BREAK] {second+1} seconds has passed")
    # Back to work!
    webbrowser.open("https://www.animalbehaviorcollege.com/wp-content/uploads/2021/11/DogCatMoney-768x564.jpg")

def main():
    NUM_FOCUS_SESSIONS = 3
    for session in range(NUM_FOCUS_SESSIONS):
        print(f"Session {session+1}/{NUM_FOCUS_SESSIONS}")
        start = input("Start focus? [y]/n: ")
        if start == "y":
            start_focus()
            start_break()
        elif start == "n":
            print("Ok, stopping app")
            break
        else:
            print(f"Expected 'y' or 'n', instead got {start}. Stopping app.")
            break

if __name__ == "__main__":
    main()