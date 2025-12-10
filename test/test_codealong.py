from pftp.codealong import CodeAlongWriter


class TestCodeAlongWriter:

    def test_func_to_str(self):
        def f() -> None:
            """A function, f"""

            print("Hello, World!")

        writer = CodeAlongWriter()
        actual = writer.func_to_filestring(f)

        expected = '''"""f

A function, f
"""

print("Hello, World!")
'''

        assert actual == expected

    def test_func_to_str_multiline_docstring(self):
        def f() -> None:
            """
            A function, f
            """

            print("Hello, World!")

        writer = CodeAlongWriter()
        actual = writer.func_to_filestring(f)

        expected = '''"""f

A function, f
"""

print("Hello, World!")
'''
        assert actual == expected


