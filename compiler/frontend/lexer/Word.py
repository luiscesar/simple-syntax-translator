
from compiler.frontend.lexer.Token import Token
from compiler.frontend.lexer.Tag import *


class Word(Token):

    def __str__(self):
        return str(self.lexeme)

    def __init__(self, l, t):
        super().__init__(t)
        self.lexeme = l
        self.__pp = None

    def __eq__(self, other):
        result = isinstance(other, Word) and (self.lexeme == other.lexeme) and \
                 super().__eq__(other)
        return result

    @property
    def pp(self):
        return self.__pp

    @pp.setter
    def pp(self, value):
        self.__pp = value


Word.AND = Word("&&", Tag.AND)
Word.OR = Word("||", Tag.OR)
Word.EQ = Word("==", Tag.EQ)
Word.NE = Word("!=", Tag.NE)
Word.LE = Word("<=", Tag.LE)
Word.GE = Word(">=", Tag.GE)
Word.MINUS = Word("minus", Tag.MINUS)
Word.TRUE = Word("true", Tag.TRUE)
Word.FALSE = Word("false", Tag.FALSE)
Word.TEMP = Word("t", Tag.TEMP)
Word.IF = Word("if", Tag.IF)
Word.ELSE = Word("else", Tag.ELSE)
Word.WHILE = Word("while", Tag.WHILE)
Word.DO = Word("do", Tag.DO)
Word.BREAK = Word("break", Tag.BREAK)
