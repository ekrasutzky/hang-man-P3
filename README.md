# HANGMAN 

 The Hangman Game is a classic word-guessing game implemented in Python. In this game, the player's objective is to guess a hidden word by suggesting letters one at a time. The game provides a visual representation of a hangman figure that evolves with each incorrect guess, adding an element of suspense and challenge.
 ## How to play
 - The game selects a word, and the player starts with a blank word with underscores representing each letter.

- The player guesses a letter by entering it via the keyboard.

- If the guessed letter is in the word, it is revealed in the word display; otherwise, the hangman figure evolves.

- The player continues guessing until they either correctly guess the word or run out of attempts.

- After the game ends (win or lose), the player can choose to restart and play again.

## Features
- Word Selection: The game randomly selects a word from a predefined list or dictionary. Players must guess this word letter by letter.

- Visual Feedback: The game displays an ASCII art hangman figure that progressively appears as the player makes incorrect guesses. This adds an exciting visual element to the game.

- User Input Validation: The game validates user input to ensure it's a single letter. If the input is invalid, the game prompts the player to try again.

- Word Display: The game displays the word with underscores for unguessed letters and reveals correct guesses. This provides players with feedback on their progress.

- Attempts Limit: The player has a limited number of attempts to guess the word correctly. If they exceed this limit, they lose the game.

- Restart Option: After winning or losing a game, the player has the option to restart and play again, providing endless entertainment.

- Colorama: I installed colorama in order to give the game color features to pop up the wrong answers, or any other prompt. 

## Testing
### Bugs
### Remaining bugs
### Validator testing

## Deployment
The project was deployed using Code Institute's mock terminal for Heroku

- Steps for deployment: 
  - Fork or clone this repository
  - Create a new Heroku app 
  - Set the buildpacks to `python` and `node.js` (in that order)
  - Link the Heroku app to the repository
  - Click on Deploy

# Credits
- Code Institute for the deployment terminal.