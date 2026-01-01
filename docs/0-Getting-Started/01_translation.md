# 🗣️ Lost in Translation

To build up our intuition about the Python language, we'll spend this chapter looking at English-to-Python translations.
You should expect to feel confused, especially because many aspects of the way in which we communicate in English are lost in translation when we write code to accomplish a task.

!!! danger "Do NOT Copy-Paste"

    Please do not copy paste. Type out all the characters yourself.
    Working your muscle memory through typing will significantly help you remember Python.

## 💬 Texting

### Title casing my essay

=== "English"

    I typed out the title of my essay in lower case, but I want it in title case.
    The title is "no mr. wallace, I will not consider the lobster"[^1].

    [^1]: I actually was persuaded by David Foster Wallace's [essay](https://www.columbia.edu/~col8/lobsterarticle.pdf) and I do try to consider the lobster.

=== "Python"

    ```python
    >>> print('no mr. wallace, I will not consider the lobster'.title())
    No Mr. Wallace, I Will Not Consider The Lobster
    ```

---

Notice that English is much more verbose than the Python equivalent.
Additionally, in Python we have to be much more explicit with our instructions,
even needing to remind the computer to actually print out the title-cased essay title.

Another thing to note is the difference in meaning of punctuation; `.` is a period in English, marking the end of a sentence. However, in Python, a `.` joins an **object** (here, the string of text `'no mr. wallace ...'`) and a **method** (here, the `title()` method). We will come back around to methods later on in the book, but in a nutshell a method is simply a verb or the action which we want the computer to execute.

!!! info "To `print()` or not to `print()`, that is the question"

    In IDLE, we can actually dispose of the call to `print()` and instead write:

    ```python
    >>> 'no mr. wallace, I will not consider the lobster'.title()
    'No Mr. Wallace, I Will Not Consider The Lobster'
    ```

    You will notice the output is now surrounded by quotes.
    Using `print()` seems to not really add much value - either way we get the title-cased essay title,
    but `print()` is necessary in later examples, and especially once we move away from IDLE. 

### Oh my gosh, like, can you believe it?

=== "English"

    My friend says "like" way too much. To prove my point, count how many time she says "like" in her last text message to me:

    "i was like, totally ready to leave, but then like, my hair was being so weird and i like, couldnt find my gloss? And then like, the traffic was like, actually insane for a Tuesday. im like literally pulling up now though, so like, dont even be mad! Luv you, like, so much!! ✨💖"

=== "Python"

    ```python
    >>> "I was like, totally ready to leave, but then like, my hair was being so weird and I like, couldn' find my gloss? And then like, the traffic was like, actually insane for a Tuesday. I’m like literally pulling up now though, so like, don't even be mad! Love you, like, so much!! ✨💖".count("like")
    8
    ```

    She said "like" 8 times, like, can you believe it?

---

Similar to the previous example, to ask the computer to count the occurrences of "like", we take our object of interest (the string of text) and follow it by a `.` and the appropriate method.
Unlike `.title()`, the `count()` method accepts another object, which we call the **argument**. In this case, the argument is the word `"like"`.

### Caesar Salad

=== "English"

    My friend and I are supposed to grab food,
    but he got super into cryptography lately and has only been texting me in [Caesar Ciphers](https://en.wikipedia.org/wiki/Caesar_cipher) 😭.
    Can you help me decipher his last message?

    `"Pt kvdu mvy zvtl zhshk aio"`

    He always likes to use a shift of 7 letters, e.g. the letter `a` was replaced with `h`, `b` with `i`, etc.


=== "Python"

    ```python
    >>> 'pt kvdu mvy zvtl zhshk aio'.translate(str.maketrans('hijklmnopqrstuvwxyzabcdefg', 'abcdefghijklmnopqrstuvwxyz'))
    'im down for some salad tbh'
    ```

---

This is a more complicated example, and we won't concern ourselves too much with how it works for now.
You may only really understand this once you finish the book.

Instead, let's try an exercise. Modify the above code so that the cipher goes the other way, converting the string of text `im down for some salad tbh` into the ciphered message `pt kvdu mvy zvtl zhshk aio`.
Hint: You just have to swap around some strings of text, no need to add or remove any code.

??? success "Answer"

    ```python
    >>> 'im down for some salad tbh'.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'hijklmnopqrstuvwxyzabcdefg'))
    'pt kvdu mvy zvtl zhshk aio'
    ```

## 🧮 Calculations

### Taxes for Axes

=== "English"

    In Canada, the Goods & Sales Tax rate is 13%. This means a box of raspberries selling for $2.00 CAD really will cost you $2.26 CAD.

    If I buy an axe listed at a retail price of $39.98 CAD, how much would I pay after tax? 

=== "Python"

    ```python
    >>> round(39.98 * 1.13, 2)
    45.18
    ```
---

Python can be used as a calculator too! In fact, it is a much more powerful calculator than the calculator app on your smartphone, because it has a wide assortment of "buttons" like `round` and offers you the flexibility to create your own "buttons" as needed (though that topic - **functions** - will come later in the book).

!!! tip "Variable Names and Readability"

    When writing code, it's important to think about readability. In the English translations, we have so much rich context (we know the axe costs $39.98, there is a particular tax rate, etc.).

    However, the Python translation above is very opaque if you didn't already have the context of what the numbers meant in English translation.
    We can improve the readability of the code by using **variable names**. Here is an alternative Python translation that better preserves the context from English:

    ```python
    >>> gst = 1.13
    >>> axe_retail_price = 39.98
    >>> axe_full_price = round(axe_retail_price * gst, 2)
    >>> axe_full_price
    45.18
    ```

    We could go a step further and make use of strings of text:

    ```python
    >>> gst = 1.13
    >>> axe_retail_price = 39.98
    >>> axe_full_price = axe_retail_price * gst
    >>> print(f"The price of the axe after tax is ${axe_full_price:.2f} CAD.")
    The price of the axe after tax is $45.18 CAD
    ```

    This is a common way to format information in Python.
    We wll revisit this in a later chapter.

## 🏋️ Exercises

TBD
