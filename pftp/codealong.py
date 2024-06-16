"""progress

Module for displaying code inprogress.
Useful for managing code-along files.
"""
from typing import Self, Callable
from abc import ABC
import inspect
from pprint import pprint
from io import StringIO
from pathlib import Path
import re
import textwrap

import logging
logging.basicConfig(format="%(module)s:%(message)s")
log = logging.getLogger(__name__)
log.setLevel(logging.WARNING)

class CodeAlong(ABC):
    """Base class for a code along"""

    def __init__(self, file_name: str, sections: list[Callable[[None], None]]) -> Self:
        self.file_name = file_name
        self._sections = sections

# TODO: Refactor
class CodeAlongWriter:
    """Class for writing the code-along files"""

    # FIXME: Don't accept a code along in the `init` function, accept in a separate function
    def __init__(self,
            docstring_char: str = r'"""',
        ) -> Self:
        self._docstring = docstring_char

    def write(self, dir: Path, code_along: CodeAlong, encoding: str = "utf-8") -> None:
        """Writes the code-along content"""
        for f in code_along._sections:
            file_path = dir/f"{f.__name__}.py"
            content = self.func_to_filestring(f)
            file_path.write_text(content, encoding=encoding)
            print(f"Wrote '{file_path}'")

    def func_to_filestring(self, f: Callable[[None], None]) -> str:
        """Converts a Python function to a formatted string,
        as if it were a standalone file
        """
        s = StringIO()
        s.write(self.func_to_module_docstring(f))
        s.write(self.func_body_to_filestring(f))
        log.debug(s.getvalue())
        return s.getvalue()
    
    def func_to_module_docstring(self, f: Callable[[None], None]) -> str:
        """Converts name and function docstring to module docstring"""
        doc = inspect.cleandoc(f.__doc__)
        return f"\"\"\"{f.__name__}\n\n{doc}\n\"\"\"\n"

    def func_body_to_filestring(self, f: Callable[[None], None]) -> str:
        """Converts the body of a function to a string, preserving identation"""
        src = inspect.getsource(f)
        # Strip docstring
        re_docstring = r'"""[\s\S]+"""\n'
        signature, body = re.split(re_docstring, src)
        # inspect preserves absolute indentation,
        #   but we want to only preserve relative identation
        body = textwrap.dedent(body)
        return body
    

class CodeAlongTester:
    """Class for testing code-alongs
    
    For now, we assume that code blocks shouldn't error.
    In the future, I might define blocks that intentionally error.
    """

    def test_for_errors(self, code_along: CodeAlong) -> None:
        """Check that the code blocks defined in a code along do not error."""
        print("")

        for section in code_along._sections:
            # In case some example code has an intentional indefinite loop
            try:
                section_title = f"Testing '{section.__name__}'"
                print(f"{section_title}\n{len(section_title)*"-"}")
                section()
            except KeyboardInterrupt as err:
                print("\tKeyboard interrupt")
            print()