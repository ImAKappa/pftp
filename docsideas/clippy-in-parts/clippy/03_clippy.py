"""clippy.py

This module augments the computer clipboard with these features:

1. Modify text on the clipboard (upper, lower, title, sentence cases)
2. Quick web searching for clipped text
3. Clip a set of template text. Useful for writing emails
"""
from pathlib import Path

if __name__ == "__main__":
    with open(Path("../data/email.txt")) as file:
        email = file.read()
        
    # Generate emails for multiple recipients
    recipients = [
        "Marta",
        "Gailen",
        "Xiaolin",
        "Prem",
        "Anmol",
    ]
        
    for recipient in recipients:
        print(email.format(recipient=recipient, meeting_date="Dec 12"))
        print("="*20)