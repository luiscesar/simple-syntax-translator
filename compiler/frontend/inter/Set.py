
from compiler.frontend.inter.Stmt import Stmt
from compiler.frontend.inter.Node import Node
from compiler.frontend.symbols.Type import *
from compiler.frontend.symbols.Arrays import Arrays
from compiler.error.CompilerError import CompilerError


class Set(Stmt):

    def __init__(self, id_c, expr_c):
        self.id = id_c
        self.expr = expr_c
        if self.check(self.id.type, self.expr.type) is None:
            self.error("Type error")

    def gen(self, begin_label, after_label):
        Node.emit(str(self.id) + " = " + str(self.expr.gen()))

    def check(self, type1, type2):
        if Type.numeric(type1) and Type.numeric(type2):
            return type2
        elif (type1 == Type.Bool) and (type2 == Type.Bool):
            return type2
        elif isinstance(type2, Arrays) and Type.numeric(type1) and Type.numeric(type2.of):
            return type1
        else:
            return None
