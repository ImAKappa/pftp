# 🔁 Starting Fresh

Isn't Clippy working just fine? Why should we start again?[^1]

[^1]: I was inspired to structure the tutorial this way by [Luna's brilliant "Make A Language" series](https://arzg.github.io/lang/10/)

The script we made:

1. It is hard to maintain and extend. If we keep adding features it will eventually become one gargantuan file that will be a major pain to modify.
   
    1. What if we want to store `recipients` in an external file or a database, instead of hard-coding it directly into the script file?

    2. What if we want to point the script to templates at different paths on our computer? 

    3. Support for generating multiple templates at a time? 

    4. Consider if we want to save the filled-templates to their own files or zip folder?
   
2. No exception handling! The code is not robust because we didn't gracefully handle possible errors

    1. What if we try to fill a template with a variable that isn't actually in the template?

    1. What should the script do if `email.txt` goes missing, gets renamed, or can't be opened for security reasons?

    2. How should we handle errors with `subprocess.run()` due to some operating system issue?

3. No tests! We should **always** write tests for our code

    1. How do we know for sure that our `get_meeting_date()` function works when the next month is in the next year?

    2. How could we test that the `get_clipboard_command()` function works for other operating systems, even if we might not be able to actually run the code on other operating systems?


The second half of this tutorial series involves rebuilding Clippy from the ground up using **best practices**.
