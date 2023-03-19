"""Converts Python source code examples to markdown


"""

# TODO: Manipulate ast to test that no example throws an error
# TODO: Write a MarkDown generator

import ast
from pathlib import Path


class PyMDVisitor(ast.NodeVisitor):
    """Converts AST to specified markdown format

    Example: Writing mkdocs material documentation that displays English and Python sentences in a content tab

    ```src.py
    def add_nums():
        '''Write the sum of 1 and 2'''
        print(f"{1 + 2 =}")
    ```

    converts to =>

    ```output.md
    ### Add nums

    === "English"

        Write the sum of 1 and 2

    === "Python"

        print(f"{1 + 2 =}")
    ```

    """

    def generic_visit(self, node):
        print(f"entering {ast.dump(node)}")
        super().generic_visit(node)


p = Path(r"docs\1-Getting-Started\reading.py")

with open(p, mode="r", encoding="utf-8") as f:
    content = f.read()
    print(content)

tree = ast.parse(content)

visitor = PyMDVisitor()

visitor.visit(tree)
