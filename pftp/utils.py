"""utils

Module for utilities
"""


def underline(s: str, char="=") -> str:
    """Underlines text"""
    return s + "\n" + char * len(s)


def overline(s: str, char="=") -> str:
    return char * len(s) + "\n" + s
