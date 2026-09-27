# 📦 Scripts vs Apps vs Libraries

A **script** is a short piece of code, usually in a single file, that does one main thing.
For example, this script fetches a random useless fact from the internet:

```python title="uselessfact.py"
--8<-- "uselessfact.py"
```

!!! tip "Try it yourself"

    You don't need to _how_ this code works at this point in the guide, but try typing this code into
    the code editor section of Thonny (the top portion, not the Shell).
    Then press the green run button, and look at the Shell section to see the result.

    ![uselessfact.py in Thonny](./img/01_programming-thonny_useless_fact-2024-06-14.png)

    Try re-running the script a few times to see different useless facts.

Scripts are different from applications, or **apps**, which are bundles of code that you use to accomplish one or more tasks. 
Apps are typically more complicated than scripts.
Compare the script above to something like your calendar app, which can send notifications, set reminders, store data related to events, dates, and times, has a user interface, and can synchronize data across multiple devices.

There is another kind of software called a **library**.
A library is a bundle of code that is meant to be used in other people's code.
Libraries tend to be pretty hard to write because you have to think about how the code will be used on many different operating systems, and write lots of tests, publish documentation on how to use the library, and maintain it when people find bugs or are looking for more features.
Python developers typically use the word "**packages**" instead of library.
[PyPI](https://pypi.org/) is where you can find Python packages. 

Specific to Python, we have **modules**. These are files with reusable bits of code.
Python comes pre-installed with many modules.
For example, we can use the `random` module which lets us write code that can generate random numbers

```python title="Python random module"
import random
print("Here's a random number from 1 to 10:", random.randint(1, 10))
```

We need to write `import random` to tell the Python interpreter to load the code from the random module.
It's a good thing the interpreter doesn't automatically load every single built-in module,
otherwise it would take a while to start up. Better for us to explicitly ask for just the specific modules we need.

!!! note

    In this guide, we will stick to writing modules and scripts

## 🏋️‍♂️ Exercises

**Q2.** What is the difference between a script, an app, and a library? Provide an example for each

??? success "Answer"

    | Type of Software | Description | Example |
    | --- | -- | --- |
    | Script | Typically a single file of code that accomplishes a few simple/short tasks | A script to download files from the internet |
    | App | A bundle of software that people use to accomplish a few complicated tasks | [Thonny](https://thonny.org/) is an app for editing Python code |
    | Library| A bundle of software that people can use in their own code | [pandas](https://pandas.pydata.org/) is data analysis library for Python |