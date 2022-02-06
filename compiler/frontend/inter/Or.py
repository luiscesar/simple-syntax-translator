
from compiler.frontend.inter.Logical import Logical
from compiler.frontend.inter.Node import Node


class Or(Logical):

    def __init__(self, token_c, expr1_c, expr2_c):
        super().__init__(token_c, expr1_c, expr2_c)

    def __str__(self):
        super().__str__()

    def jumping(self, t, f):
        label = t if not (t == 0) else Node.new_label()
        self.expr1.jumping(label, 0)
        self.expr2.jumping(t, f)
        if t == 0:
            Node.emit_label(label)


