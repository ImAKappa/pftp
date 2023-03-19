from typing import Callable
from collections import namedtuple

# A collection to represent the result of a parser combinator operation
Result = namedtuple("Result", ["captured", "rest"])


class ParserError(Exception):
    """Base-class for parser errors"""


class ParserCombinator:
    """Simple parser. Might use later"""

    def tag(self, starting_txt: str, src: str) -> Result:
        """Matches a specific sequence of characters at the start of `src`"""
        if src.startswith(starting_txt):
            return Result(starting_txt, src[len(starting_txt) :])
        else:
            raise ParserError(f"Expected '{starting_txt}'")

    def take_while(self, fn: Callable[[str], bool], src: str) -> Result:
        """Takes while `fn` is true"""
        pos = 0
        while pos < len(src) and fn(src[pos]):
            pos += 1
        return Result(src[:pos], src[pos:])

    def take_until(self, txt: str, src: str):
        """Takes until `txt` is found"""
        pos = src.find(txt)
        if pos == -1:
            raise ParserError(f"Could not find '{txt}'")
        return Result(src[:pos], src[pos:])

    def parse(src: str) -> None:
        raise NotImplementedError
