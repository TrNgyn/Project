import nltk 
from nltk.corpus import words 
import random  

# Get a list of all words in the NLTK words corpus
word_list = words.words()

# Create a word bank by filtering for words that have exactly 5 letters
word_bank = [word for word in word_list if len(word) == 5]

# Randomly select a word from the word bank to be guessed
word = random.choice(word_bank)

# Initialize the guessed word with underscores for each letter in the selected word
guessed_word = '_' * len(word)

# Set the number of attempts the player has to guess the word
attempts = 10

# Start the guessing loop that continues until attempts are exhausted
while attempts > 0:
    print('\nCurrent word:', guessed_word)  # Show the current state of the guessed word
    guess = input('Guess a letter: ').lower()  # Prompt the user for a letter and convert it to lowercase

    # Check if the input is a valid single letter
    if len(guess) != 1 or not guess.isalpha():
        print('Please enter a single letter.')  # Inform the user of invalid input
        continue  

    # Check if the guessed letter is in the selected word
    if guess in word:
        # If the guess is correct, update the guessed_word
        for i in range(len(word)):
            if word[i] == guess:
                print('\nGreat guess!')  # Inform the user of a successful guess
                guessed_word = guessed_word[:i] + guess + guessed_word[i + 1:]  # Update the guessed word
                print('Current word:', guessed_word)  # Show the updated guessed word

        attempts -= 1  # Decrement attempts only once for correct guess
        print('You have', attempts, 'attempts left.')  # Show remaining attempts
    else:
        attempts -= 1  # Decrement attempts for a wrong guess
        print('\nWrong guess! You have', attempts, 'attempts left.')  # Inform the user of a wrong guess

    # Check if the word has been completely guessed
    if '_' not in guessed_word:
        print('\nCongratulations! You have guessed the word:', guessed_word)  # Success message
        break  # Exit the loop

    # Check if the player has run out of attempts
    if attempts == 0:
        print('You have run out of attempts. The word was:', word)  # Inform the user of game over
