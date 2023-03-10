# 📔 Reading

To get good at writing in a language, you need to read a lot.

It also helps to know the parts of speech:

| Part of Speech | English | Part of Speech | Python | Purpose/Description |
| --- | --- | --- | --- | --- |
| Concrete noun | dog, chair | Data | `3`, `"Hello"`, `[1, 2]` | Something that exists |
| Abstract Noun | animal, furniture | Data type | `int`, `str`, `list` | A kind or type of thing |
| Pronoun | he, she, they, it | Variable | `age`, almost any english word | A placeholder for another thing |
| Verb | Run, repeat | Function | `print`, `range`, `math.sqrt` | An action |
| Conjunction | and, but, or, not | Logical operators | `and`, `or`, `not` | Joins statements with logic |

!!! note

    These are loose analogies

Below, we state a sentence in English and an analogous sentence in Python.

!!! warning "Type everything"

    Type all the examples to better remember Python

## Data & Data Types (Nouns)

### Strings

"String" is short for "string of characters"

---

Write the word "Apple"

```python
print("Apple")
```

Write the japanese word for "Apple"

```python
print("りんご")
```

### Numbers

Python has two kinds of numbers:

1. **Integers**, like `1` or `345` or `-12`
2. **Floats**, like `3.14` or `-68.72`. These are similar to decimal numbers.

---

Add 23 and -3, then write the answer

```python
print(23 + -3)
```

Calculate $\frac{2(3 + 4.25) - 2}{5}$, then write the answer

```python
print((2*(3 + 4.25) - 2) / 5)
```

Write the remainder of 12 divided by 5

```python
print(12 % 5)
```

### Lists

A list is a collection of things

---

Write a list containing the following grocery items: apples, bananas, bread, milk, eggs

```python
print(["apples", "bananas", "bread", "milk", "eggs"])
```

Write the second item in the grocery list

```python
print(["apples", "bananas", "bread", "milk", "eggs"][1])
```

!!! warning "0-indexed counting"

    In Python, we start counting from 0.
    That's why the position, or **index**, of the second item is **1** instead of 2.

### Tuples

Also a collection of things, but you use round brackets.

??? note "Tuples vs Lists"

    You can modify a list, but not a tuple

    ```python
    groceries = ["apples", "bananas", "bread", "milk", "eggs"]
    groceries[1] = "carrots"
    print(groceries)
    ```

    ```python
    groceries = ("apples", "bananas", "bread", "milk", "eggs")
    groceries[1] = "carrots"
    print(groceries)
    ```

---

Write a collection containing the following hardware items: saw, cutting bench, power drill, level,  

```python
print(("saw", "cutting bench", "power drill", "level"))
```

### True/False (Bools)

Tell me, is 3 greater than 5?

```python
print(3 > 5)
```

Tell me, what is not true?

```python
print(not True)
```

Is -2 less than or equal to -2?

```python
print(-2 <= -2)
```

Is "Joseph" and "Josef" spelled the same?

```python
print("Joseph" == "Josef")
```

### Dictionary

A collection of mappings. A set of key-value pairs.

---

Amanda got a test score of 89, Shruthi got 87, George got 85, and Michael got 91

```python
{"Amanda": 89, "Shruthi": 87, "George": 85, "Michael": 91 }
```

## Variables (Pronouns)

Variables are things that can change their value. You can think of them as a box, or a label.

All variables have a _name_ and a _value_. You can associate a value with a name by writing `name = value`.

---

My name is "Joseph". Write my name.

```python
name = "Joseph"
print(name)
```

My age is 22. Write my age, then write my age in 10 years

```python
age = 22
print("My age is", age)
print(f"In 10 years, I will be {age + 10}")
```

!!! note "Format strings"

    In Python, you can write template strings be prepending an `f` to a string.
    Then, place any values for the template inside curly braces `{ }`

    For example,

    ```python
    clothing = "jeans"
    print(f"I am wearing {clothing} today")

    clothing = "a shirt"
    print(f"I am wearing {clothing} today")
    ``` 

