from compiler.frontend.inter.Logical import Logical
from compiler.error.CompilerError import CompilerError


class Not(Logical):

    def __init__(self, token_c, expr_c):
        super().__init__(token_c, expr_c, expr_c)

    def __str__(self):
        return str(self.op) + " " + str(self.expr2)

    def jumping(self, t, f):
        try:
            self.expr2.jumping(f, t)
        except (RuntimeError, TypeError, NameError) as err:
            raise CompilerError(err)
