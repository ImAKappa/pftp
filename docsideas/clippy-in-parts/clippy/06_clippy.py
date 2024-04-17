"""clippy.py

This module augments the computer clipboard with these features:

1. Modify text on the clipboard (upper, lower, title, sentence cases)
2. Quick web searching for clipped text
3. Clip a set of template text. Useful for writing emails
"""
from pathlib import Path
from datetime import date

# Refactor the day as an argument to the function
def get_meeting_date(day: int) -> date:
    """Get the next meeting date"""
    today = date.today()
    
    meeting_date = date(today.year, today.month, day)
    # Change the format of the date to Weekday Month Day, Year
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
        
    for email in new_emails(template, recipients):
        print(email)
        print("="*20)