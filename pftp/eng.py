"""eng

This module converts Python source with special comments
into Mkdocs Material Markdown files with a specified formatting.
The idea is to compare English sentences with Python sentences.

For example, consider a Python source file with the contents:

    #eng Write 'apple' in upper case
    print('apple'.upper())

    #eng Sort a list of grocery items alphabetically
    print(sorted(['dragonfruit', 'yam', 'apple', 'banana']))


This module could convert that to Mkdocs Material syntax:

    === "Python"

        ```python
        print('apple'.upper())
        ```

    === "English"

        ```text
        Write 'apple' in upper case
        ```


    === "Python"

        ```python
        print(sorted(['dragonfruit', 'yam', 'apple', 'banana']))
        ```

    === "English"

        ```text
        Sort a list of grocery items alphabetically
        ```
"""
from collections import namedtuple
from typing import Callable

py_src = """#eng Write 'apple' in upper case
print('apple'.upper())

#eng Sort a list of grocery items alphabetically
print(sorted(['dragonfruit', 'yam', 'apple', 'banana']))
"""

print(py_src.split("#eng"))

# A collection to hold an English expression and a roughly equivalent Python expression
EngVsPy = namedtuple('EngVsPy', ['english', 'python'])

# A collection to represent the result of a parser combinator operation
Result = namedtuple('Result', ['captured', 'rest'])

class Parser:

    def take_while(src: str, fn: Callable) -> Result:
        pos = 0
        while pos < len(str) and fn(src[pos]):
            pos += 1
        return Result(src[:pos], src[pos:])

    def tag(src: str):
        """Matches a specific sequence of characters at the start of `src`"""

    def parse(src: str) -> None:
