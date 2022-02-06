
from compiler.frontend.inter.Stmt import Stmt
from compiler.frontend.symbols.Type import Type
from compiler.frontend.inter.Node import Node
from compiler.error.CompilerError import CompilerError


class While(Stmt):

    def __init__(self):
        self.expr = None
        self.stmt = None

    def init(self, expr_c, stmt_c):
        self.expr = expr_c
        self.stmt = stmt_c
        if not (self.expr.type == Type.Bool):
            self.error("Boolean required in while")

    def gen(self, begin_label, after_label):
        self.after = after_label
        self.expr.jumping(0, after_label)
        label_c = Node.new_label()
        Node.emit_label(label_c)
        self.stmt.gen(label_c, begin_label)
        Node.emit("goto L" + str(begin_label))

