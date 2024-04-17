# ♻️ Reuse, Reduce, Recycle

You and your friends want to go out and do something fun, but none of you can agree on what to do.
To help you make a decision, you decide to write a computer program that will make the decision for you.

You create a file named `decision.py`, and add the following lines:

```python
activities = [
    "Boardgame Cafe",
    "Movies",
    "Roller skating",
    "Video Games",
    "Karaoke",
    "Amusement Park"
]
```

You don't have to write everything from scratch, you can reuse code that other people have written.

Python is a batteries-included language; when you downloaded the interpreter, you also downloaded a lot of extra files of code for you to freely reuse. These code files are collectively called the **standard library**. You can read more about it at the [Python Standard Library :fontawesome-solid-up-right-from-square:](https://docs.python.org/3/library/) documentation page.

!!! info "Python modules and packages"

    We call a particular bundle of functionality a **packages**. For example, there is a standard library module for generating random numbers called `random`. You use it like this:

    ```python
    import random

    # Prints a random integer from 1 to 10
    print(random.randint(1, 10))
    ```

    Packages are composed of many Python **modules**. A module is a single Python file like `myfile.py`

!!! danger "Conflict with stdlib"

    When you write your own modules, don't name them after modules found in the standard library.
    For example, if you have a module that does something with HTML you might be tempted to call it `html.py`
    But there already exists an `html` module in the stdlib.

    If you import a library that uses the stdlib `html`, it will throw an error because the Python interpreter
    will accidentally try to use your `html.py`. Chances are you haven't written all the code that it's in
    the stdlib `html` module, so your code will throw an error.

## 🏋️ Exercises

<!-- **Q1.** Search for the documentation, or tutorials, for each of the modules we will use for Clippy.

i. Explain what each one is for in your own words

ii. Write a Python example that uses each module -->