"""clippy.py

This module augments the computer clipboard with these features:

1. Modify text on the clipboard (upper, lower, title, sentence cases)
2. Quick web searching for clipped text
3. Clip a set of template text. Useful for writing emails
"""
# "pathlib" is a standard module library that handles file paths
# "Path" is an object that handles file paths
from pathlib import Path

if __name__ == "__main__":
    # Read and save content from email.txt
    with open(Path("../data/email.txt")) as file:
        email = file.read()
    
    # Print content to shell
    print(email.format(recipient="Marta", meeting_date="Dec 12"))
