import ast
from collections import namedtuple
from typing import Any

Fn = namedtuple("Fn", ["name", "docstring", "body"])

class FnDefVisitor(ast.NodeVisitor):
    """Extracts and formats data from FunctionDef's in Python AST"""

    def __init__(self, src: str):
        self.src = src
        self.fns: list[Fn] = []

    def fn_body_str(self, node: ast.FunctionDef) -> str:
        """Converts the FunctionDef body to source string"""
        fn_src = ast.get_source_segment(self.src, node, padded=True)
        # The first line in the source is the function definition
        # Assuming that the function definition does not span multiple lines
        if fn_src is None:
            msg = f"Expected function source for '{node}', got None"
            raise ValueError(msg)
        return fn_src.replace(f"def {node.name}():\n", "")

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        """Visits all FunctionDef nodes in the AST"""
        fn = Fn(
            node.name,
            ast.get_docstring(node),
            self.fn_body_str(node)
        )
        self.fns.append(fn)
        return node
