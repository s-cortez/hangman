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


def updateDisplayWord(guess: chr, realWord: str, currentDisplayWord: str) -> str:
    """
    Fills in the blanks of a masked word given a guess
    :param guess: the character to fill in
    :param realWord: string containing the full word
    :param currentDisplayWord: string containing all revealed guesses
    :return: updated display word
    """
    return ""


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
    while trys > 0:
        print(displayword)
        print("You have", trys, "tries left")
        x = input("Pick a letter!")
        if len(x) > 1:
            print("Maybe just put 1 letter plz")
        if x in used:
            print("Error! You've already used that letter silly!")
        elif x in realword:
            new = realword.count(x)
            print("ok cool theres", new, " ", x)
            used += x
            pos = realword.find(x)
            lengthpos = 2 * pos
            b = list(displayword)
            b[lengthpos] = x
            displayword = "".join(b)


        else:
            trys = trys - 1
            print("oof sorry no ", x)
            used += x
        print("You've used: ", used)
    print("The word was:", realword)
