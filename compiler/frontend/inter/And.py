from compiler.frontend.inter.Logical import Logical
from compiler.frontend.inter.Node import Node
from compiler.error.CompilerError import CompilerError


class And(Logical):

    def __init__(self, token_c, expr1_c, expr2_c):
        super().__init__(token_c, expr1_c, expr2_c)

    def __str__(self):
        super().__str__()

    def jumping(self, t, f):
        try:
            label = f if (f is not 0) else Node.new_label()
            self.expr1.jumping(0, label)
            self.expr2.jumping(t, f)
            if f is 0:
                Node.emit_label(label)
        except (RuntimeError, TypeError, NameError) as err:
            raise CompilerError(err)

