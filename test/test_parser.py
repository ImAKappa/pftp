"""test_parser

This module tests the Parser class
"""

from pftp.combparser import ParserCombinator, ParserError
import pytest

p = ParserCombinator()

@pytest.fixture
def src():
    return """Life finds a way. 
Yeah, but John, if The Pirates of the Caribbean breaks down, the pirates don’t eat the tourists. 
Remind me to thank John for a lovely weekend. 
Do you have any idea how long it takes those cups to decompose. 
Just my luck, no ice. 
This thing comes fully loaded. 
AM/FM radio, reclining bucket seats, and... power windows."""

def test_tag(src):
    assert p.tag("Life finds a way", src)

    with pytest.raises(ParserError, match="Expected 'Jeff'"):
        p.tag("Jeff", src)

def test_take_while(src):
    captured, src = p.take_while(lambda c: c.isalnum() or c == ' ', src)
    assert captured == "Life finds a way"

def test_take_until(src):
    captured, src = p.take_until("John", src)
    assert captured == "Life finds a way. \nYeah, but "

    with pytest.raises(ParserError, match="Could not find 'Dinosaur'"):
        p.take_until("Dinosaur", src)