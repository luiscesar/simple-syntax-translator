
from compiler.frontend.lexer.Token import Token
from compiler.frontend.lexer.Tag import Tag


class Num(Token):

    def __str__(self):
        return str(self.value)

    def __init__(self, v):
        super().__init__(Tag.NUM)
        self.value = v


