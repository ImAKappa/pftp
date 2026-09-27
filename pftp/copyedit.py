"""links

Module for formatting links
"""

import re
from pathlib import Path

# TODO(2026-09-26) Deprecate
# def fmt_links(content: str) -> str:
#     """Formats links

#     Every link should have:

#     - :fontawesome-solid-up-right-from-square:
#     """
#     # Modified from https://davidwells.io/snippets/regex-match-markdown-links
#     pattern = re.compile(r"\[([\w\s\d]+)\]\((https:\/\/[\w\d.\/?=#-]+)\)")
#     # return re.sub(pattern, r"[\1 :fontawesome-solid-up-right-from-square:](\2)", content)
#     return re.sub(pattern, r"[\1 :fontawesome-solid-up-right-from-square:](\2)", content)


def check_http_links(content: str) -> None:
    """Raises error if http links found (not secure)"""
    pattern = re.compile(r"\[([\w\s\d]+)\]\((http:\/\/[\w\d.\/?=#-]+)\)")
    matches = re.findall(pattern, content)
    if matches:
        msg = f"Found unsecure http: {matches}"
        raise ValueError(msg)


def copyedit(dir: Path) -> None:
    """Copy edit a directory of coding tutorial files"""
    for p in dir.rglob("*.md"):
        content = p.read_text()

        check_http_links(content)

if __name__ == "__main__":
    copyedit(Path("dir"))
