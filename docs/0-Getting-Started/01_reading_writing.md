# 📝 Reading & Writing

To build up our intuition about the Python language, we'll spend this chapter reading and writing simple instructions in IDLE.

!!! danger "Do NOT Copy-Paste"

    Please do not copy paste. Type out all the characters yourself.
    Working your muscle memory through typing will significantly improve help you remember Python.

## 💬 Manipulating Text

### Title casing my essay

=== "English"

    I typed out the title of my essay in lower case, but I want it in title case.
    The title is "no mr. wallace, I will not consider the lobster".

=== "Python"

    ```python
    >>> print('no mr. wallace, I will not consider the lobster'.title())
    No Mr. Wallace, I Will Not Consider The Lobster
    ```

### Oh my gosh, like, can you believe it?

=== "English"

    My daughter says "like" way too much. To prove my point, count how many time she says "like" in her last text message to me:

    "i was like, totally ready to leave, but then like, my hair was being so weird and i like, couldnt find my gloss? And then like, the traffic was like, actually insane for a Tuesday. im like literally pulling up now though, so like, dont even be mad! Luv you, like, so much!! ✨💖"

=== "Python"

    ```python
    >>> print("I was like, totally ready to leave, but then like, my hair was being so weird and I like, couldn' find my gloss? And then like, the traffic was like, actually insane for a Tuesday. I’m like literally pulling up now though, so like, don't even be mad! Love you, like, so much!! ✨💖".count("like"))
    8
    ```

    She said "like" 8 times, can you believe it?

### Caesar Salad

=== "English"

    My friend and I are supposed to grab food,
    but he got super into cryptography lately and has only been texting me in [Caesar Ciphers](https://en.wikipedia.org/wiki/Caesar_cipher) 😭.
    Can you help me decipher his last message?

    `"Pt kvdu mvy zvtl zhshk aio"`

    He always likes to use a shift of 7 letters.


=== "Python"

    ```python
    >>> print("pt kvdu mvy zvtl zhshk aio".translate(str.maketrans("hijklmnopqrstuvwxyzabcdefg", "abcdefghijklmnopqrstuvwxyz")))
    im down for some salad tbh
    ```

## 🛣️ Making Decisions

=== "English"

    Is my password easy to guess? It's `password1`


=== "Python"

    ```python
    >>> password = "password1"
    >>> if "password" in password:
            print("Your password is easy to guess")
        else:
            print("Your password is not the worst")
    Your password is easy to guess
    ```

## 🔁 Do It Again

=== "English"

    I have a list of names that I want to format in an ordered list.
    The list is: "Johnathan", "Joseph", "Jotaro", "Josuke", "Giorno", "Jolyne", "Johnny"


=== "Python"

    ```python
    >>> names = ["Jonathan", "Joseph", "Jotaro", "Josuke", "Giorno", "Jolyne", "Johnny"]
    >>> for number, name in enumerate(names):
            print(f"{number}. {name}")
    0. Jonathan
    1. Joseph
    2. Jotaro
    3. Josuke
    4. Giorno
    5. Jolyne
    6. Johnny
    ```

## 🧮 Calculations

=== "English"

    I have $1000 in my savings account, which accumulates 2.4% interest annually.
    How much money would I have in the account by the end of the year?

=== "Python"

    ```python
    >>> principal = 1000
    >>> interest = 0.024
    >>> total = principal * (1.0 + interest)
    >>> print(f"At the end of the year, the account will have ${total}")
    ```