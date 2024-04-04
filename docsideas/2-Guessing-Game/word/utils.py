"""utils

Utility functions
"""
import platform
import os

def strip_newline(s: str) -> str:
    return "".join(s.split())

def clear_screen() -> None:
    """Clears stdout"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def fmt_title(s: str, underline="=") -> str:
    """Format a title"""
    return f"{s}\n{underline*len(s)}"

if __name__ == "__main__":
    import time
    demo_txt = "Hello\n"
    print(f"{demo_txt!r}")
    print(fmt_title(strip_newline(demo_txt)))
    print("Clearing screen in 2 seconds")
    time.sleep(2)
    clear_screen()
    print("Screen cleared!")