"""hangman"""

from random import randrange

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME) as f:
        word_list = ''.join(f.readlines()).split()
    print("  ", len(word_list), "words loaded.")
    print('Enter play_hangman() to play a game of hangman!')
    return word_list


# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word = words_dict[randrange(0, len(words_dict))]
    return word


# end of helper code
# -----------------------------------


# CONSTANTS
# TODO 1a: Create a constant MAX_GUESSES = 6

# GLOBAL VARIABLES
# TODO 1b: Create a variable secret_word set to 'claptrap'
# TODO 1c: Create an empty list letters_guessed


# From part 3b:
def word_guessed():
    """Returns True if the player has successfully guessed the word, and False otherwise."""
    global secret_word
    global letters_guessed

    # TODO 3 Implement the word_guessed function
    pass


def print_guessed():
    """Prints out the characters you have guessed in the secret word so far."""
    global secret_word
    global letters_guessed

    # TODO 4 Implement the print_guessed function
    pass


def play_hangman():
    """Actually play the hangman game"""
    global secret_word
    global letters_guessed

    # Put the mistakes_made variable here, since you'll only use it in this function
    # TODO 1d create a local variable mistakes_made initialized to 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    # TODO 5 Implement the hangman game
    return None
