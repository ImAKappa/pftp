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
    --8<-- "1-Getting-Started/reading/maps.py"
    ```

> ⌨️ Try typing this example into Thonny and running it using the green 'run' button.

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
| Pronoun | he, she, they, it, we, us, that, them | Variable/Identifier | `age`, almost any word | A placeholder/label/identifier for another thing |
| Verb | Run, repeat | Function | `print`, `range`, `math.sqrt` | An action |
| Conjunction | and, but, or, not | Logical operators | `and`, `or`, `not` | Joins statements with logic |

This is a rough analogy, but it's a good place as any to start.

## Data & Data Types

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
    --8<-- "1-Getting-Started/reading/filematcher.py"
    ```

    Structural pattern matching uses the keywords `match`, `case`, and `_`,
    however, the Python interpreter knows to interpret these words
    as keywords in the specific context of structural pattern matching,
    and to interpret the words as identifiers otherwise.

For each example:

1. Explain in English what you _think_ the code does.
2. Then type the code into the Thonny code editor (**avoid copy-pasting**, it is essential to develop muscle memory for writing Python)
3. Finally, run it to see if you were right

!!! warning "Type everything"

    Type all the examples to better remember Python

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

--8<-- "1-Getting-Started/reading.txt"


### Greet

=== "English"

    Write a a hello message

=== "Python"

    ```python
    """Write a a hello message"""
    print("Hello, World!")
    ```

### While Loop

=== "English"

    It's a birthday tradition to repeatedly chant "Are you 1? Are you 2? Are you ..."
    all the way up to the actual age of the birthday-person.
    Write a program that simulates this.

=== "Python"

    ```python
    """It's a birthday tradition to repeatedly chant "Are you 1? Are you 2? Are you ..."
    all the way up to the actual age of the birthday-person.
    Write a program that simulates this.
    """
    age = 12
    age_chant = 1

    while age_chant < age:
        print(f"Are you {age_chant}?")
        age_chant = age_chant + 1

    print(f"Happy Birthday! You are {age_chant}!")
    ```

### Structural Pattern Matching

=== "English"

    I have a list of files that I want to categorize. Write a program that will say the kind of each file.

=== "Python"

    ```python
    """I have a list of files that I want to categorize. Write a program that will say the kind of each file."""
    files = ["cute-puppies.png", ""]

    for file in files:
        match file.split("."):
            case [filename, ("png" | "jpg" | "webp" | "svg")]:
                print(f"'{filename}' is an image file")
            case [filename, ("csv" | "txt" | "md")]:
                print(f"'{filename}' is a plain-text file")
            case [filename, "py"]:
                print(f"'{filename}' is Python source code!")
            case _:
                print(f"Not sure what kind of file '{file}' is...")
    ```

### Strings

### Numbers



### Variables

```python title="Binding data to labels"
age = 18
print(f"My age is {age}. In ten years I will be {age + 10}")
```

```python title="Readable variable names"
seconds_per_minute = 60
minutes_per_hour = 60

seconds_per_hour = seconds_per_minute * minutes_per_hour

print(f"There are {seconds_per_hour} seconds in one hour")
```

### Sequences

```python title="Lists"
print(type([1, 2, 3]))
print(type(["a", "b", "c"]))
```

```python title="Sum of list"
print(sum([-1, -1, -1]))
```

```python title="Shorthand sum of list"
print(sum([-1] * 3))
```

```python title="List of numbers"
print(list(range(20)))
print([num for num in range(20)])
```

```python title="More lists of numbers"
print(list(range(0, 20, 2)))
print([num for num in range(20) if num % 2 == 0])
```

```python title="Dictionaries"
jojo = {"name": "Jotaro", "age": 17, "stand": "Star Platinum"}
print(jojo)
print(type(jojo))
print(jojo.keys())
print(jojo.values())
print(jojo.items())
```

### Control Flow

Write a program that will calculate income before and after taxes based on this bracketed tax scheme:

| Tax bracket | Percent tax |
| --- | --- |
| > $220,000 | 33% |
| > $150,000 | 29% |
| > $100,000 | 26% |
| > $50,000 | 20% |
| <= $50,000 | 15% |

```python title="if/elif/else statement"
income = 57456.34
tax = None

if income > 220_000:
    tax = 0.33
elif income > 150_000:
    tax = 0.29
elif income > 100_000:
    tax = 0.26
elif income > 50_000:
    tax = 0.20
elif income >= 0:
    tax = 0.15
else:
    print("Invalid income!")

if tax:
    print(f"Income before taxes: {income}")
    print(f"Income after deducting {tax*100}% taxes: {income * (1.0 - tax)}")
```

---

```python title="For loop"
countries = ["Canada", "India", "Japan", "Germany", "Venezuela", "Kenya"]

for country in countries:
    print(f"I want to visit {country}")
```

```python title="For loop (parallel)"
groceries = {
    "milk": "2 bags",
    "eggs": "1 carton",
    "strawberry shortcake": "1",
}

print("Honey, we need:")

for item, amount in groceries.items():
    print(f" {amount} {item}")
    if "cake" in item:
        print("(Keep it a surprise!)")
```

---

```python title="While loop"
age = 12
age_chant = 1

while age_chant < age:
    print(f"Are you {age_chant}?")
    age_chant = age_chant + 1

print(f"Happy Birthday! You are {age_chant}!")
```

---

I have a list of files that I want to categorize.
Write a program that will say the kind of each file.

```python title="Match"
files = [
    "cute-puppies.png",
    ""
]

match file.split("."):
    case [filename, ("png" | "jpg" | "webp" | "svg")]:
        print(f"'{filename}' is an image file")
    case [filename, ("csv" | "txt" | "md")]:
        print(f"'{filename}' is a plain-text file")
    case [filename, "py"]:
        print(f"'{filename}' is Python source code!")
    case _:
        print(f"Not sure what kind of file '{file}' is...")
```

### Functions

```python title="Basic"
def greet(name):
    print(f"Hello {name}!")

greet("world")
```

```python title="Return a value"
def fahrenheit_to_celsius(F):
    return (float(F) - 32) * (5 / 9)

print(f"100 Fahrenheit is {fahrenheit_to_celsius(100.0)} deg Celsius")
```

```python title="Default value"
def speaker(audio, volume=40.0, on=True):
    if not on:
        return "*silence*"

    if volume > 1000:
        print(" ".join(list(audio.upper())) + " ! ! !")
    elif volume > 50:
        print(audio.upper())
    else:
        print(audio.lower())
    return 

speaker("Hello is this thing on?", on=False)
speaker("Oh, wait, now it's working!")
speaker("Never gonna give you up...", volume=65.0)
speaker("Never gonna let you down...", volume=20.2)
speaker("Never gonna run around and desert you", volume=9000)
```