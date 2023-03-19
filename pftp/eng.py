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
import logging

logging.basicConfig(level=logging.WARNING)
from combparser import ParserCombinator, ParserError

# A collection to hold an English expression and a roughly equivalent Python expression
EngVsPy = namedtuple("EngVsPy", ["english", "python"])

p = ParserCombinator()

src = """#eng Write 'apple' in upper case
print('apple'.upper())

#eng Sort a list of grocery items alphabetically
print(sorted(['dragonfruit', 'yam', 'apple', 'banana']))
"""

content = []

while len(src) > 0:
    english_tag, src = p.tag("#eng", src)
    english, src = p.take_while(lambda c: c != "\n", src)
    try:
        code, src = p.take_until("#eng", src)
    except ParserError as err:
        # Take until EOF
        code, src = p.take_while(lambda c: True, src)
    eng_vs_py = EngVsPy(english=english.strip(), python=code.strip())
    logging.debug(eng_vs_py)
    content.append(eng_vs_py)


def format_eng_vs_py(evp: EngVsPy) -> str:
    return f"""=== "English"

    {evp.english}

=== "Python"

    ```python
    # {evp.english}
    {evp.python}
    ```
"""


outputs = [format_eng_vs_py(evp) for evp in content]
print("\n---\n\n".join(outputs))
