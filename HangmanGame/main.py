
import random

words = ['geology', 'hamburger', 'pizza', 'science', 'youtube', 'bacon', 'poker', 'space']

# How to randomly choose a word from the list
chosen_word = random.choice(words)
# Create a list of underscores for the word
word_display = ['_' for _ in chosen_word]
# Number of attempts
attempts = 8

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input ("Guess a letter: ").lower()
    # The '.lower()' makes everything a lowercase letter to match the list words
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            # So for enumerate of 'pizza' index of 0 is letter 'p', index of 1 is letter 'i'... etc.
            if letter == guess:
                word_display[index] = guess
    else:
        print("That letter is not in the word.")
        attempts -= 1

# Gamne conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost!")
