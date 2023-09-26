import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


WORD_LIST = ["apple", "banana", "cherry", "date", "grape", "kiwi", "lemon"]

"""
List of words for the game
"""

hangman_stages = [
    """
     ------
    |    |
         |
         |
         |
         |
    """,
    """
     ------
    |    |
    O    |
         |
         |
         |
    """,
    """
     ------
    |    |
    O    |
    |    |
         |
         |
    """,
    """
     ------
    |    |
    O    |
   /|    |
         |
         |
    """,
    """
     ------
    |    |
    O    |
   /|\\   |
         |
         |
    """,
    """
     ------
    |    |
    O    |
   /|\\   |
   /     |
         |
    """,
    """
     ------
    |    |
    O    |
   /|\\   |
   / \\   |
         |
    """
]

"""
ASCII art for hangman
"""


def select_word():
    return random.choice(WORD_LIST)


"""
Function to select a random word from the list
"""


def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display


"""
Function to display the current state of the
word with underscores for hidden letters
"""


def play_hangman():
    selected_word = select_word()
    guesses = ""
    max_attempts = 6
    hangman_stage = 0

    print(f"{Fore.MAGENTA}{Style.BRIGHT}Welcome to Hangman!")

    while max_attempts > 0:
        print(hangman_stages[hangman_stage])
        print(display_word(selected_word, guesses))
        guess = input(f"{Fore.MAGENTA}{Style.BRIGHT} Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(f"{Fore.YELLOW} Please enter a single letter.")
            continue

        if guess in selected_word:
            guesses += guess
            if display_word(selected_word, guesses) == selected_word:
                print(f"{Back.WHITE}{Fore.MAGENTA}Congratulations! You guessed the word: {Back.MAGENTA}{Fore.CYAN} {selected_word} ")
                break
        else:
            max_attempts -= 1
            hangman_stage += 1
            print(f"{Back.RED} {Style.BRIGHT} Wrong guess! You have {max_attempts} attempts left.")

    if max_attempts == 0:
        print(f"Sorry, you're out of attempts. The word was {Back.MAGENTA}{Fore.CYAN} {selected_word}.")


"""
Function to play the Hangman game
"""


if __name__ == '__main__':
    while True:
        play_hangman()
        play_again = input(f"{Fore.CYAN}{Style.BRIGHT} Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"{Fore.GREEN}{Style.BRIGHT}Thanks for playing Hangman!")

"""
Main loop for restarting the game
"""
