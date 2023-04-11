"""xlmerge.py

Merge separate Excel file into one
"""
from pathlib import Path
import pandas as pd

def main() -> None:
    root = Path("data")
    xls: dict[Path, pd.DataFrame] = {}
    for file in root.glob("*.xlsx"):
        xl = pd.read_excel(file)
        xls[file] = xl
    with pd.ExcelWriter(root/"combined.xlsx") as writer:
        for path, xl in xls.items():
            xl.to_excel(writer, path.stem, index=False)

if __name__ == "__main__":
    main()