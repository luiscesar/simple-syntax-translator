from compiler.frontend.inter.Stmt import Stmt
from compiler.frontend.symbols.Type import Type
from compiler.error.CompilerError import CompilerError
from compiler.frontend.inter.Node import Node


class If(Stmt):

    def __init__(self, expr_c, stmt_c):
        self.expr = expr_c
        self.stmt = stmt_c
        if not (self.expr.type == Type.Bool):
            self.error("Boolean required in if")

    def gen(self, begin_label, after_label):
        label_c = Node.new_label()
        self.expr.jumping(0, after_label)
        Node.emit_label(label_c)
        self.stmt.gen(label_c, after_label)

