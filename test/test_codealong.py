import pytest
from pftp.codealong import CodeAlong, CodeAlongWriter

def test_codealong():
    from typing import Self
    from pathlib import Path

    class HelloWorld(CodeAlong):

        def __init__(self) -> Self:
            super().__init__("Hello World", 
                sections=[
                    self.hello_world_1,
                    self.hello_world_2,
                ]
            )
            
        def hello_world_1(self) -> None:
            """Module for 'Hello, World!' program - part 1"""
            
            print("Hello, World!")

        def hello_world_2(self) -> None:
            """Module for 'Hello, World!' program - part 2"""

            if __name__ == "__main__":
                print("Hello, World!")

    writer = CodeAlongWriter(HelloWorld(), indent_amount=3)
    root_dir = Path("./test/codealong")
    writer.write(root_dir)


    expected = '''"""hello_world_1

Module for 'Hello, World!' program - part 1
"""

print("Hello, World!")
'''

    assert (root_dir/"hello_world_1.py").read_text() == expected


    expected = '''"""hello_world_2

Module for 'Hello, World!' program - part 2
"""

if __name__ == "__main__":
    print("Hello, World!")
'''

    assert (root_dir/"hello_world_2.py").read_text() == expected

def test_codealong_multiple_idents():
    assert False