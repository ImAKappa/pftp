import pytest
import pftp.links as links


def test_links():
    content = """Just like writing, learning to code well takes time.
    Goole developer and leading AI-researcher Peter Norvig wrote about this best in his blog post [Teach Yourself Programming in Ten Years](https://www.norvig.com/21-days.html).
    Do not be tempted to skim! Read it over in its entirety to set your expectations for learning to code.
    """
    expected = """Just like writing, learning to code well takes time.
    Goole developer and leading AI-researcher Peter Norvig wrote about this best in his blog post [Teach Yourself Programming in Ten Years :fontawesome-solid-up-right-from-square:](https://www.norvig.com/21-days.html).
    Do not be tempted to skim! Read it over in its entirety to set your expectations for learning to code.
    """
    
    assert links.fmt_links(content) == expected

    # Should not affect LOCAL file markup
    content = """If you try typing this into Thonny,
    specifically the section of the app that says "Shell", then press `enter`:
    ![Python Syntax](./imgs.com/my.png)
    """
    print(links.fmt_links(content))
    assert links.fmt_links(content) == content

    # Links can be first in string
    content = """[Python Syntax](https://somewhere.com/file.html)"""
    assert links.fmt_links(content) == """[Python Syntax :fontawesome-solid-up-right-from-square:](https://somewhere.com/file.html)"""

def test_check_http():
    content = """Just like writing, learning to code well takes time.
    Goole developer and leading AI-researcher Peter Norvig wrote about this best in his blog post [Teach Yourself Programming in Ten Years](http://www.norvig.com/21-days.html).
    Do not be tempted to skim! Read it over in its entirety to set your expectations for learning to code.
    """
    with pytest.raises(ValueError):
        links.check_http_links(content)

    content = """Just like writing, learning to code well takes time.
    Goole developer and leading AI-researcher Peter Norvig wrote about this best in his blog post [Teach Yourself Programming in Ten Years](https://www.norvig.com/21-days.html).
    Do not be tempted to skim! Read it over in its entirety to set your expectations for learning to code.
    """
    assert links.check_http_links(content) is None