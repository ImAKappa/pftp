# 📔 Reading

## 👀 Reading Python

> "Code is more often read than written" 
> 
> \- [Guido van Rossum :fontawesome-solid-up-right-from-square:](https://en.wikipedia.org/wiki/Guido_van_Rossum) (creator of the Python programming language)

Python is famous for being a **readable** language.
The words we use in Python, and the way we string words together, is very reminiscent of English.

For example, if we wanted to tell our friend to open Google Maps for various countries, we could write:

=== "English"

    Repeat the following for each country in this list of countries:

    "Canada", "Italy", "Cambodia", "Kenya", and "Japan"

    1. Type [https://www.google.com/maps/place/](https://www.google.com/maps/place/) (the Google Maps url) into a new browser tab
    2. Add the country to the end of the url, like [https://www.google.com/maps/place/Canada](https://www.google.com/maps/place/Canada)
    3. Hit enter to go to the website

=== "Python"

    ```python title="maps.py"
    --8<-- "3-Reading-and-Writing/reading/maps.py"
    ```

!!! tip "Try it yourself"

    Try typing this example into Thonny and running it using the green 'run' button.

Now, although Python is a readable language, this example is still probably confusing.
Take some time to study the example, and come up with **3** things that confuse you.

??? success "Possibly confusing things"

    - What does `import webbrowser` mean?
    - What's with the underscore in `maps_url`?
    - Why is `webbrowser.open_new_tab(MAPS_URL + country)` indented?
    - Why do we need the `.` and the round brackets `(` and `)`
    - What's with the colon (`:`), or the square brackets (`[` and `]`)?

To develop our fluency, we will practice translating between English and Python.

## 🔣 Parts of Speech

When learning a language, it's helpful to know the parts of speech:

| Part of Speech | English | Part of Speech | Python | Purpose/Description |
| --- | --- | --- | --- | --- |
| Noun (instance) | that dog there, this chair | Data | `3`, `[1, 2]`, `"Hello"`,  | Something that exists |
| Noun (type) | animal, furniture | Data type | `int`, `list`, `str` | A kind or type of thing |
| Pronoun | he, she, they, it, we, us, that, them | Placeholder for a noun | `age`, almost any word | A placeholder/label/identifier for data |
| Verb | Run, repeat | Function | `print`, `range`, `math.sqrt` | An action |
| Conjunction | and, but, or, not | Logical operators | `and`, `or`, `not` | Joins statements with logic |

This is a rough analogy, but it's a good place as any to start.

## Variable (Pronoun)

In Python, we can identify data with a name like so:

```python
my_name = "Reyna"
```

!!! tip "snake_case"

    Python variable names are written in **snake_case**. This means

    1. All lower case letters
    2. Underscores in place of spaces

!!! warning "Valid variable names"

    Variable names can use the characters `A - Z`, `a - z`, `0 - 9`, `_`

    Note that the first character cannot be a digit

## Data & Data Types (Nouns)

Data is information. In Python, this information comes in the form of numbers, text, and collections of numbers or text.

### 🔢 Numbers

Python has two kinds of numbers:

1. **Integers**, like `1` or `345` or `-12`
2. **Floats**, like `3.14` or `-68.72`. These are similar to decimal numbers.

!!! note "Making numbers easier to read"

    We could write numbers like `478862301`, but that's a little tricky to read.
    Lot's of languages have ways to make numbers easier to read, including Python.

    | Language | Separator | Syntax |
    | --- | --- | --- |
    | English | comma (`,`) | `478,862,301` |
    | French | period (`.`) | `478.862.301` |
    | **Python** | underscore (`_`) | `478_862_301` |

### 🅰️ Strings

Strings are text.

In Python, we surround text with double quotes (`"`) or single-quotes (`'`).
It's up to you which one to use, but be consistent.

If you want to write text that spans multiple lines, use triple quotes:

```python
"""This is some text.
It spans multiple lines
"""

'''Multi-line text can also
be surrounded
with triple-single quotes
'''
```

### 🫙 Lists

Lists are a collection of items.

```python title="List of numbers"

```

```python title="List of strings"
["Apple", "Banana", "Pear", "Plum", "Strawberry"]
```

```python title="List of stuff"

```

## Meta

### 💬 Comments

Comments are lines of text that the Python interpreter ignores.
You usually write comments to annotate your code so that other people, and your future self, can understand your code.



=== "English"

    Write "Hungry" (this is how I am feeling right now)

=== "Python"

    ```python
    # This is how I am feeling right now
    print("Hungry")
    ```

### 🔑 Keywords

**Keywords** are reserved words in Python; they mean something specific to the Python interpreter,
in the same way that almost all of our English words mean something specific.

The keywords include:

| Keyword| Purpose |
| --- | --- |
| `for`, `while`, `else`, `continue`, `break`, `in`, `yield` | Repetition/loops |
| `if`, `elif`, `else`, `True`, `False`, `and`, `or`, `not` | Conditional logic |
| `def`, `return`, `lambda` | Functions |
| `import`, `from`, `as` | Importing modules |
| `try`, `except`, `finally`, `raise` | Exception handling |
| `del`, `global`, `nonlocal` | Memory |
| `class`| Classes |
| `assert` | testing |
| `async`, `await`| Asynchronous programing |
| `pass` | Multiple uses |

You **cannot** use these words as identifiers because otherwise the Python interpreter will get confused.

!!! note "Soft keywords"

    Python 3.10 introduced [Structral pattern matching :fontawesome-solid-up-right-from-square:](https://peps.python.org/pep-0636/),
    an extremely powerful feature to handle complex data structures.
    For example,

    ```python title="filematcher.py"
    --8<-- "3-Reading-and-Writing/reading/filematcher.py"
    ```

    Structural pattern matching uses the keywords `match`, `case`, and `_`,
    however, the Python interpreter knows to interpret these words
    as keywords in the specific context of structural pattern matching,
    and to interpret the words as identifiers otherwise.

## 📃 Cheatsheets

The examples here are purposefully a little more complicated because there are already so many articles, books, and cheatsheets with simple Python examples.

!!! note "You don't have to remember everything"

    If you ever forget how to do something in Python, see the [resources](../05_resources/) section for advice on how to search for help

I recommend studying (and typing out) the examples at [Python Cheat Sheet :fontawesome-solid-up-right-from-square:](https://www.pythoncheatsheet.org/).
Ideally, you would work your way through all of the sections over a few weeks or months.
But if you are short on time or energy, read the following in this order:

1. [Basics :fontawesome-solid-up-right-from-square:](https://www.pythoncheatsheet.org/cheatsheet/basics)
2. [Built-in Functions :fontawesome-solid-up-right-from-square:](https://www.pythoncheatsheet.org/cheatsheet/built-in-functions)
3. [Manipulating Strings :fontawesome-solid-up-right-from-square:](https://www.pythoncheatsheet.org/cheatsheet/manipulating-strings)
4. [String formatting :fontawesome-solid-up-right-from-square:](https://www.pythoncheatsheet.org/cheatsheet/string-formatting)
5. [Control Flow :fontawesome-solid-up-right-from-square:](https://www.pythoncheatsheet.org/cheatsheet/control-flow)
6. [Functions :fontawesome-solid-up-right-from-square:](https://www.pythoncheatsheet.org/cheatsheet/functions)
7. [Lists and Tuples :fontawesome-solid-up-right-from-square:](https://www.pythoncheatsheet.org/cheatsheet/lists-and-tuples)
8. [Dictionaries :fontawesome-solid-up-right-from-square:](https://www.pythoncheatsheet.org/cheatsheet/dictionaries)
9. [Sets :fontawesome-solid-up-right-from-square:](https://www.pythoncheatsheet.org/cheatsheet/sets)
10. [Comprehensions Step-by-Step :fontawesome-solid-up-right-from-square:](https://www.pythoncheatsheet.org/blog/python-comprehensions-step-by-step)


## Examples

For each example:

1. Explain in English what you _think_ the code does.
2. Then type the code into the Thonny code editor (**avoid copy-pasting**, it is essential to develop muscle memory for writing Python)
3. Finally, run it to see if you were right

!!! warning "Type everything"

    Type all the examples to better remember Python

---

--8<-- "3-Reading-and-Writing/reading.txt"