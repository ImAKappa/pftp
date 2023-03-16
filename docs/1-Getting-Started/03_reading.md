# 📔 Reading

To write, you must read. Let's practice reading Python code.

It also helps to know the parts of speech:

| Part of Speech | English | Part of Speech | Python | Purpose/Description |
| --- | --- | --- | --- | --- |
| Noun (instance) | that dog over there, this chair | Data | `3`, `"Hello"`, `[1, 2]` | Something that exists |
| Noun (type) | animal, furniture | Data type | `int`, `str`, `list` | A kind or type of thing |
| Pronoun | he, she, they, it | Variable | `age`, almost any english word | A placeholder for another thing |
| Verb | Run, repeat | Function | `print`, `range`, `math.sqrt` | An action |
| Conjunction | and, but, or, not | Logical operators | `and`, `or`, `not` | Joins statements with logic |

Below, we state a sentence in English and an analogous sentence in Python.

!!! warning "Type everything"

    Type all the examples to better remember Python

For each example:

1. Explain in English what you _think_ the code does.
2. Then type the code into the Thonny code editor (**avoid copy-pasting**, it is essential to develop muscle memory for writing Python)
3. Finally, run it to see if you were right

## Comments

!!! info 

    Comments are lines of text that the Python interpreter ignores.
    You usually write comments to annotate your code so that other people, and your future self, can understand your code.

    > "Code is more often read than written" 
    > 
    > \- Guido van Rossum (creator of the Python programming language)

Write "Hungry" (this is how I am feeling right now)

```python
# This is how I am feeling right now
print("Hungry")
```

## Data & Data Types (Nouns)

### Strings of Text

!!! info

    "String" is short for "string of characters"

Write the word "Apple"

```python title="String"
print("Apple")
```

Write the japanese word for "Apple"

```python title="Multilingual"
print("りんご")
```

```python title="Title case"
print("the quick brown fox jumps over the lazy dog".title())
```

```python title="Upper case"
print("the quick brown fox jumps over the lazy dog".upper())
```

```python title="Replace text"
print("the quick brown fox jumps over the lazy dog".replace("dog", "frog"))
```

```python title="Format text"
print("323 + 456 is equal to {323 + 456}")
print(f"323 + 456 is equal to {323 + 456}")
```

```python title="Split & Join"
print("the quick brown fox jumps over the lazy dog".split(" "))

print("##".join("the quick brown fox jumps over the lazy dog".split(" ")))
```

### Numbers

!!! info

    Python has two kinds of numbers:

   1. **Integers**, like `1` or `345` or `-12`
   2. **Floats**, like `3.14` or `-68.72`. These are similar to decimal numbers.

```python title="Number types"
print(f"5.3 is a {type(5.3)}")
print(f"5 is a {type(5)}")
``` 


```python title="Operators"
print(f"Addition: {5 + 2 =}")
print(f"Subtraction: {5 - 2 =}")
print(f"Multiplication: {5 * 2 =}")
print(f"Division: {5 / 2 =}")
print(f"Floor division: {5 // 2 =}")
print(f"Remainder: {5 % 2 =}")
```

```python title="Spacers"
print(478_862_301)
```

```python title="Float format"
print(f"{47.288459}")
print(f"{47.288459:.2f}")
# Percentage
print(f"{0.928:.2%}")
```

!!! note "Making numbers easier to read"

    We could write `478862301`, but that's a little tricky to read.
    Lot's of languages have ways to make numbers easier to read, including Python.

    | Language | Separator | Syntax |
    | --- | --- | --- |
    | English | comma (`,`) | `478,862,301` |
    | French | period (`.`) | `478.862.301` |
    | **Python** | underscore (`_`) | `478_862_301` |

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

```python title="if/else"
temperature = 19

if 15 <= temperature < 24:
    print("The temperature is perfect for me")
else:
    print("I'm not a fan of this temperature!")
```

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

```python title="While loop"
age = 12
age_chant = 1

while age_chant < age:
    print(f"Are you {age_chant}?")
    age_chant = age_chant + 1

print(f"Happy Birthday! You are {age_chant}!")
```

```python title="Match"
file = "cute-puppies.png"

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