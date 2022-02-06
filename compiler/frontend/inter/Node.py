
from compiler.frontend.lexer.Lexer import Lexer
from compiler.error.CompilerError import CompilerError


class Node:

    labels = 0

    def __str__(self):
        return "Node: [lex_line = " + str(self.lex_line) + "]"

    def __init__(self):
        self.lex_line = Lexer.line

    def error(self, message):
        raise CompilerError("near line " +
                            str(self.lex_line) +
                            ": " + message)

    @classmethod
    def new_label(cls):
        cls.labels = cls.labels + 1
        return cls.labels

    @classmethod
    def emit_label(cls, i):
        print("L" + str(i) + ":", end=" ")

    @classmethod
    def emit(cls, message):
        print("\t" + message)

