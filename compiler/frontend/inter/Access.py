
from compiler.frontend.inter.Op import Op
from compiler.frontend.lexer.Word import Word
from compiler.frontend.lexer.Tag import Tag


class Access(Op):

    def __str__(self):
        return str(self.array) + " [ " + str(self.index) + " ] "

    def __init__(self, id_c, expr_c, type_c):
        super().__init__(Word("[]", Tag.INDEX), type_c)
        self.array = id_c
        self.index = expr_c

    def gen(self):
        return Access(self.array, self.index.reduce(), self.type)

    def jumping(self, t_label, f_label):
        self.emit_jumps(str(self.reduce()), t_label, f_label)


