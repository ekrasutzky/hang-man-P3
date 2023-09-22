import random

"""List of words for the game"""
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

""" ASCII art for hangman """
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

"""Function to select a random word from the list"""
def select_word():
    return random.choice(word_list)

""" Function to display the current state of the word with underscores for hidden letters"""
def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display

""" Function to play the Hangman game"""
def play_hangman():
    selected_word = select_word()
    guesses = ""
    max_attempts = 6
    hangman_stage = 0

    print("Welcome to Hangman!")

    while max_attempts > 0:
        print(hangman_stages[hangman_stage])
        print(display_word(selected_word, guesses))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in selected_word:
            guesses += guess
            if display_word(selected_word, guesses) == selected_word:
                print(f"Congratulations! You guessed the word: {selected_word}")
                break
        else:
            max_attempts -= 1
            hangman_stage += 1
            print(f"Wrong guess! You have {max_attempts} attempts left.")

    if max_attempts == 0:
        print(f"Sorry, you're out of attempts. The word was {selected_word}.")

""" Main loop for restarting the game """
while True:
    play_hangman()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing Hangman!")
