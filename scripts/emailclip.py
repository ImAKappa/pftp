"""emailclip.py
This module copies a sequence of email templates to the clipboard.
"""

# "subprocess" lets us send commands to the operating system
import subprocess
# "platform" provides information about the operating system
import platform
# "datetime" provides date and time related methods
from datetime import date
from dateutil.relativedelta import relativedelta

def get_clipboard_command() -> str:
    """Ask operating system to put data on the clipboard"""
    clipboard = ""
    system = platform.system()
    match system:
        case "Windows":
            clipboard = "clip"
        case "Linux":
            clipboard = "xclip"
        case "Darwin":
            # MacOS - "Darwin" is the name of the core of MacOS
            clipboard = "pbcopy"
        case _:
            raise ValueError(f"Cannot find clipboard app for unknown or unsupported OS named '{system}'")
    return clipboard

def get_next_meeting_date(meet_day: int) -> date:
    """Determines the date of the next MLM meeting"""
    today = date.today()
    meet_date = date(today.year, today.month, meet_day)
    # Check if this month's meeting has passed
    if today > meet_date:
        meet_date = meet_date + relativedelta(months=1)
    return meet_date

def fill_template(recipient: str):
    """Generates an email template"""
    meeting_date = get_next_meeting_date(meet_day=12)
    template = f"""Dear {recipient.upper()},

Would you be interested in joining my Essential Oils MLM Business?
We have information sessions on the 12th of every month.
The next one is {meeting_date.strftime("%A %d. %B %Y")}.

We hope to see you there!

Sincerely,

Alex S. Chamer
"""
    return template

if __name__ == "__main__":
    program_name = "Email Clipper v0.1.0"
    emphasis_chars = 4
    print(program_name.center(len(program_name)+emphasis_chars*2, "="))
    
    recipients = [
        "Beenu",
        "Bilbo",
        "Borwein",
        "Boromir",
        "Bella",
        "Beatrice",
    ]
    
    try:
        clipboard_cmd = get_clipboard_command()
    except ValueError as err:
        print(err)
        raise SystemExit
    
    try:
        # Generate emails
        for i, recipient in enumerate(recipients):
            email = fill_template(recipient)
            subprocess.run(clipboard_cmd, text=True, input=email)
            print(f"Attached {recipient}'s email to clipboard ({i+1}/{len(recipients)})")
            input(f"Next email?")
            print()
        # Clear the clipboard
        subprocess.run(clipboard_cmd, text=True, input="")
    except FileNotFoundError as err:
        print(err)
        raise SystemExit
    else:
        print("Finished generating emails!")
    finally:
        print("Ending program. Goodbye!")
