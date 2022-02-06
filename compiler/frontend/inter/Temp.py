from compiler.frontend.inter.Expr import Expr
from compiler.frontend.lexer.Word import Word


class Temp(Expr):
    count = 0

    def __str__(self):
        return "t" + str(self.number)

    def __init__(self, type_c):
        super().__init__(Word.TEMP, type_c)
        self.__class__.count = self.__class__.count + 1
        self.number = self.__class__.count



