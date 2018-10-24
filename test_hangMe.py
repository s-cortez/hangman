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
        realWord = "cat"
        displayWord = "_ a _"
        guess = "c"

        self.assertEqual("c _ _",
                         updateDisplayWord(guess, realWord, displayWord))

    def test_failsOnUnequalLengthWords(self):
        # Fail if pass in "cat" with "_ _ _ _ _"
        try:
            updateDisplayWord("c", "cat", "_ _ _ ")
        except ValueError:
            pass

        try:
            updateDisplayWord("c", "cat", "_ _ _ _ _")
        except ValueError:
            pass

    def test_updatesWordsWithMultipleOfSameChar(self):
        realWord = "noodle"
        displayWord = "_ _ _ _ _ _"
        guess = "o"

        self.assertEqual("_ o o _ _ _",
                         updateDisplayWord(guess, realWord, displayWord))
