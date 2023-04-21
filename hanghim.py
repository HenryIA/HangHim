import random

# Define a list of words to choose from
words = ["apple", "banana", "cherry", "orange", "kiwi", "strawberry"]

# Select a random word from the list
word = random.choice(words)

# Initialize variables
max_guesses = 6
num_guesses = 0
guessed_letters = []
correct_guesses = ["_" for _ in word]

# Print a welcome message
print("Welcome to Hangman! Can you guess the word?")

# Loop through the game until the player wins or loses
while num_guesses < max_guesses:
    # Print the current state of the word
    print(" ".join(correct_guesses))
    
    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()
    
    # Check if the player has already guessed the letter
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue
    
    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(guess)
    
    # Check if the letter is in the word
    if guess in word:
        # Update the state of the word to show the correct guesses
        for i in range(len(word)):
            if word[i] == guess:
                correct_guesses[i] = guess
        # Check if the player has guessed all the letters in the word
        if "_" not in correct_guesses:
            print("Congratulations, you guessed the word!")
            break
    else:
        # Increment the number of incorrect guesses and draw a part of the hangman
        num_guesses += 1
        print("Incorrect guess. You have", max_guesses - num_guesses, "guesses left.")
    # Print a blank line for spacing
    print()
    
# Check if the player lost the game
if num_guesses == max_guesses:
    print("Sorry, you ran out of guesses. The word was", word + ".")
