from compiler.frontend.inter.Op import Op
from compiler.frontend.symbols.Type import Type

class Unary(Op):

    def __str__(self):
        return str(self.op) + " " + str(self.expr)

    def __init__(self, token_c, expr_c):
        super().__init__(token_c, None)
        self.expr = expr_c
        self.type = Type.max(Type.Int, self.expr.type)
        if self.type is None:
            self.error("Type error")

    def gen(self):
        return Unary(self.op, self.expr.reduce())

