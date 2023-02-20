# The Python Language 🐍

Python is famous for being an easy-to-learn, yet powerful, programming language.
The Python language is, in some ways, very similar to English.
Let's compare Python and English by looking at key components of languages in general: 
1) Interpreters and 2) Syntax.

## Interpreters 👂

You can write instructions in English like

```text
Calculate the sum of the numbers 1 up to, but not including, 10
```

Of course, nothing will happen if you write down these instructions on a piece of paper,
or if you say these instructions out loud in an empty room.

Instructions in any language are only useful if there is someone there to **interpret** the instructions.
So, you text your friend the instructions to sum up the numbers. They respond with "45". Your friend is the interpreter for the instruction.

The Python language is the same. On its own the language is kind of useless, it's just a bunch of rules for how to arrange words and numbers. You need a Python **interpreter** that can understand the instructions and execute them.

!!! info "Where can I get a Python interpreter?"

    You can download the "official"[^1] Python interpreter [here](https://www.python.org/downloads/).
    This tutorial uses Python version `3.11` (or `Python 3.11` for short)

    [^1]: By "official", we mean the most up-to-date interpreter. There's no "pirated" version of the Python interpreter because it's completely open-source and free!

Follow the installation instructions for your operating system (i.e. Windows or Mac), then when the software is finished installing, test to see if Python works. We test the Python installation by running the IDLE program, which is a program that is installed alongside the Python interpreter.

!!! note "What's IDLE?"

    IDLE is the name of the Python interpreter. It stands for 
    
    - **I**ntegrated
    - **D**evelopment (and)
    - **L**earning
    - **E**nvironment

=== "Windows"

    Click the "Start" menu, then search for "Python IDLE". Open the app.

=== "Mac"

    Click the "Spotlight" menu, then search "Python IDLE". Open the app.

You should see something like this:


![Python IDLE](./imgs/python-idle-2023-02-19.png)


## Syntax 📝

**Syntax** is the structure of words in a sentence.

For example, in English we say:

```
That dog is so fluffy and cute!
```

But we wouldn't say:

```
fuffy !That so dog cute is and
```

The sentence above uses the exact same words and punctuation, but it doesn't make sense.
It doesn't use correct English syntax.

Python also has a syntax; there is a right and wrong way to structure sentences in Python.

Let's revisit the sum example, where you texted your friend:

```
Calculate the sum of the numbers 1 up to, but not including, 10
```

If you try typing this into IDLE:

![Python Syntax](./imgs/python-syntax-2023-02-19.png)


The Python interpreter doesn't understand what we're saying, because we haven't structured the sentence correctly in the Python language. Unlike your friend, the Python interpreter won't bother to ask us to clarify or rephrase what we meant. It will give up trying to understand our instructions very quickly, but will usually tell us why it gave up.
In this case, the interpreter gave up, or **threw an error**, because it didn't understand the syntax of the instruction we provided to it. The Python interpreter doesn't speak English, it speaks Python.

!!! note "Entering instructions"

    After we finish typing an instruction, we need to enter the instruction into the interpreter by pressing the `enter`/`return` key on our keyboard; this is what we mean by entering an instruction. 
    
    This is the same as when you type in a search query into Google or Bing. You have to hit enter for the search engine to actually start searching.

    After we enter an instruction, the Python interpreter will try to understand the instruction and, if it does, will return the result of the instruction on the screen

Python can be tricky initially because:

1. We're not yet fluent in the language
2. We're used to human languages, which are much more powerful and flexible than Python[^2]

[^2]: In my opinion. The interpreters for natural languages, our brains, are extraordinarily complex, flexible, and powerful, and the power of a language tends to be limited to the complexity of its interpreter.

There are lots of valid ways to ask someone to sum up the numbers 1 up to, but not including, 10 in English or any other human language. But in Python we say

```python
sum(range(1, 10))
```

![Python Syntax Part 2](./imgs/python-syntax-p12-2023-02-19.png)

Python looks like a bare-bones version of English, kind of like a cave-person language. But it's still pretty powerful.
Now imagine you text your friend

```
Calculate the sum of the numbers 1 up to, but not including, 478,862,301
```

It would probably take your friend a significantly longer amount of time to do this calculation by hand. 
But the Python interpreter just takes a few seconds:

![Python Syntax Part 3](./imgs/python-syntax-pt3-2023-02-19png.png)

!!! note "Making numbers easier to read"

    We could write `478862301`, but that's a little tricky to read.
    Lot's of languages have ways to make numbers easier to read, including Python.

    | Language | Separator | Syntax |
    | --- | --- | --- |
    | English | comma (`,`) | `478,862,301` |
    | French | period (`.`) | `478.862.301` |
    | **Python** | underscore (`_`) | `478_862_301` |


We'll look at a lot of examples of how to write Python with proper syntax throughout this tutorial.
For now, I highly recommend you try the exercises below.

## Exercises 🏋️‍♀️


**Q1.** What is an interpreter?

**Q2.** What is syntax?

**Q3.** State whether each sentence has the correct syntax in English:


a) "Hey! Hey! Hey! Frisbee! Hey! Frisbee! Frisbee!"

b) "Hey, throw the Frisbee here!"

c) "May you please pass that rotating plastic disk to my general direction by means of sudden impulse using your hands?"

d) "Frisbee here now the !throw"


**Q4.** Which of the following has the correct syntax for displaying the numbers 1 up to, but not including, 5 in Python?

!!! note "Hint"

    Try typing all these options into IDLE. The output should look like:

    ```python
    >>> ???
    1 2 3 4
    ``` 
    
    Which ones result in a syntax error? Which ones work, but don't give the correct answer?

a)
```python
print(range(1, 5))
``` 

b)
```python
print range(1, 5)
```

c)
```python
print(*range(1, 5))
```

d)
```python
print(1 up to, but not including, 5)
```

**Q5.** Calculate the sum of the numbers 1 to 53,786 using Python. You should get 1,446,493,791

!!! note "Hint"

    The sum should include the number 53,786 but remember that `range(a, b)` only includes up to `b - 1`

**Q6.** Type `help()` in the interpreter, then press the return/enter key. Read the text.

!!! info

    To quit the help menu, enter `q` or just hit the `enter` key

**Q7.** If you haven't already, skim through the [official Python tutorial](https://docs.python.org/3.11/tutorial/). A lot of it might not make sense just yet, but you should still look through it to get some more context about Python
