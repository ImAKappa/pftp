"""clipfinder

This module extracts structured text from your clipboard.
This includes:

- telephone numbers
- emails
- dates

See https://projects.lukehaas.me/regexhub/ for more useful patterns
"""

import pyperclip
import re

def displaymatch(match):
    if match is None:
        return 'No matches!'
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

patterns = {
    "email": re.compile("[\w.-]+@[\w.-]+\.\w+"),
    "phone number": re.compile("\(\d\d\d\)\s\d\d\d-\d\d\d\d")
}

if __name__ == "__main__":
    print('Clipfinder'.center(30, '='))
    print()

    # Clear clipboard
    pyperclip.copy("")

    # Get clipboard value
    print('Wating for clipboard to update...')
    value = pyperclip.waitForNewPaste()
    # print(value)
    print("Clipboard updated!")
    print()

    # Extract data
    for name, pattern in patterns.items():
        print(f'{name}\n{"-"*len(name)}\n')
        for result in re.findall(pattern, value):
            print(f'\t{result}')
        print()