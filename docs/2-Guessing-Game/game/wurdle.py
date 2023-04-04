"""wurdle

A guessing game
"""

import random
from pathlib import Path
from dataclasses import dataclass
import tomllib
import os
import platform

@dataclass
class Settings:
    max_guesses: int
    word_list: Path

def load_settings(config_file: Path) -> Settings:
    with open(config_file, mode="rb") as file:
        settings = tomllib.load(file)
    return Settings(max_guesses=settings["max_guesses"], word_list=Path(settings["word_list"]))
    
def rand_word(words: Path) -> str:
    with open(words, mode="r", encoding="utf-8") as file:
        words = file.readlines()

    word = ""
    while len(word) < 4:
        word: str = random.choice(words)
        # Strip any extra newlines from word
        word = "".join(word.split())
    return word

def validate_guess(guess: str) -> None:
    if len(guess) > 1:
        raise ValueError("Guess a single letter!")
    if not guess.isalpha():
        raise ValueError("The guess should be a letter!")
    
def clear() -> None:
    """Clears output"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    
@dataclass
class Game:
    """Bundle of data for game"""
    title: str
    word: str
    guessed_letters: list[str]
    max_guesses: int
    incorrect_guesses: int = 0

    def hidden_word(self) -> str:
        return "".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
    
    def make_guess(self, guess: str) -> None:
        """Add a guess to the guesses list"""
        if guess in self.guessed_letters:
            raise ValueError("You already guessed that!")
        self.guessed_letters.append(guess)
        if guess not in self.word:
            self.incorrect_guesses += 1

    def is_won(self) -> bool:
        return self.hidden_word() == self.word

    def print_title(self):
        print(f"{self.title.upper()}")
        print("="*len(self.title))

    def print_ui(self) -> None:
        """Print the User Interface for the game"""
        clear()
        self.print_title()
        print()
        print("Can you guess the word?")
        print()
        print(self.hidden_word())
        print()
        print(f"Guesses: {', '.join(self.guessed_letters)}")
        print(f"{self.incorrect_guesses}/{self.max_guesses} incorrect")

def main() -> None:
    # 1. Initialize game
    settings = load_settings(Path("./settings.toml"))
    game = Game(
        title="Wurdle",
        word=rand_word(settings.word_list),
        guessed_letters=list(),
        max_guesses=settings.max_guesses,
    )
    game.print_ui()
    # 2. Play game
    while game.incorrect_guesses < game.max_guesses:
        try:
            guess = input("Letter: ")
            validate_guess(guess)
            game.make_guess(guess)
        except ValueError as err:
            print(err)
            continue
        if game.is_won():
            game.print_ui()
            print("You got it! :)")
            break
        game.print_ui()
    if not game.is_won():
        print("Better luck next time!")
        print(f"The word was '{game.word}'")

if __name__ == "__main__":
    main()
