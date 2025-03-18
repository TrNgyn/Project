import nltk 
from nltk.corpus import words 
import random  

def game_instruction():
    print("""Welcome to Wordle!
    The goal of the game is to guess a 5-letter word.
    You have 6 attempts to guess the word.
    After each guess, you will receive feedback on your guess.
    The feedback consists of the following symbols:
    - '🟩' indicates a correct letter in the correct position
    - '🟨' indicates a correct letter in the wrong position
    - '⬜' indicates a letter that is not in the word""")

# Ensure that the NLTK words corpus is available
nltk.download('words')

# Get a list of all words in the NLTK words corpus
word_list = words.words()

# Create a word bank by filtering for words that have exactly 5 letters
word_bank = [word.lower() for word in word_list if len(word) == 5]

def play_game():
    """Main game loop for playing Wordle."""
    hidden_word = random.choice(word_bank)
    attempts = 6

    game_instruction()

    while attempts > 0:
        print('\nAttempts left:', attempts)
        guess = input('Guess a 5-letter word: ').lower()

        if len(guess) != 5 or not guess.isalpha():
            print('Please enter a valid 5-letter word.')
            continue

        # First layer: Check if the guessed word is correct
        if guess == hidden_word:
            print('\nCongratulations! You have guessed the word:', hidden_word)
            break
        
        # Second layer: Provide feedback
        feedback = []
        actual_list = list(hidden_word)  # Create a mutable list for tracking letters

        # First pass for correct positions (green)
        for i in range(len(guess)):
            if guess[i] == actual_list[i]:
                feedback.append('🟩')  # Correct letter and position
                actual_list[i] = None  # Mark as matched
            else:
                feedback.append(None)  # Placeholder for feedback

        # Second pass for correct letters in wrong positions (yellow)
        for i in range(len(guess)):
            if feedback[i] is None and guess[i] in actual_list:
                feedback[i] = '🟨'  # Correct letter, wrong position
                actual_list[actual_list.index(guess[i])] = None  # Mark as matched

        # Fill in any remaining letters as not in the word
        for i in range(len(feedback)):
            if feedback[i] is None:
                feedback[i] = '⬜'  # Letter not in the word

        print('Feedback:', ''.join(feedback))  # Display the feedback
        attempts -= 1  # Decrement attempts after processing the guess

        # Check if the player has run out of attempts
        if attempts == 0:
            print('You have run out of attempts. The word was:', hidden_word)

# Start the game
play_game()
