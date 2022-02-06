from compiler.frontend.inter.Expr import Expr
from compiler.frontend.inter.Temp import Temp


class Op(Expr):

    def __init__(self, token_c, type_c):
        super().__init__(token_c, type_c)

    def reduce(self):
        x = self.gen()
        t = Temp(self.type)
        self.emit(str(t) + " = " + str(x))
        return t
