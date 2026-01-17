# 🗣️ Lost in Translation

To build up our intuition about the Python language, we'll spend this chapter looking at English-to-Python translations.
You should expect to feel confused, especially because many aspects of the way in which we communicate in English are lost in translation when we write code to accomplish a task.

!!! danger "Do NOT Copy-Paste"

    Please do not copy paste. Type out all the characters yourself.
    Working your muscle memory through typing will significantly help you remember Python.

You should type out all the examples in **IDLE**, and remember not type the prompt characters (`>>>`).

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

Another thing to note is the difference in meaning of punctuation; `.` is a period in English, marking the end of a sentence. However, in Python, a `.` joins an **object** (here, the string of text `'no mr. wallace ...'`) and a **method** (here, the `title()` method). We will come back around to methods later on in the book, but in a nutshell a method is simply a verb or the action which we want the computer to execute on an object.

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

    My friend says "like" way too much. To prove my point, count how many time she said "like" in her last text message:

    "i was like, totally ready to leave, but then like, my hair was being so weird and i like, couldnt find my gloss? And then like, the traffic was like, actually insane for a Tuesday. im like literally pulling up now though, so like, dont even be mad! Luv you, like, so much!! ✨💖"

=== "Python"

    ```python
    >>> "I was like, totally ready to leave, but then like, my hair was being so weird and I like, couldn' find my gloss? And then like, the traffic was like, actually insane for a Tuesday. I’m like literally pulling up now though, so like, don't even be mad! Love you, like, so much!! ✨💖".count("like")
    8
    ```

    She said "like" 8 times, like, can you believe it?

---

Similar to the previous example, to ask the computer to count the occurrences of "like", we take our object of interest (the string of text) and follow it by a `.` and the appropriate method.
Unlike `.title()`, the `count()` method accepts another object, which we call the **argument** in general. In this case, the argument to the `count()` method is the string of text `"like"`.

Try replacing every instance of the word "like" with "RAHH" using the `replace()` method. How many arguments does it accept?

??? success "Answer"

    ```python
    >>> "I was like, totally ready to leave, but then like, my hair was being so weird and I like, couldn' find my gloss? And then like, the traffic was like, actually insane for a Tuesday. I’m like literally pulling up now though, so like, don't even be mad! Love you, like, so much!! ✨💖".replace("like", "RAHH")
    "I was RAHH, totally ready to leave, but then RAHH, my hair was being so weird and I RAHH, couldn' find my gloss? And then RAHH, the traffic was RAHH, actually insane for a Tuesday. I’m RAHH literally pulling up now though, so RAHH, don't even be mad! Love you, RAHH, so much!! ✨💖"
    ```

    The `replace()` method accepts two arguments: the first is the word to replace (e.g. "like") and the second is the word to replace with (e.g. "RAHH").

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

    Does the solution make sense to you?

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

!!! tip "Variables and Readability"

    When writing code, it's important to think about readability. In the English translations, we have so much rich context (we know the axe costs $39.98, there is a particular tax rate, etc.).

    However, the Python translation above is very opaque if you didn't already have the context of what the numbers meant in English translation.
    We can improve the readability of the code by using **variables**. Here is an alternative Python translation that better preserves the context from English:

    ```python
    >>> gst = 1.13
    >>> axe_retail_price = 39.98
    >>> axe_full_price = round(axe_retail_price * gst, 2)
    >>> axe_full_price
    45.18
    ```

    Notice that words in the variable name are connected by `_` instead of spaces like you would expect.
    There are many rules for valid and invalid variable names that we will explain in a later chapter.
    
    We could also go a step further and make use of strings of text:

    ```python
    >>> gst = 1.13
    >>> axe_retail_price = 39.98
    >>> axe_full_price = axe_retail_price * gst
    >>> print(f"The price of the axe after tax is ${axe_full_price:.2f} CAD.")
    The price of the axe after tax is $45.18 CAD
    ```

    This is a common way to format information in Python.
    We wll revisit this in a later chapter.

## 🗓️ Dates & Times

### Birthday Weekday

=== "English"

    My birthday was on May 15, 2002. What day of the week was that?

=== "Python"

    ```python
    >>> from datetime import date
    >>> import calendar
    >>> birthday = date(2002, 5, 15)
    >>> calendar.day_name[birthday.weekday()]
    'Wednesday'
    ```

---

Try modifying the code above to figure out what day of the week you were born!

