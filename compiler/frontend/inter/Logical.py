from compiler.frontend.inter.Expr import Expr
from compiler.frontend.symbols.Type import Type
from compiler.frontend.inter.Node import Node
from compiler.frontend.inter.Temp import Temp
from compiler.error.CompilerError import CompilerError


class Logical(Expr):

    def gen(self):
        try:
            f = Node.new_label()
            a = Node.new_label()
            temp = Temp(self.type)
            self.jumping(0, f)
            self.emit(str(temp) + " = true")
            self.emit("goto L" + str(a))
            self.emit_label(f)
            self.emit(str(temp) + " = false")
            self.emit_label(a)
            return temp
        except (RuntimeError, TypeError, NameError) as err:
            raise CompilerError(err)

    def __str__(self):
        return str(self.expr1) + " " + str(self.op) + " " + str(self.expr2)

    def __init__(self, token_c, expr1_c, expr2_c):
        super().__init__(token_c, None)
        self.expr1 = expr1_c
        self.expr2 = expr2_c
        self.type = self.check(self.expr1.type, self.expr2.type)
        if self.type is None:
            self.error("Boolean expected")

    def check(self, type1_c, type2_c):
        result = None
        if (type1_c == Type.Bool) and (type2_c == Type.Bool):
            return Type.Bool
        return result
