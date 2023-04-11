"""word

A guessing game for words
"""
import random
from pathlib import Path
from dataclasses import dataclass
import tomllib
import utils

@dataclass
class Settings:
    max_guesses: int
    word_list: Path

def load_settings(config_file: Path) -> Settings:
    with open(config_file, mode="rb") as file:
        settings = tomllib.load(file)
    return Settings(
        max_guesses=settings["max_guesses"], 
        word_list=Path(settings["word_list"]),
    )
    
def rand_word(words_path: Path) -> str:
    """Select a random word from a text file with words"""
    with open(words_path, mode="r", encoding="utf-8") as file:
        words = file.readlines()
    return utils.strip_newline(random.choice(words))

def validate_guess(guess: str) -> None:
    if len(guess) > 1:
        raise ValueError("Guess a single letter!")
    if not guess.isalpha():
        raise ValueError("The guess should be a letter!")
    
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
    
    def is_over(self) -> bool:
        return self.incorrect_guesses >= self.max_guesses

    def draw(self) -> None:
        """Print the User Interface for the game"""
        utils.clear_screen()
        print(utils.fmt_title(self.title.upper()))
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
        title="gword",
        word=rand_word(settings.word_list),
        guessed_letters=list(),
        max_guesses=settings.max_guesses,
    )
    game.draw()
    # 2. Play game
    while not (game.is_won() or game.is_over()):
        try:
            guess = input("Letter: ")
            validate_guess(guess)
            game.make_guess(guess)
        except ValueError as err:
            print(err)
            continue
        game.draw()
    # 3. Display results after game over
    if game.is_won():
        game.draw()
        print("You got it! :)")
    else:
        print("Better luck next time!")
        print(f"The word was '{game.word}'")

if __name__ == "__main__":
    main()
