"""clippy.py

This module augments the computer clipboard with these features:

1. Modify text on the clipboard (upper, lower, title, sentence cases)
2. Quick web searching for clipped text
3. Clip a set of template text. Useful for writing emails
"""
from pathlib import Path
# "datetime" is a standard library module that provides functionality
# for handling dates.
# "date" is a specific bundle of code for date-related functionality
from datetime import date

def get_meeting_date() -> date:
    """Get the next meeting date"""
    # The day the script is run
    today = date.today()
    return date(today.year, today.month, 12)

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
        
    for email in new_emails(template, recipients):
        print(email)
        print("="*20)