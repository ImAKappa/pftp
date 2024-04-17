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

class CodeAlong(ABC):
    """Base class for a code along"""

    def __init__(self, file_name: str, sections: list[Callable[[None], None]]) -> Self:
        self.file_name = file_name
        self._sections = sections

class CodeAlongWriter:
    """Class for writing the code-along files"""

    def __init__(self, code_along: CodeAlong,
            indent: int = 4,
            indent_amount: int = 2,
            docstring_char: str = r'"""',
        ) -> Self:
        self.code_along = code_along
        self._indent_size = indent
        self._indent_amount = indent_amount
        self._docstring = docstring_char

    def write(self, dir: Path, encoding: str = "utf-8") -> None:
        """Writes the code-along content"""
        for f in self.code_along._sections:
            file_path = dir/f"{f.__name__}.py"
            content = self.func_to_filestring(f)
            file_path.write_text(content, encoding=encoding)
            print(f"Wrote '{file_path}'")

    def _strip_indent(self, s: str) -> str:
        return s.replace(r" " * self._indent_size * self._indent_amount, "")

    def func_to_filestring(self, f: Callable[[None], None]) -> str:
        """Converts a Python function to the appropriately formatted string"""
        s = StringIO()
        docstring = f"\"\"\"{f.__name__}\n\n{f.__doc__}\n\"\"\"\n"
        s.write(self._strip_indent(docstring))
        s.write("\n")
        s.write(self.parse_func_body(f))
        s.write("\n")
        return s.getvalue()

    def parse_func_body(self, f: Callable[[None], None]) -> str:
        """Parses the body from the function"""
        src = inspect.getsource(f)
        _, src_without_doc = src.split(f.__doc__)
        lines = src_without_doc.splitlines()
        lines = [line.replace(r" "*self._indent_size*self._indent_amount, "") for line in lines]
        i = lines.index("")
        return "\n".join(lines[i+1:])
    

class CodeAlongTester:
    """Class for testing code-alongs
    
    Code-along files are either expected to:

    1. Run without error
    2. Crash and output an error

    So testing code-along files is much simpler than creating a whole pytest test suite
    """