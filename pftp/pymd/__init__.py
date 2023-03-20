"""Converts Python source code examples to markdown

Example: Writing mkdocs material documentation that displays English and Python sentences in a content tab

```src.py
def add_nums():
    '''Write the sum of 1 and 2'''
    print(f"{1 + 2 =}")
```

can be converted to

```output.md
### Add nums

=== "English"

    Write the sum of 1 and 2

=== "Python"

    ```python
    print(f"{1 + 2 =}")
    ```
```
"""

# TODO: Manipulate ast to test that no example throws an error

import ast
from pathlib import Path
from .visitors import Fn, FnDefVisitor
from dataclasses import dataclass

@dataclass
class Args:
    src: Path
    out: Path|None

    def __post_init__(self):
        self._validate()

    def _fmt_err(self, expected: str, found: str):
        """Raises errors"""
        return f"Expected {expected}; found {found}"

    def _validate(self) -> None:
        """Validates CLI arguments
        :raises ValueError:
        """
        if self.src.suffix != ".py":
            raise ValueError(self._fmt_err("Python source file ('.py')", self.src))

def fn_to_md(fn: Fn) -> str:
    title: str = fn.name.replace("_", " ").title()
    docstring: str = fn.docstring.replace("\n", "\n    ")
    # body: str = fn.body.replace("\n", "\n    ")
    body: str = fn.body
    """Converts a FunctionDef to markdown"""
    s = f"""### {title}

=== "English"

    {docstring}

=== "Python"

    ```python
{body}
    ```
"""
    return s

def main(args: Args):
    with open(args.src, mode="r", encoding="utf-8") as f:
        content = f.read()

    tree = ast.parse(content)
    visitor = FnDefVisitor(content)
    visitor.visit(tree)

    with open(args.out, mode="w", encoding="utf-8") as f:
        for fn in visitor.fns:
            f.write(fn_to_md(fn))