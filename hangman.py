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

    guessed_letter = input('guess a letter: ').upper()

    if guessed_letter in (alphabet_letters - guessed_letters):
        guessed_letters.add(guessed_letter)

        if guessed_letter in hidden_letters:
            hidden_letters.remove(guessed_letter)
    
    elif guessed_letter in guessed_letters:
        print(f'you already guessed {guessed_letter}')

    else:
        print('invalid character')
