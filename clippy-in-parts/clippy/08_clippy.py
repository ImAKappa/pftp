"""clippy.py

This module augments the computer clipboard with these features:

1. Modify text on the clipboard (upper, lower, title, sentence cases)
2. Quick web searching for clipped text
3. Clip a set of template text. Useful for writing emails
"""
from pathlib import Path
from datetime import date

# "subprocess" is a standard library module that can run other programs
# on the computer
import subprocess

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
        
    for email in new_emails(template, recipients):
        print(email)
        # Run the clipboard command on Windows
        subprocess.run(["clip"], text=True, input=email)
        # Run the clipboard command on macOS
        # subprocess.run(["pbcopy", text=True, input=email])
        print("="*20)