"""clippy.py

This module augments the computer clipboard with these features:

1. Modify text on the clipboard (upper, lower, title, sentence cases)
2. Quick web searching for clipped text
3. Clip a set of template text. Useful for writing emails
"""
from pathlib import Path
from datetime import date
import subprocess

# "platform" is a standard library module to get information
# about the the platform and operating system that this code is run on
import platform

def get_clipboard_command() -> str:
    """Gets the clipboard command for the host platform"""
    system = platform.system()
    clipboard = ""
    if system == "Windows":
            clipboard = "clip"
    elif system == "Linux":
            clipboard = "xclip"
    elif system == "Darwin":
            # "Darwin" is basically macOS because of historical and technical reasons...
            clipboard = "pbcopy"
    else:
        print(f"Unknown or unsupported platform named '{system}'")
    return clipboard

def get_meeting_date(day: int) -> date:
    """Get the next meeting date"""
    today = date.today()
    meeting_date = date(today.year, today.month, day)
    if meeting_date < today:
        year_carry_over, month = divmod(today.month + 1, 12)
        year = today.year + year_carry_over
        meeting_date = date(year, month, day)
    return meeting_date.strftime("%A %B %d, %Y")

def new_emails(template: str, recipients: list[str]) -> list[str]:
    """Creates new emails by filling email template with recipient data"""
    return [template.format(recipient=recipient, meeting_date=get_meeting_date(day=12)) for recipient in recipients]

if __name__ == "__main__":
    with open(Path("../data/email.txt")) as file:
        template = file.read()
        
    recipients = [
        "Marta",
        "Gailen",
        "Xiaolin",
        "Prem",
        "Anmol",
    ]
    
    clipboard = get_clipboard_command()
    
    # If clipboard exists...
    if clipboard:
        for email in new_emails(template, recipients):
            # Add another visual separator for email
            print("="*20)
            print(email)
            print("="*20)
            # Run the clipboard command
            subprocess.run([clipboard], text=True, input=email)
            # Provide a notification about things that user can't see
            print("Copied email to clipboard!")
    else:
        print("Couldn't find clipboard :O")
