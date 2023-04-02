"""links

This module formats links
"""
import re

def fmt_links(content: str) -> str:
    """Formats links
    
    Every link should have:

    - :fontawesome-solid-up-right-from-square:
    """
    # Modified from https://davidwells.io/snippets/regex-match-markdown-links
    pattern = re.compile(r"\[([\w\s\d]+)\]\((https:\/\/[\w\d.\/?=#-]+)\)")
    # return re.sub(pattern, r"[\1 :fontawesome-solid-up-right-from-square:](\2)", content)
    return re.sub(pattern, r"[\1 :fontawesome-solid-up-right-from-square:](\2)", content)

def check_http_links(content: str) -> None:
    """Raises error if http links found (not secure)"""
    pattern = re.compile(r"\[([\w\s\d]+)\]\((http:\/\/[\w\d.\/?=#-]+)\)")
    matches = re.findall(pattern, content)
    if matches:
        raise ValueError(f"Found unsecure http: {matches}")