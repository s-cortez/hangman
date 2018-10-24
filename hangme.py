"""
Hangman
Author: Saby Cortez
"""
import random


def chooseWord():
    """
    Returns a random word from words/custom.txt
    :return: random word as a string
    """
    words = "words/custom.txt"
    file = open(words)
    wordlist = file.read().splitlines()
    word = random.choice(wordlist)
    file.close()
    return word


def updateDisplayWord(guess: chr, realword: str, currentdisplayword: str) -> str:
    """
    Fills in the blanks of a masked word given a guess
    :param guess: the character to fill in
    :param realword: string containing the full word
    :param currentdisplayword: string containing all revealed guesses
    :return: updated display word
    """
    pos = realword.find(guess)
    lengthpos = 2 * pos
    b = list(currentdisplayword)
    b[lengthpos] = guess
    return "".join(b)


def main():
    """
    User interface for hangman game
    :return: None
    """

    # Initialize variables
    realword = chooseWord()
    trys = 7
    used = []
    displayword = ("_ " * len(realword)).strip()

    # Main game
    while trys > 0 or displayword.replace(" ", "") == realword:
        print(displayword)
        print("You have {} tries left".format(trys))
        guess = input("Pick a letter!")
        if len(guess) != 1:
            print("Maybe just put 1 letter plz")
        elif guess in used:
            print("Error! You've already used that letter silly!")
        elif guess in realword:
            # Says how many there are in the word
            print("ok cool theres {} {}"
                  .format(realword.count(guess), guess))

            # Adds letter to used pile
            used += guess

            # Updates display word
            displayword = updateDisplayWord(guess, realword, displayword)
        else:
            trys -= 1
            used.append(guess)
            print("oof sorry no ", guess)
        print("You've used: ", used)
    print("The word was:", realword)