!!! info "What are we importing?"

    Notice the `from datetime import date` and `import calendar`. These kind of imports are not like the imports of countries. Instead, we are importing additional code into the Python interpreter's memory.
    The Python interpreter you downloaded comes with a lot of extra features to do computations with math, dates, text, the internet, and many more things - but you have to explicitly ask for those features.

    Here's another example. Say we wanted to our computer to generate a random number from 1 to 100.
    The Python interpreter comes with random number generating features that we can load like this:

    ```python
    >>> import random
    >>> random.randint(1, 101)
    35
    ```

    Why 101 instead of 100? Well it's because the second argument to the `random.randint()` is exclusive - this means the random number generator will go up to, but not including, 101.
    
    How would you know that? Well, I just told you so now you know it. But if you ever come across a Python feature you don't know and I'm not there to tell you, definitely check out the [documentation](https://docs.python.org/3/library/random.html#random.randint). While you can ask your favourite AI assistant as well, be warned that the information you get from them might not always be correct.

### Days Until Christmas

=== "English"

    Today is Halloween, Oct 31st. How many days are there until Christmas?

=== "Python"

    ```python
    >>> from datetime import date
    >>> halloween = date(2025, 10, 31)
    >>> christmas = date(2025, 12, 25)
    >>> christmas - halloween
    datetime.timedelta(days=55)
    ```

---

Subtracting two date objects yields a timedelta (i.e. time difference) object which tells us that there are 55 days between Halloween and Christmas.

How many days are there between Valentine's Day and Christmas?

??? success "Answer"

    ```python
    >>> from datetime import date
    >>> valentines = date(2025, 2, 14)
    >>> christmas = date(2025, 12, 25)
    >>> christmas - valentines
    datetime.timedelta(days=314)
    ```

    If you have already imported `date`, then you don't need to run `from datetime import date` again. But also no harm if you do run it again.

## 🏋️ Exercises

In the first few questions, we will learn how to instruct our computers to calculate things for us.
For each question, enter the correct Python instructions into IDLE:

**Q1.** `60 / 12 = ?`

??? success "Answer"

    ```python
    >>> 60 / 12
    5.0
    ```

**Q2.** How many seconds in a week?

??? success "Answer"

    There are 60 seconds per minute, 60 minutes per hour, 24 hours per day, and 7 days per week.
    Multiply all of those together and you get the total number of seconds per week.

    ```python
    >>> 60 * 60 * 24 * 7
    604800
    ```

    We can improve readability with variables:

    ```python
    >>> sec_per_min = 60
    >>> min_per_hour = 60
    >>> hours_per_day = 24
    >>> days_per_week = 7
    >>> sec_per_week = sec_per_min * min_per_hour * hours_per_day * days_per_week
    >>> sec_per_week
    604800
    ```

**Q3.** I invited 12 friends over for a party. Let's say each person eats a minimum of 2 slices. How many 8-slice pizzas should I buy at minimum?

??? success "Answer"

    I will need $12 \times 2 = 24$ slices, minimum. 24 slices divided by 8 slices per pizza yields 3 pizzas.

    ```python
    >>> 12 * 2 / 8
    3.0
    ```

    We can improve readability with variables:

    ```python
    >>> party_size = 12
    >>> slices_per_person = 2
    >>> slices_per_pizza = 8
    >>> pizzas = party_size * slices_per_person / slices_per_pizza
    >>> pizzas
    3.0
    ```
---

In next series of exercises, the main problem is to determine if it's worth speeding.

**Q4.** I need to make it to my daughter's ballet recital in 15min.
Fortunately, I just need to take a single road from my work to the ballet studio,
which is 15km away. The road has a speed limit of 50 kilometers (km) / hour (hr) because it's a small residential area.

If I drive the speed limit, will I make it in time? Write a Python program to verify if I can make it.

??? success "Answer"

    You should really try to solve this yourself before looking for answers.
    You cannot learn to program without thinking through it, noodling around with the numbers, and taking a stab at the problem.

    If you are stuck on writing the Python program, at least work out the answer on pencil and paper (or with a calculator or an Excel spreadsheet).

    If you need a hint, I cannot make it in time for the ballet. But you should be able to figure out how many minutes I will be late by on your own.

    ??? success "Answer"

        If I travel at 50km/hr, it will take me 18 minutes to travel 15km.
        Here is the calculation in Python:

        ```python
        >>> speed = 50
        >>> distance = 15
        >>> time_in_hours = speed / distance
        >>> time_in_min = time * 60
        >>> time_in_min
        18
        >>> time_limit = 15
        >>> late_by = time_in_min - time_limit
        >>> late_by
        3
        ```

**Q5.** How fast do I need to go to make it to the ballet on time?

??? success "Answer"

    Speed is just distance (km) over time (hr), so we compute:

    ```python
    >>> distance = 15
    >>> time_in_min = 15
    >>> time_in_hr = time_in_min / 60
    >>> speed = distance / time_in_hr
    60
    ```

    Just 10km/hr over the speed limit. Worth it if I can get to the show on time!
