from unittest import TestCase
from hangme import *


class TestChooseWord(TestCase):
    def test_checkWordIsFromFile(self):
        words = "words/custom.txt"
        file = open(words)
        wordlist = file.read().splitlines()
        file.close()
        self.assertTrue(chooseWord() in wordlist)


class TestUpdateDisplayWord(TestCase):
    def test_updatesWithBlankDisplayWord(self):
        realWord = "cat"
        displayWord = "_ _ _"
        guess = "c"

        self.assertEqual("c _ _",
                         updateDisplayWord(guess, realWord, displayWord))

    def test_updatesWithNonBlankDisplayWord(self):
        self.fail()

    def test_failsOnUnequalLengthWords(self):
        # Fail if pass in "cat" with "_ _ _ _ _"
        self.fail()
