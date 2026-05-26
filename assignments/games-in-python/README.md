
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game in Python that lets a player guess letters to reveal a hidden word before running out of attempts. This assignment practices string manipulation, control flow, list handling, and user input.

## 📝 Tasks

### 🛠️ Implement the Game Mechanics

#### Description
Create a playable Hangman game with the core loop that prompts the player for letter guesses, updates the displayed progress, and tracks remaining attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list (or from `data.csv` if provided).
- Display the current word progress using underscores for unknown letters (e.g. `_ a _ _ m a n`).
- Accept single-letter guesses and ignore repeated guesses.
- Track and display remaining incorrect attempts.
- End the game with a win message if the word is guessed, or a lose message showing the correct word if attempts run out.

### 🛠️ Optional Enhancements

#### Description
Add at least one enhancement to improve the game experience or code quality.

#### Requirements

- Add difficulty levels that adjust the number of allowed incorrect guesses.
- Or: load the word list from `data.csv` and filter by word length.
- Or: implement a simple ASCII-art hangman that progresses on wrong guesses.

## Skills Practiced

- String manipulation
- Loops and conditionals
- Random selection and list handling
- Basic file I/O (optional)

## Starter code

See `starter-code.py` for a minimal scaffold you can extend.

