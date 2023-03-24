# ♻️ Reuse, Reduce, Recycle

You don't have to write everything from scratch, you can reuse code that other people have written.

Python is a batteries-included language; when you downloaded the interpreter, you also downloaded a lot of extra files of code for you to freely reuse. These code files are collectively called the **standard library**. You can read more about it at the [Python Standard Library](https://docs.python.org/3/library/) documentation page.

!!! info "Python modules"

    We call a particular bundle of functionality a **module**. For example, there is a standard library module for generating random numbers called `random`. You use it like this:

    ```python
    import random

    # Prints a random integer from 1 to 10
    print(random.randint(1, 10))
    ``` 

We will use these stdlib modules for Clippy:

| Module(s) | Use case |
| --- | --- |
| `datetime` | Handle date and time data |
| `subprocess`, `platform` | Interact with operating system |
| `pathlib` | Manage files |

!!! danger "Conflict with stdlib"

    When you write your own modules, don't name them after modules found in the standard library.
    For example, if you have a module that does something with HTML you might be tempted to call it `html.py`
    But there already exists an `html` module in the stdlib.

    If you import a library that uses the stdlib `html`, it will throw an error because the Python interpreter
    will accidentally try to use your `html.py`. Chances are you haven't written all the code that it's in
    the stdlib `html` module, so your code will throw an error.

## Exercises

**Q1.** Search for the documentation, or tutorials, for each of the modules we will use for Clippy.

i. Explain what each one is for in your own words

ii. Write a Python example that uses each module