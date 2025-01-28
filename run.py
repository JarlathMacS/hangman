# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
import random
import string
from words import words

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

    #hidden letters remain to be guessed, and user still alive
    while len(hidden_letters) > 0 and lives > 0:
        guessed_letters_list = list(guessed_letters)
        guessed_letters_list.sort()
        
        #only print '6 lives' at start of game
        if lives == 6 and len(guessed_letters) == 0:
            print(f'you have {lives} lives')

        #user has made a guess
        if len(guessed_letters) > 0:
            print('guessed letters are', ' '.join(guessed_letters_list))

        displayed_characters = [letter if letter in guessed_letters else '-' for letter in hidden_word]
        print('word is', ' '.join(displayed_characters), '\n')

        guessed_letter = input('guess a letter: ').upper()
        
        #validation of input conditional statement start
        #if user enters a valid, single letter, for the first time
        if guessed_letter in (alphabet_letters - guessed_letters):
            guessed_letters.add(guessed_letter)

            #if users' guess is a letter within the hidden word
            if guessed_letter in hidden_letters:
                hidden_letters.remove(guessed_letter)
            else:
                lives -= 1
                print(f'no {guessed_letter}, you now have {lives} lives')   #2 e's for correct guesses?
        
        #if user enters a valid, single letter, for the second time or more
        elif guessed_letter in guessed_letters:
            print(f'you already guessed {guessed_letter}')

        #if user enters any invalid letter/s, or any other keyboard input/s, at any time
        else:
            print('invalid character')

    #user either depleted the hidden letters, or they depleted their lives
    if lives == 0:
        print(f'you died, the word was {hidden_word}')
    else:
        print(f'well done, you solved for {hidden_word}')

def main():
    """
    main function
    clears terminal and calls hangman function
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    hangman()

main()

#if __name__ == '__main__':