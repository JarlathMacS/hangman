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

        guessed_letters_list = list(guessed_letters)
        guessed_letters_list.sort()
        
        print(f'''
{Fore.RED}{Back.WHITE}You have {lives} lives remaining{Style.RESET_ALL}
        ''')

        #user has made a guess
        if len(guessed_letters) > 0:
            print(f'''
You guessed the letters {Fore.YELLOW}{' '.join(guessed_letters_list)}
            {Style.RESET_ALL}
            ''')

        displayed_characters = [letter if letter in guessed_letters 
        else '_' for letter in hidden_word]

        print(f'''
The word is {Fore.GREEN}{' '.join(displayed_characters)}{Style.RESET_ALL}
        ''')

        guessed_letter = input('Guess a letter: ').upper()
        
        #validation of input conditional statement start
        #if user enters a valid, single letter, for the first time
        if guessed_letter in (alphabet_letters - guessed_letters):
            guessed_letters.add(guessed_letter)

            #if users' guess is a letter within the hidden word
            if guessed_letter in hidden_letters:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'''
{Fore.GREEN}Yes, there's {hidden_word.count(guessed_letter)} letter
                {guessed_letter} in the word{Style.RESET_ALL}
                ''')
                hidden_letters.remove(guessed_letter)
            else:
                lives -= 1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'''
{Fore.RED}Sorry, there's no letter {guessed_letter} in the word
                {Style.RESET_ALL}\
                ''')
        
        #if user enters a valid, single letter, for the second time or more
        elif guessed_letter in guessed_letters:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''
{Fore.BLUE}{Back.WHITE}You have already guessed letter {guessed_letter}
            {Style.RESET_ALL}
            ''')

        #if user enters any invalid letter/s, or any other keyboard input/s, 
        # at any time
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''
{Fore.RED}You have guessed an invalid character.  Only letters A to Z are valid
            ''')

    #user either depleted the hidden letters, or they depleted their lives
    if lives == 0:
        print(f'''
{Fore.RED}{Back.WHITE}Sorry, you had {lives} lives remaining, so you died
        {Style.RESET_ALL}
You guessed the letters {Fore.YELLOW}{' '.join(guessed_letters_list)}
        {Style.RESET_ALL}
The word was {Fore.GREEN}{' '.join(displayed_characters)}{Style.RESET_ALL}
The answer was {Fore.GREEN}{Back.WHITE}{hidden_word}{Style.RESET_ALL}
        ''')
    else:
        print(f'''
{Fore.RED}{Back.WHITE}You still had {lives} lives remaining{Style.RESET_ALL}
You guessed the letters {Fore.YELLOW}{' '.join(guessed_letters_list)}
        {Style.RESET_ALL}
The word was {Fore.GREEN}{' '.join(displayed_characters)}
{Back.WHITE}Well done, you correctly answered {hidden_word}{Style.RESET_ALL}
        ''')


def display_rules():
    print(f'''
{Fore.YELLOW}[1] {Fore.CYAN}The aim of this classic game is to guess the
hidden word before you lose all your lives
{Fore.YELLOW}[2] {Fore.CYAN}You get six (6) lives at the start of the game
{Fore.YELLOW}[3] {Fore.CYAN}Only the 26 alphabet letters (A to Z) are valid
guesses
{Fore.YELLOW}[4] {Fore.CYAN}You may only guess a single letter at a time
{Fore.YELLOW}[5] {Fore.CYAN}Invalid guesses don't count towards your lives
{Fore.YELLOW}[6] {Fore.CYAN}Repeated guesses don't count towards your lives
{Fore.YELLOW}[7] {Fore.CYAN}The hidden words are chosen at random by the
computer
{Fore.YELLOW}[8] {Fore.CYAN}There are no spaces ( ) or hyphens (-) in the
hidden words
{Fore.YELLOW}[9] {Fore.CYAN}Have fun!{Style.RESET_ALL}
    ''')


def main():
    """
    main function
    clears the terminal and calls the hangman and/or display_rules functions,
    or exits the program
    """

    os.system('cls' if os.name == 'nt' else 'clear')

    #Show welcome message
    print(f'''
{Fore.MAGENTA}
Welcome to my Hangman game!
    ''')

    options = ['[1] Play game', '[2] Show rules', '[3] Exit']
    terminal_menu = TerminalMenu(options, title = 'Options')

    end = False
    while end == False:
        menu_entry_index = terminal_menu.show()
        options_choice = options[menu_entry_index]

        if (options_choice == '[3] Exit'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''
            {Fore.MAGENTA}
Thank you for playing my Hangman game
            ''')
            end = True
        elif (options_choice == '[2] Show rules'):
            os.system('cls' if os.name == 'nt' else 'clear')
            display_rules()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            hangman()


if __name__ == "__main__":
    main()