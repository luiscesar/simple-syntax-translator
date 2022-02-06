from compiler.frontend.inter.Op import Op
from compiler.frontend.symbols.Type import Type


class Arith(Op):

    def __str__(self):
        return str(self.expr1) + " " + str(self.op) + " " + str(self.expr2)

    def __init__(self, token_c, expr1_c, expr2_c):
        super().__init__(token_c, None)
        self.expr1 = expr1_c
        self.expr2 = expr2_c
        self.type = Type.max(self.expr1.type, self.expr2.type)
        if self.type is None:
            self.error("Type error")

    def gen(self):
        return Arith(self.op, self.expr1.reduce(), self.expr2.reduce())

