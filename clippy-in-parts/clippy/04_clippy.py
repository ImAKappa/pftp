"""clippy.py

This module augments the computer clipboard with these features:

1. Modify text on the clipboard (upper, lower, title, sentence cases)
2. Quick web searching for clipped text
3. Clip a set of template text. Useful for writing emails
"""
from pathlib import Path

# Refactor code to a function.
# The functionality doesn't change,
# but it's much easier to extend the code and understand what it does
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
        
    # Call function here
    for email in new_emails(template, recipients):
        print(email)
        print("="*20)