## Comments

Comments are lines of text that the Python interpreter ignores.
You usually write comments to annotate your code so that other people, and your future self, can understand your code.

> "Code is more often read than written" 
> 
> \- Guido van Rossum (creator of the Python programming language)

---

Write "Hungry" (this is how I am feeling right now)

```python
# This is how I am feeling right now
print("Hungry")
```

## Functions (Verbs)

_Functions_ are actions that the Python interpreter can do.

A function can take an _input_, and can return an _output_.

---

Write a list of numbers from 1 up to (but not including) 10

```python
print(list(range(1, 10)))
```

!!! info "Built-in functions"

    The `range(start, end, step=1)` function, takes a `start` number and an `end` number, then returns
    a range of each number from start to end. Optionally, you can specify a step size between numbers.
    Try `range(1, 10, 2)`

    The `list(thing)` function tries to turn `thing` into a list.

    The `print(thing)` function writes `thing` to the computer screen.

Sum the list of numbers from 1 up to (but not including) 10

```python
print(sum(list(range(1, 10))))
```

I am working on a paper called "attention is all you need".
Could you write it in title case for me?

```python
paper_title = "attention is all you need"
print(paper_title.title())
```

Put a period between each letter of the acronym "YMMV".

```python
text_msg = "YMMV"
text_msg = ".".join(list(text_msg))
print(text_msg)
```

Say "You have so much irresistable charisma", but like you're Gen Z.

```python
phrase = "You have so much irresistable charisma"
print(phrase.replace("have", "got").replace("so much", "mad").replace("irresistable charisma", "rizz"))
```

!!! note "Methods"

    When a function is attached to a data type we call it a method

    For example, this is a function:

    ```python
    alphabet = ["Ball", "Apple", "Dog", "Car"]
    alphabet = sorted(alphabet)
    print(alphabet)
    ```

    And this is a method (notice the "dot" syntax):

    ```python
    alphabet = ["Ball", "Apple", "Dog", "Car"]
    alphabet.sort()
    print(alphabet)
    ```

## Logic (Conjunctions)

This section is related to conjunctions ("and", "or", "not"),
but goes a bit beyond parts of speech and into control flow.

**Control flow** is the logic of when and how certain parts of a program should be executed.

### Repetition

Write a countdown for a rocket launch

```python
for num in range(10, 0, -1):
    print(num)

print("Blast off!")
```

Write a numbered list of grocery items

```python
for num, item in enumerate(["apples", "milk", "bread"]):
    print(f"{num}. {item}") 
```

While we haven't reached their age, keep chanting "Are you 1?", "Are you 2?", and so on

```python
age = 12
age_chant = 1

while age_chant < age:
    print(f"Are you {age_chant}?")
    age_chant = age_chant + 1

print(f"You're {age_chant}!")
print("Happy Birthday!".upper())
```

### Control Flow

Write a program that checks if someone can legally drink.
If their age is 19 or older, welcome them. Otherwise, turn them away.

```python
age = 19

print(f"It says on your ID that you're {age}")

if age >= 19:
    print("Welcome!")
else:
    print("Sorry, I can't let you in.")
```

!!! note "Getting user input"

    Here's an interactive version of the program. The program will wait for you to type a number and press `enter`:

    ```python
    age = int(input("What is your age? "))

    print(f"It says on your ID that you're {age}")

    if age >= 19:
        print("Welcome!")
    else:
        print("Sorry, I can't let you in.")
    ```

Write a program that decides if I want to go out today.

 - I will only go outside if the weather is sunny, or if it is raining and I have an umbrella.
 - If I'm not going outside, I'm watching a popular show.

```python
weather = "sunny"
has_umbrella = True
a_popular_show = "The Last of Us"

print(f"The weather outside is {weather}")

if weather == "sunny" or (weather == "raining" and has_umbrella):
    print("I'm going for a nice walk outside")
else:
    print(f"Yeah, I'm staying inside and watching {a_popular_show} today")
```