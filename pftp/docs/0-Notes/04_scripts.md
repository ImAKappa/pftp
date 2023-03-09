# 📜 Scripting

## Exception handling

```python
try:
    with open("path/to/my/file.docx") as f:
        content = f.read()
except FileNotFoundError as err:
    print(err)
except PermissionError() as err:
    print(err)
```

## 3rd-Party Packages

PyPi

GitHub

!!! danger "Security"

    How to trust 3rd party code

## Testing

Super important

* Assert statements

* Pytest

## Automation Examples

Some more complex scripts that could be used for automating work at home or in the office

These typically use 3rd packages

### Complex "Find & Replace"

re

Need to explain "Regular Expressions"

1. Extract telephone codes, email addresses, other formatted text from documents and clipboard text

### Merging & Splitting Excel files

openpyxl

pandas

pathlib

1. Split one workbook (many worksheets) into multiple workbooks
2. Merge multiple workbooks into one with many sheets

### Sending Emails

gmail api

### Mass file renaming & moving

io (stdlib)

pathlib

os

shutil

1. Append "last modified" dates to file names
2. Convert arbitrary number of folders to zipped folders

### Scheduling programs

subprocess

datetime

pathlib

1. Start and stop programs after a specified amount of time
2. Run an app at a specific time everyday or every week

### Extending clipboard

threading

maybe async

1. Let clipboard handle multiple pieces of text at a time

### Image manipulation

pillow

1. Convert all images in a folder to grayscale
2. Convert all images in a folder to a different type (PNG -> JPG or WEBP, or vice versa)
3. Resize all images in a folder to be 200 x 200 or less
4. Combine multiple images into one large image

## Webscraping

request-html

beautiful

!!! danger "Legality"

    You need to make sure to abide by "robots.txt" files, copyright law, and terms of service

    Also, don't be a pain by bombarding sites with automated requests

## Math

Custom calculator operations

### Stats & Machine learning

pytorch

tensorflow

pandas
