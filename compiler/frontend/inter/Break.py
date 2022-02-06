
from compiler.frontend.inter.Stmt import Stmt
from compiler.error.CompilerError import CompilerError
from compiler.frontend.inter.Node import Node


class Break(Stmt):

    def __init__(self):
        if Stmt.Enclosing == Stmt.NULL:
            self.error("unenclosed  break")
        self.stmt = Stmt.Enclosing

    def gen(self, begin_label, after_label):
        Node.emit("goto L" + str(self.stmt.after))


