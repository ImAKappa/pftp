# 📔 Reading Python Code


To write, you must read. Let's practice reading Python code. For each example:

1. Explain in English what you _think_ the code does.
2. Then type the code into the Thonny code editor (do **not** copy-paste, it is essential that you develop muscle memory for writing Python)
3. Finally, run it to see if you were right

### Strings of Text


```python title="Title case"
print("the quick brown fox jumps over the lazy dog".title())
```

```python title="Upper case"
print("the quick brown fox jumps over the lazy dog".upper())
```

```python title="Replace text"
print("the quick brown fox jumps over the lazy dog".replace("dog", "frog"))
```

```python title="Format/Template text"
print(f"323 + 456 is equal to {323 + 456}")
```

```python title="Split & Join"
print("the quick brown fox jumps over the lazy dog".split(" "))

print("##".join("the quick brown fox jumps over the lazy dog".split(" ")))
```

### Numbers
 
```python title="Operators"
print(f"{5 + 2 =}")
print(f"{5 - 2 =}")
print(f"{5 * 2 =}")
print(f"{5 / 2 =}")
print(f"{5 // 2 =}")
print(f"{5 % 2 =}")
```

```python title="Number types"
print(f"5.3 is a {type(5.3)}")
print(f"5 is a {type(5)}")
```

### Variables

```python title="Saving data"
age = 18
print(f"My age is {age}. In ten years I will be {age + 10}")
```

```python title="Readability"
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