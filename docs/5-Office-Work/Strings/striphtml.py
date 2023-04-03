"""striphtml

This module strips html tags from blocks of text
"""

from io import StringIO
from html.parser import HTMLParser


class HTMLStripper(HTMLParser):
    """Class that strips html tags from text"""

    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        # A buffer for string data
        self.text = StringIO()

    def handle_data(self, data: str) -> None:
        """Adds data (within html tags), to string buffer"""
        self.text.write(data)

    def get_data(self):
        """Returns value in string buffer"""
        return self.text.getvalue()


def strip_tags(html: str) -> str:
    s = HTMLStripper()
    s.feed(html)
    return s.get_data()


def main():
    source_html = """<address>
  <p>
    Chris Mills<br />
    Manchester<br />
    The Grim North<br />
    UK
  </p>

  <ul>
    <li>Tel: 01234 567 890</li>
    <li>Email: me@grim-north.co.uk</li>
  </ul>
</address>
    """
    msg = "Stripped HTML"
    print(f'{msg}\n{"-"*len(msg)}')
    stripped_input = strip_tags(source_html)
    print(stripped_input)
    print()


if __name__ == "__main__":
    main()
