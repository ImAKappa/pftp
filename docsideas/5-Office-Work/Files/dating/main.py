"""dating

This module adds the last modified date to a file name
"""
from datetime import datetime
import os
from pathlib import Path
import time

def modification_date(filename: Path) -> datetime:
    t = os.path.getmtime(filename)
    return datetime.fromtimestamp(t)

def prepend_modified_date(root: Path) -> None:
    """Prepends the last modified date of each file to the name of the file"""
    for file in root.iterdir():
        last_modification = modification_date(file)
        file.rename(root/f"{last_modification:%Y-%b-%d}-{file.name}")

def main() -> None:
    root = Path("fakedata")
    prepend_modified_date(root)

if __name__ == "__main__":
    main()