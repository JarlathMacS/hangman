# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
import random
import string
from simple_term_menu import TerminalMenu
from colorama import Fore, Back, Style
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

        #os.system('cls' if os.name == 'nt' else 'clear')

        guessed_letters_list = list(guessed_letters)
        guessed_letters_list.sort()
        
        #only print '6 lives' at start of game
        #if lives == 6 and len(guessed_letters) == 0:
            #os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
        {Fore.RED}{Back.WHITE}You have {lives} lives{Style.RESET_ALL}
        \n\n''')

        #user has made a guess
        if len(guessed_letters) > 0:
            print(f'''Guessed letters are {Fore.YELLOW}{' '.join(guessed_letters_list)}{Fore.WHITE}\n\n''')

        displayed_characters = [letter if letter in guessed_letters else '_' for letter in hidden_word]
        print(f'''Word is {Fore.GREEN}{' '.join(displayed_characters)}{Fore.WHITE}\n\n''')

        guessed_letter = input('Guess a letter: ').upper()
        
        #validation of input conditional statement start
        #if user enters a valid, single letter, for the first time
        if guessed_letter in (alphabet_letters - guessed_letters):
            guessed_letters.add(guessed_letter)

            #if users' guess is a letter within the hidden word
            if guessed_letter in hidden_letters:
                os.system('cls' if os.name == 'nt' else 'clear')
                hidden_letters.remove(guessed_letter)
            else:
                lives -= 1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'''{Fore.RED}No {guessed_letter}{Style.RESET_ALL}\n\n''')    #, you now have {lives} lives')   #2 e's for correct guesses?
        
        #if user enters a valid, single letter, for the second time or more
        elif guessed_letter in guessed_letters:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''{Fore.BLUE}{Back.WHITE}You already guessed {guessed_letter}{Style.RESET_ALL}\n\n''')

        #if user enters any invalid letter/s, or any other keyboard input/s, at any time
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''{Fore.RED}Invalid character{Style.RESET_ALL}\n\n''')  #{Fore.WHITE}{Back.BLACK}

    #user either depleted the hidden letters, or they depleted their lives
    if lives == 0:
        #print(f'No {guessed_letter}')
        print(f'''{Fore.RED}{Back.WHITE}You have {lives} lives, you died{Style.RESET_ALL}\n\n''')
        print(f'''Guessed letters were {Fore.YELLOW}{' '.join(guessed_letters_list)}{Style.RESET_ALL}\n\n''')
        print(f'''Word was {Fore.GREEN}{' '.join(displayed_characters)}{Fore.WHITE}\n\n''')
        print(f'''Solution was {Fore.GREEN}{Back.WHITE}{hidden_word}{Style.RESET_ALL}''')
        #print(f'You died, the word was {hidden_word}')
    else:
        print(f'''{Fore.RED}{Back.WHITE}You have {lives} lives{Style.RESET_ALL}\n\n''')
        print(f'''Guessed letters were {Fore.YELLOW}{' '.join(guessed_letters_list)}{Style.RESET_ALL}\n\n''')
        print(f'''Word was {Fore.GREEN}{' '.join(displayed_characters)}{Fore.WHITE}\n\n''')
        print(f'''{Fore.GREEN}{Back.WHITE}Well done, you solved for {hidden_word}{Style.RESET_ALL}''')

def display_rules():
    print(f'''
    {Fore.YELLOW}[1] {Fore.BLUE}You get six (6) lives
    {Fore.YELLOW}[2] {Fore.BLUE}Invalid entries don\'t count towards your lives
    {Fore.YELLOW}[3] {Fore.BLUE}Repeated guesses don\'t count towards your lives
    {Fore.YELLOW}[4] {Fore.BLUE}There are no spaces ( ) or hyphens (-) in the words
    {Fore.YELLOW}[5] {Fore.BLUE}Have fun!
    ''')

def main():
    """
    main function
    clears terminal and calls hangman function
    """

    os.system('cls' if os.name == 'nt' else 'clear')

    #Show welcome message
    print(f'''
    {Fore.CYAN}Welcome to my Hangman game!{Style.RESET_ALL}
    ''')

    options = ['[1] Play game', '[2] Show rules', '[3] Exit']
    terminal_menu = TerminalMenu(options, title = 'Options')

    end = False
    while end == False:
        menu_entry_index = terminal_menu.show()
        options_choice = options[menu_entry_index]

        if (options_choice == '[3] Exit'):
            #message here
            end = True
        elif (options_choice == '[2] Show rules'):
            display_rules()
        else:
            hangman()

    #menu_entry_index = terminal_menu.show()
    #print(f'You have selected {options[menu_entry_index]}!')

    #hangman()

if __name__ == "__main__":
    main()