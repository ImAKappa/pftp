password = "password1"
attempts = 0
max_attempts = 5

while True and attempts < max_attempts:
    guess = input("Enter password: ")

    if guess == password:
        break
    elif guess == "password":
        print("You need to try harder than that to break in!")
    elif guess == "abc123":
        print("Seriously? What kind of security do you think we have here?")
    elif len(guess) > 12:
        print("Sweetie, the password is less than 12 characters. Please try again!")
    else:
        print("Sorry, you entered the wrong password")
    attempts = attempts + 1

print("Access granted")