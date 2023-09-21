import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Select a random word from the list
selected_word = random.choice(word_list)

# Initialize variables
guesses = ""
max_attempts = 6

# Function to display the current state of the word with underscores for hidden letters
def display_word(word, guesses):
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "_"
    return display

# Main game loop
print("Welcome to Hangman!")
while max_attempts > 0:
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
        print(f"Wrong guess! You have {max_attempts} attempts left.")

if max_attempts == 0:
    print(f"Sorry, you're out of attempts. The word was {selected_word}. Better luck next time!")
