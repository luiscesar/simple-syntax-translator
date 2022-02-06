import unittest

from tests.TestContext import *
from compiler.frontend.lexer.Word import Word
from compiler.frontend.lexer.Tag import Tag


class TagTest(unittest.TestCase):

    def test001_word_init_case1(self):
        print(test_separator)
        print("test001_word_init_case1: Begin")
        word = Word("if", Tag.IF)
        self.assertEqual(word, Word.IF)
        print("word = " + str(word))


if __name__ == '__main__':
    unittest.main()
