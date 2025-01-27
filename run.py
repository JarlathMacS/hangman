# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
from words import words
import string

def get_valid_word(words):
    """chooses a word at random from the list"""
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():

    hidden_word = get_valid_word(words)
    hidden_letters = set(hidden_word)

    alphabet_letters = set(string.ascii_uppercase)

    guessed_letters = set()

    while len(hidden_letters) > 0:
        sorted_guessed_letters = list(guessed_letters)
        sorted_guessed_letters.sort()
        
        print('guessed letters are', ' '.join(sorted_guessed_letters)) #need to alphabetize this list

        displayed_characters = [letter if letter in guessed_letters else '-' for letter in hidden_word]
        print('current word is', ' '.join(displayed_characters), '\n')

        guessed_letter = input('guess (enter) a letter: ').upper()

        if guessed_letter in (alphabet_letters - guessed_letters):
            guessed_letters.add(guessed_letter)

            if guessed_letter in hidden_letters:
                hidden_letters.remove(guessed_letter)
        
        elif guessed_letter in guessed_letters:
            print(f'you already guessed {guessed_letter}')

        else:
            print('invalid character')

    print(f'well done, you solved for {hidden_word}')

#if __name__ == '__main__':
hangman()