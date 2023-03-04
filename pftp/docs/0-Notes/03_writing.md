# ✍️ Writing

## 1. Login Authentication

Write a passive-agressive login authenticator.

1. Let the user access the system if they give the correct password.
2. But if they try to guess "password" tell them they need to try harder than that to get in!
3. And if they try "abc123", give an exasperated response.
4. And if they try anything longer than 12 characters, gently remind them that the password can't be that long.
5. Also, the user only has 5 attempts to log in. If they fail all 5, print a message saying to try again later. 
6. Otherwise, tell them they entered the wrong password.

??? success "Possible solution"

    ```python title="password.py" linenums="1"
    --8<-- "password.py"
    ```

## 2. Fetching Useless Facts


When you type in a website URL in your browser, your browser has to download the website from another computer. Your browser asks the other computer for the website, and the other computer always responds with a status code.

Two important status codes are:

- `200`: everything is ok and the website has been successfully transferred to your browser
- `404`: the other computer couldn't find the website files, so it says "page not found"

Go to [https://uselessfacts.jsph.pl/api/v2/facts/random :fontawesome-solid-up-right-from-square:](https://uselessfacts.jsph.pl/api/v2/facts/random)

> If you see some text, great, the other computer returned a status code of 200.

Now try [https://uselessfacts.jsph.pl/api/v2/facts/random1 :fontawesome-solid-up-right-from-square:](https://uselessfacts.jsph.pl/api/v2/facts/random1)

> You probably got a `404` "page not found" status code.

Based on what you just learned about status codes, try to complete the Python script below: 

```python title="ueslessfact.py" linenums="1"
--8<-- "uselessfact_incomplete.py"
```

??? success "Possible solution"

    ```python title="ueslessfact.py" linenums="1"
    --8<-- "uselessfact.py"
    ```

## 3. Powerball

Write a program that simulates the chances of winning the [Powerball :fontawesome-solid-up-right-from-square:](https://www.powerball.ca/how-to-play/), and how much money you would realistically need to spend on to win.

> "To play Powerball, you must fill in a draw ticket by choosing five main numbers up to 69 and a sixth 'Powerball' number from 1-26"

Use the code below to get started:

1) Calculate your earnings

| Matching Draw | Amount ($)|
| --- | --- |
| 5 + Powerball | Jackpot ($60 million) |
| 5| US $1,000,000 |
| 4 + Powerball | US $50,000 |
| 4 | US $100 |
| 3 + Powerball | US $100 |
| 3 | US $7 |
| 2 + Powerball | US $7 |
| 1 + Powerball | US $4 |
| 0 + Powerball | US $4 |

2) For notable winnings (Grand prize, 1 million, and 50 thousand), print a message

```python title="powerball.py" linenums="1"
--8<-- "powerball_incomplete.py"
```

??? success "Possible solution"

    ```python title="powerball.py" linenums="1"
    --8<-- "powerball.py"
    ```