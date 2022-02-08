import unittest


from tests.TestContext import *
from compiler.frontend.lexer.Lexer import Lexer
from compiler.frontend.lexer.Word import Word
from compiler.error.CompilerError import CompilerError


class LexerTest(unittest.TestCase):

    def test001_lexer_init_case1(self):
        print(test_separator)
        print("test001_lexer_init_case1: Begin")
        file_name = r"tests\resources\TestSource.txt"
        lexer = Lexer(file_name)
        self.assertTrue(lexer is not None)
        print("lexer = " + str(lexer))

    def test002_lexer_words_case1(self):
        print(test_separator)
        print("test002_lexer_words_case1: Begin")
        file_name = r"tests\resources\TestSource.txt"
        lexer = Lexer(file_name)
        if_word = lexer.words[Word.IF.lexeme]
        print(if_word)
        print("if_word.tag = " + str(if_word.tag))
        self.assertEqual(if_word, Word.IF)

    def test003_lexer_readch_case1(self):
        print(test_separator)
        print("test003_lexer_readch_case1: Begin")
        file_name = r"tests\resources\TestSource.txt"
        lexer = Lexer(file_name)
        lexer.readch()
        #self.assertTrue(lexer.peek == '{')
        print("lexer.peek = " + str(lexer.peek))

    def test004_lexer_readch_next_case1(self):
        print(test_separator)
        print("test004_lexer_readch_next_case1: Begin")
        file_name = r"tests\resources\TestSource.txt"
        lexer = Lexer(file_name)
        is_correct = lexer.readch_next('{')
        print("is_correct = " + str(is_correct))
        print("lexer.peek = " + str(lexer.peek))
        self.assertTrue(is_correct)

    def test005_lexer_scan_case1(self):
        print(test_separator)
        print("test005_lexer_scan_case1: Begin")
        file_name = r"tests\resources\TestSource.txt"
        lexer = Lexer(file_name)
        try:
            token = lexer.scan()
            print("token = " + str(token))
            print("peek = " + lexer.peek)
        except CompilerError as err:
            print(str(err))
            self.fail(str(err))
        except Exception as err:
            self.fail(str(err))

    def test006_lexer_scan_case2(self):
        print(test_separator)
        print("test006_lexer_scan_case2: Begin")
        file_name = r"tests\resources\TestSource.txt"
        lexer = Lexer(file_name)
        try:
            token = lexer.scan()
            print("token = " + str(token))
            print("peek = " + lexer.peek)
        except CompilerError as err:
            print(str(err))
            self.fail(str(err))
        except Exception as err:
            self.fail(str(err))

    def test007_lexer_scan_case3(self):
        print(test_separator)
        print("test007_lexer_scan_case3: Begin")
        file_name = r"tests\resources\TestSource.txt"
        lexer = Lexer(file_name)
        try:
            while True:
                token = lexer.scan()
                print("token = " + str(token))
                print("lexer.line = " + str(lexer.line))
                #print("peek = [" + lexer.peek + "]")
                if token is None:
                    break
        except CompilerError as err:
            print(str(err))
            self.fail(str(err))
        except Exception as err:
            self.fail(str(err))


if __name__ == '__main__':
    unittest.main()
