from compiler.frontend.inter.Stmt import Stmt
from compiler.error.CompilerError import CompilerError
from compiler.frontend.symbols.Type import Type
from compiler.frontend.symbols.Arrays import Arrays
from compiler.frontend.inter.Node import Node


class SetElem(Stmt):

    def __init__(self, access_c, expr_c):
        super().__init__()
        self.array = access_c.array
        self.index = access_c.index
        self.expr = expr_c
        if SetElem.check(access_c.type, expr_c.type) is None:
            raise CompilerError("Type error")

    def gen(self, begin_label, after_label):
        s1 = str(self.index.reduce())
        s2 = str(self.expr.reduce())
        Node.emit(str(self.array) + " [ " + s1 + " ] = " + s2)

    @staticmethod
    def check(type1, type2):
        if isinstance(type1, Arrays) or isinstance(type2, Arrays):
            return None
        elif type1 == type2:
            return type2
        elif Type.numeric(type1) and Type.numeric(type2):
            return type2
        else:
            return None


