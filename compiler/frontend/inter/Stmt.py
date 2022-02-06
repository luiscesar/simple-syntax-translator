from compiler.frontend.inter.Node import Node


class Stmt(Node):

    def __init__(self):
        self.after = 0

    def gen(self, begin_label, after_label):
        pass

    def __eq__(self, other):
        if (other is None) or isinstance(other, Stmt):
            return False
        else:
            return self.after == other.after


Stmt.NULL = Stmt()
Stmt.Enclosing = Stmt.NULL

