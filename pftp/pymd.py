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

    print(f"{1 + 2 =}")
```
"""

# TODO: Manipulate ast to test that no example throws an error
# TODO: Write a MarkDown generator

import ast
from pathlib import Path
from typing import Any
from collections import namedtuple

Fn = namedtuple("Fn", ["name", "docstring", "body"])

def fn_to_md(fn: Fn) -> str:
    title: str = fn.name.replace("_", " ").title()
    body: str = fn.body.replace('\n', '\n    ')
    """Converts a FunctionDef to markdown"""
    s = f"""### {title}

=== "English"

    {fn.docstring}

=== "Python"

    ```python
    {body}
    ```
"""
    return s

class FnDefVisitor(ast.NodeVisitor):
    """Extracts and formats data from FunctionDef's in Python source code"""

    def __init__(self, src: str):
        self.src = src
        self.fns: list[Fn] = list()

    def fn_body_str(self, node: ast.FunctionDef) -> str:
        """Converts the FunctionDef body to a string of the source"""
        return "\n".join([ast.get_source_segment(self.src, n) for n in node.body])

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        fn = Fn(
            node.name,
            ast.get_docstring(node),
            self.fn_body_str(node)
        )
        self.fns.append(fn)
        return node


p = Path("docs/1-Getting-Started/reading.py")

with open(p, mode="r", encoding="utf-8") as f:
    content = f.read()
    # print(content)

tree = ast.parse(content)

visitor = FnDefVisitor(content)

visitor.visit(tree)

for fn in visitor.fns:
    print(fn_to_md(fn))