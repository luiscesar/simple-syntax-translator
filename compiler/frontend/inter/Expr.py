
from compiler.frontend.inter.Node import Node


class Expr(Node):

    def __str__(self):
        return str(self.op)

    def __eq__(self, other):
        return isinstance(other, Expr) and \
               (self.op == other.op) and \
               (self.type == other.type)

    def __init__(self, op_c, type_c):
        super().__init__()
        self.op = op_c
        self.type = type_c

    def gen(self):
        return self

    def reduce(self):
        return self

    def jumping(self, t, f):
        self.emit_jumps(str(self.op), t, f)

    def emit_jumps(self, cond, t, f):
        if (not (t == 0)) and (not (f == 0)):
            self.emit("if " + str(cond) + " goto L" + str(t))
            self.emit("goto L" + str(f))
        elif not (t == 0):
            self.emit("if " + str(cond) + " goto L" + str(t))
        elif not (f == 0):
            self.emit("iffalse " + str(cond) + " goto L" + str(f))

