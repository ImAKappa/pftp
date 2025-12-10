"""codealong

Module for writing code alongs.

A code along is a series of code snippets that demonstrate a programming example in an incremental way.
Incremental changes, whereby the tutorial writer explains their thought process, hopefully give the learner
more insight into why particular decisions are made, and also more time to digest the code their are learning to write.

Concretely, code alongs are an ordered collection of snippets,
    where a snippet is a chunk of source code + metadata.
For example, a snippet could be:

Code Along:
    Snippet 1:
        source:
            '''
            def hello(name: str) -> str:
                return f"Hello {name}
            '''
        metadata:
            comment: "The hello function has an error due to an unterminated string"
            intentionally_throws_error: true
    Snippet 2:
        source:
            '''
            def hello(name: str) -> str:
                return f"Hello {name}"
            '''
        metadata:
            comment: "We fix the hello function by correctly terminating the string"
            intentionally_throws_error: false
"""

import inspect
import logging
import re
import sys
import textwrap
from collections.abc import Callable
from dataclasses import dataclass, field
from io import StringIO
from pathlib import Path

from pftp import utils as ut

logging.basicConfig(format="%(module)s:%(message)s")
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

@dataclass
class SnippetMetadata:
    """Metadata for a snippet"""
    comment: str = ""
    intentionally_throws_error: bool = False
    intentionally_unterminating: bool = False
    prompts: list[str] = field(default_factory=list)

@dataclass
class Snippet:
    """A snippet
    
    A single chunk of source code + metadata for the learner to read, copy, and digest.
    The source code of a snippet is implemented as a function so that it can be tested and inspected.
    """
    source: Callable[[], None]
    metadata: SnippetMetadata

class CodeAlongWriter:
    """Writes code along snippets to the source file tree of the book"""

    def __init__(self, docstring_char: str = r'"""') -> None:
        self._docstring = docstring_char

    def write(self, dir: Path, snippets: list[Snippet], encoding: str = "utf-8") -> None:
        """Writes the code-along content"""
        dir.mkdir(parents=True, exist_ok=True)

        for snippet in snippets:
            f = snippet.source
            file_path = dir/f"{f.__name__}.py"
            content = self.func_to_filestring(f)
            file_path.write_text(content, encoding=encoding)
            print(f"Wrote '{file_path}'")

    def func_to_filestring(self, f: Callable[[], None]) -> str:
        """Converts a Python function to a formatted string,
        as if it were a standalone file
        """
        s = StringIO()
        s.write(self.func_to_module_docstring(f))
        s.write(self.func_body_to_filestring(f))
        return s.getvalue()

    def func_to_module_docstring(self, f: Callable[[], None]) -> str:
        """Converts name and function docstring to module docstring"""
        if f.__doc__ is None:
            raise ValueError(f"Snippet source code '{f.__name__}' is missing docstring")
        doc = inspect.cleandoc(f.__doc__)
        return f"\"\"\"{f.__name__}\n\n{doc}\n\"\"\"\n"

    def func_body_to_filestring(self, f: Callable[[], None]) -> str:
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
    """Tests snippets in a code along"""

    def test_snippets(self, snippets: list[Snippet]) -> None:
        """Check that the code blocks defined in a code along do not error."""
        print()

        for snippet in snippets:
            test_header = f"Testing '{snippet.source.__name__}'"
            print(f"{test_header}\n{len(test_header)*"-"}")

            if snippet.metadata.intentionally_unterminating:
                # TODO (2025-12-10) Maybe test for a timeout instead?
                continue
            try:
                if snippet.metadata.prompts:
                    input_stream = StringIO("\n".join(snippet.metadata.prompts))
                    sys.stdin = input_stream
                    snippet.source()
                else:
                    snippet.source()
            except KeyboardInterrupt:
                print("\tKeyboard interrupt")
            print()

class CodeAlong:
    """A code along.
    
    A series of code snippets for the learner to follow along."""

    def __init__(self, name: str, snippets: list[Snippet]) -> None:
        self.name = name
        self.snippets = snippets

        self._tester = CodeAlongTester()
        self._writer = CodeAlongWriter()

    def test(self) -> None:
        """Tests code along"""
        print(ut.underline(f"Running tests for {self.name}"))
        self._tester.test_snippets(self.snippets)

    def write(self, dir: Path) -> None:
        """Writes code along"""
        print(ut.underline(f"Writing snippets for {self.name}"))
        dir.mkdir(parents=True, exist_ok=True)
        self._writer.write(dir, self.snippets)
