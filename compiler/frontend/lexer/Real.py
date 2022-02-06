
from compiler.frontend.lexer.Token import Token
from compiler.frontend.lexer.Tag import *


class Real(Token):

    def __str__(self):
        return str(self.value)

    def __init__(self, v):
        super().__init__(Tag.REAL)
        self.value = v

    # class method:
    @classmethod
    def MyClassMethod(klass):
        pass

    # static method:
    @staticmethod
    def MyStaticMethod():
        pass

