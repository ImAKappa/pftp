import argparse
from pathlib import Path
from pftp.pymd import Args, main

parser = argparse.ArgumentParser()
parser.add_argument("src", type=Path, help="Python source file to convert")
parser.add_argument("-o", "--out", type=Path, help="Output file")
args = parser.parse_args()

args = Args(args.src, args.out)
main(args)

# Example: hatch run pymd "docs\1-Getting-Started\reading.py" -o "docs\1-Getting-Started\reading.txt"