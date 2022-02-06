from compiler.frontend.inter.Expr import Expr
from compiler.frontend.lexer.Num import Num
from compiler.frontend.symbols.Type import Type
from compiler.frontend.lexer.Word import Word


class Constant(Expr):

    def __str__(self):
        return super().__str__()

    def __init__(self, token_c, type_c):
        super().__init__(token_c, type_c)

    @classmethod
    def int(cls, value_c):
        return cls(Num(value_c), Type.Int)

    def __eq__(self, other):
        return super().__eq__(other)

    def jumping(self, t_label, f_label):
        if (self == Constant.TRUE) and (t_label is not 0):
            self.emit("goto L" + str(t_label))
        elif (self == Constant.FALSE) and (f_label is not 0):
            self.emit("goto L" + str(f_label))


Constant.TRUE = Constant(Word.TRUE, Type.Bool)
Constant.FALSE = Constant(Word.FALSE, Type.Bool)
