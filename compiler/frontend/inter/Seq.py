
from compiler.frontend.inter.Stmt import Stmt
from compiler.frontend.inter.Node import Node

class Seq(Stmt):

    def __init__(self, stmt1_c, stmt2_c):
        self.stmt1 = stmt1_c
        self.stmt2 = stmt2_c

    def gen(self, begin_label, after_label):
        if self.stmt1 == Stmt.NULL:
            self.stmt2.gen(begin_label, after_label)
        elif self.stmt2 == Stmt.NULL:
            self.stmt1.gen(begin_label, after_label)
        else:
            label = Node.new_label()
            self.stmt1.gen(begin_label, label)
            Node.emit_label(label)
            self.stmt2.gen(label, after_label)

