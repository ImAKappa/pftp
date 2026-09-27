# 📔 Reading

!!! danger "✏️ Section undergoing re-write"

    Feel free to peruse, but there are likely errors or miscommunicated ideas.

## 👀 Reading Python

!!! quote "Code is more often read than written"
     
    \- [Guido van Rossum :fontawesome-solid-up-right-from-square:](https://en.wikipedia.org/wiki/Guido_van_Rossum) (creator of the Python programming language)

Python is famous for being a **readable** language.
The words we use in Python, and the way we string words together, is very reminiscent of English.

For example, if we wanted to tell our friend to open Google Maps for various countries, we could write:

=== "English"

    Repeat the following for each country in this list of countries:

    "Canada", "Italy", "Cambodia", "Kenya", and "Japan"

    1. Type [https://www.google.com/maps/place/](https://www.google.com/maps/place/) (the Google Maps url) into a new browser tab
    2. Add the country to the end of the url, like [https://www.google.com/maps/place/Canada](https://www.google.com/maps/place/Canada)
    3. Hit enter to go to the website

=== "Python"

    ```python title="maps.py"
    import webbrowser

    maps_url = "https://www.google.com/maps/place/"
    countries = ["Canada", "Italy", "Cambodia", "Kenya", "Japan"]

    for country in countries:
        webbrowser.open_new_tab(maps_url + country)
    ```

!!! tip "Try it yourself"

    Try typing this example into Thonny and running it using the green 'run' button.

Now, although Python is a readable language, this example is still probably confusing.
Take some time to study the example, and come up with **3** things that confuse you.

??? success "Possibly confusing things"

    - What does `import webbrowser` mean?
    - What's with the underscore in `maps_url`?
    - Why is `webbrowser.open_new_tab(MAPS_URL + country)` indented?
    - Why do we need the `.` and the round brackets `(` and `)`
    - What's with the colon (`:`), or the square brackets (`[` and `]`)?

To develop our fluency, we will practice translating between English and Python.

## Examples

For each example:

1. Explain in English what you _think_ the code does.
2. Then type the code into the Thonny code editor (**avoid copy-pasting**, it is essential to develop muscle memory for writing Python)
3. Finally, run it to see if you were right

!!! warning "Type everything"

    Type all the examples to better remember Python

---