
from compiler.frontend.inter.Expr import Expr


class Id(Expr):

    def __str__(self):
        return super().__str__()

    def __eq__(self, other):
        return isinstance(other, Id) and \
               super(Id, self).__eq__(other) and \
               (other.offset == self.offset)

    def __init__(self, word_c, type_c, offset_c):
        super().__init__(word_c, type_c)
        self.offset = offset_c

