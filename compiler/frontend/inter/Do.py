from compiler.frontend.inter.Stmt import Stmt
from compiler.frontend.symbols.Type import Type
from compiler.frontend.inter.Node import Node
from compiler.error.CompilerError import CompilerError


class Do(Stmt):

    def __init__(self):
        self.expr = None
        self.stmt = None

    def init(self, expr_c, stmt_c):
        self.expr = expr_c
        self.stmt = stmt_c
        if not (self.expr.type == Type.Bool):
            self.error("Boolean required in do")

    def gen(self, b, a):
        self.after = a
        label = Node.new_label()
        self.stmt.gen(b, label)
        Node.emit_label(label)
        self.expr.jumping(b, 0)
