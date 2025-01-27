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

    #this set decreases in length as game is played
    hidden_letters = set(hidden_word)

    alphabet_letters = set(string.ascii_uppercase)
    
    #this set increases in length as game is played
    guessed_letters = set()

    lives = 6

    while len(hidden_letters) > 0 and lives > 0:
        sorted_guessed_letters = list(guessed_letters)
        sorted_guessed_letters.sort()
        
        if len(guessed_letters) > 0:
            print('guessed letters are', ' '.join(sorted_guessed_letters))

        if lives == 6:
            print(f'you have {lives} lives')

        displayed_characters = [letter if letter in guessed_letters else '-' for letter in hidden_word]
        print('word is', ' '.join(displayed_characters), '\n')

        guessed_letter = input('guess a letter: ').upper()
        
        #if user guesses valid letter for first time
        if guessed_letter in (alphabet_letters - guessed_letters):
            guessed_letters.add(guessed_letter)

            #if user guesses letter within the hidden word
            if guessed_letter in hidden_letters:
                hidden_letters.remove(guessed_letter)
            else:
                lives -= 1
                print(f'no {guessed_letter}, you now have {lives} lives')
        
        #if user guesses valid letter for second time and above
        elif guessed_letter in guessed_letters:
            print(f'you already guessed {guessed_letter}')

        else:
            print('invalid character')

    if lives == 0:
        print(f'you died, the word was {hidden_word}')
    else:
        print(f'well done, you solved for {hidden_word}')

#if __name__ == '__main__':
hangman()