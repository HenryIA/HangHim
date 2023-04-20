# Hangman Game
This is a simple implementation of the classic word guessing game, Hangman, in Python.

# Description
The game randomly selects a word from a pre-defined list of words, and the player must guess the word by suggesting letters within a limited number of guesses. For each incorrect guess, a part of a stick figure is drawn, with the game ending if the entire stick figure is drawn or the player successfully guesses the word.

# Requirements
Python 3.5 or higher
# Usage
To play the game, simply run the hangman.py file in your Python environment:

```bash
python hangman.py
```
The game will then prompt the player to guess a letter until the player guesses the word correctly or runs out of guesses.

# Customization
You can customize the game by modifying the words list in the hangman.py file to include your own list of words to guess.

```python
words = ['apple', 'banana', 'orange', 'kiwi', 'strawberry', 'grape']
```
You can also modify the MAX_GUESSES constant to set the maximum number of incorrect guesses before the game ends.

```python
MAX_GUESSES = 6
```
# Contributing
This project is open for contributions. If you have any suggestions or improvements, feel free to submit a pull request or open an issue.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
