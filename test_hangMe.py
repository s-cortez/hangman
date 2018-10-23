from unittest import TestCase
from hangme import *


class TestCheckWord(TestCase):
    def test_checkWord(self):
        self.fail()


class TestChooseWord(TestCase):
    def test_checkWordIsFromFile(self):
        words = "words/custom.txt"
        file = open(words)
        wordList = file.read().splitlines()
        file.close()
        self.assertTrue(chooseWord() in wordList)
