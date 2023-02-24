"""delete text files
"""

from pathlib import Path

for txtfile in Path(".").glob("*.txt"):
    txtfile.unlink()