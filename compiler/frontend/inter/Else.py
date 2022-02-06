
from compiler.frontend.inter.Stmt import Stmt
from compiler.frontend.symbols.Type import *
from compiler.frontend.inter.Node import Node
from compiler.error.CompilerError import CompilerError


class Else(Stmt):

    def __init__(self, expr_c, stmt1_c, stmt2_c):
        super().__init__()
        self.expr = expr_c
        self.stmt1 = stmt1_c
        self.stmt2 = stmt2_c
        if not (self.expr.type == Type.Bool):
            self.error("Boolean required in if")

    def gen(self, begin_label, after_label):
        label1 = Node.new_label()
        label2 = Node.new_label()
        self.expr.jumping(0, label2)
        Node.emit_label(label1)
        self.stmt1.gen(label1, after_label)
        Node.emit("goto L" + str(after_label))
        Node.emit_label(label2)
        self.stmt2.gen(label2, after_label)
