password = "password1"
attempts = 0
max_attempts = 5
login_is_successful = False

while attempts < max_attempts:
    guess = input("Enter password: ")

    if guess == password:
        login_is_successful = True
        break
    elif guess == "password":
        print("You need to try harder than that to break in!")
    elif guess == "abc123":
        print("Seriously? What kind of security do you think we have here?")
    elif len(guess) > 12:
        print("Sweetie, the password is 12 characters or less. Please try again!")
    else:
        print("Sorry, you entered the wrong password")
    attempts = attempts + 1

if login_is_successful:
    print("Access granted. Not sure what you have access to, but enjoy nontheless")
else:
    print("Login failed. Try again in 36 minutes")