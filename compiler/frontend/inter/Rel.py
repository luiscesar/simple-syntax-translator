from compiler.frontend.inter.Logical import Logical
from compiler.frontend.symbols.Arrays import Arrays
from compiler.frontend.symbols.Type import Type
from compiler.error.CompilerError import CompilerError


class Rel(Logical):

    def __init__(self, token_c, expr1_c, expr2_c):
        super().__init__(token_c, expr1_c, expr2_c)

    def check(self, type1_c, type2_c):
        result = None
        if (not isinstance(type1_c, Arrays)) and \
                (not isinstance(type2_c, Arrays)):
            if type1_c == type2_c:
                result = Type.Bool
        return result

    def jumping(self, t, f):
        try:
            a = self.expr1.reduce()
            b = self.expr2.reduce()
            cond = str(a) + " " + str(self.op) + " " + str(b)
            self.emit_jumps(cond, t, f)
        except (RuntimeError, TypeError, NameError) as err:
            raise CompilerError(err)

