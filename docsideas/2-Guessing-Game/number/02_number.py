"""number

This module simulates a number guessing game
"""
import random

def main() -> None:
    # 1. Think of a random number from 1 to 100 (inclusive)
    number = random.randint(1, 100+1)
    print("I'm thinking of a number from 1 to 100")
    # 2. Ask for guess until they get it right
    # 3. Every time user guesses, give feedback ("Higher" or "Lower")

if __name__ == "__main__":
    main()