"""
Hangman game implementation by Jarlath
4th February, 2025
"""
import os
import random
import string
from time import sleep
from simple_term_menu import TerminalMenu
from colorama import Fore, Back, Style
from words import words_list


def get_valid_word():
    """
    Chooses a word at random from the list
    """
    word = random.choice(words_list)

    while '-' in word or ' ' in word:
        word = random.choice(words_list)

    return word.upper()


def hangman():
    """
    This function contains the majority of the code which is executed, the
    conditional statements which run the game, and the prompts or answers which
    are output to the user via the terminal
    """
    hidden_word = get_valid_word()
    # This set decreases in length as game is played
    hidden_letters = set(hidden_word)

    alphabet_letters = set(string.ascii_uppercase)
    # This set increases in length as game is played
    guessed_letters = set()

    lives = 6
    # Hidden letters remain to be guessed, and user still alive
    while len(hidden_letters) > 0 and lives > 0:

        guessed_letters_list = list(guessed_letters)
        guessed_letters_list.sort()

        print(f'''
{Fore.RED}{Back.WHITE}You have {lives} lives remaining{Style.RESET_ALL}
        ''')

        # User has made a guess
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
        # Validation of input, conditional statement start
        # If user enters a valid, single letter, for the first time
        if guessed_letter in (alphabet_letters - guessed_letters):
            guessed_letters.add(guessed_letter)
            # If users' guess is a letter within the hidden word
            if guessed_letter in hidden_letters:
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'''\
                {Fore.GREEN}
Yes, there's {hidden_word.count(guessed_letter)} of letter {guessed_letter} in\
 the word{Style.RESET_ALL}
                ''')
                hidden_letters.remove(guessed_letter)
            else:
                lives -= 1
                sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'''
{Fore.RED}Sorry, there's no letter {guessed_letter} in the word\
{Style.RESET_ALL}
                ''')
        # If user enters a valid, single letter, for the second time or more
        elif guessed_letter in guessed_letters:
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''
{Fore.BLUE}You have already guessed letter {guessed_letter}.  You did not lose\
 a life for this guess{Style.RESET_ALL}
            ''')
        # If user enters any invalid letter/s, or any other keyboard input/s,
        # at any time
        else:
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''
{Fore.RED}You have guessed an invalid character.  Only letters A to Z are\
 valid, and\nonly one (1) letter at a time.  You did not lose a life for this\
 guess\
            ''')
    # User either depleted the hidden letters, or they depleted their lives
    if lives == 0:
        sleep(1)
        print(f'''
{Fore.RED}{Back.WHITE}Sorry, you had {lives} lives remaining, so you died
{Style.RESET_ALL}

You guessed the letters {Fore.YELLOW}{' '.join(guessed_letters_list)}
{Style.RESET_ALL}


The word was {Fore.GREEN}{' '.join(displayed_characters)}{Style.RESET_ALL}

The answer was {Fore.GREEN}{Back.WHITE}{hidden_word}{Style.RESET_ALL}
        ''')
    else:
        sleep(1)
        print(f'''
{Fore.RED}{Back.WHITE}You still had {lives} lives remaining{Style.RESET_ALL}


You guessed the letters {Fore.YELLOW}{' '.join(guessed_letters_list)}
{Style.RESET_ALL}


The word was {Fore.GREEN}{' '.join(displayed_characters)}

Well done, you correctly answered {Back.WHITE}{hidden_word}{Style.RESET_ALL}
        ''')


def display_rules():
    """
    This function displays the gameplay rules to the terminal
    """
    print(f'''
    {Fore.CYAN}
Hangman Rules:

{Fore.YELLOW}[1] {Fore.CYAN}The aim of this classic game is to guess the
hidden word before you lose all your lives
{Fore.YELLOW}[2] {Fore.CYAN}You get six (6) lives at the start of the game
{Fore.YELLOW}[3] {Fore.CYAN}Only the 26 alphabet letters (A to Z) are valid
guesses
{Fore.YELLOW}[4] {Fore.CYAN}You may only guess a single letter at a time
{Fore.YELLOW}[5] {Fore.CYAN}Invalid guesses don't count towards your lives
{Fore.YELLOW}[6] {Fore.CYAN}Repeated guesses don't count towards your lives
{Fore.YELLOW}[7] {Fore.CYAN}The hidden words are chosen at random by the
program
{Fore.YELLOW}[8] {Fore.CYAN}There are no spaces ( ) or hyphens (-) in the
hidden words
{Fore.YELLOW}[9] {Fore.CYAN}Have fun!{Style.RESET_ALL}
    ''')
    sleep(1)


def main():
    """
    Main function which clears the terminal, calls the hangman and/or
    display_rules functions, or exits the program
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    # Show a welcome message
    print(f'''
{Fore.MAGENTA}
Welcome to my Hangman game!
    ''')
    sleep(1)

    options = ['[1] Play game', '[2] Show rules', '[3] Exit']
    terminal_menu = TerminalMenu(options, title='Options')

    end = False
    while end is False:
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
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            display_rules()
        else:
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            hangman()
            sleep(1)


if __name__ == "__main__":
    main()
