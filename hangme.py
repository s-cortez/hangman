"""
Hangman
Author: Saby Cortez
"""
import random


def chooseWord():
    trys = 10
    words = "words/custom.txt"
    file = open(words)
    wordList = file.read().splitlines()
    word = random.choice(wordList)
    file.close()
    return word


def checkWord():
    word = chooseWord()
    trys = 7
    used = ""
    blank = "_ "
    length = blank * len(word)
    while trys > 0:
        print(length)
        print("You have", trys, "tries left")
        x = input("Pick a letter!")
        if len(x) >1:
            print("Maybe just put 1 letter plz")
        if x in used:
            print("Error! You've already used that letter silly!")
        elif x in word:
            new = word.count(x)
            print("ok cool theres", new, " ", x)
            used += x
            pos = word.find(x)
            lengthpos = 2*pos
            b = list(length)
            b[lengthpos] = x
            length = "".join(b)


        else:
            trys = trys-1
            print("oof sorry no ", x)
            used += x
        print("You've used: ", used)
    print("The word was:", word)
    return trys



