
from compiler.frontend.symbols.Type import Type
from compiler.frontend.lexer.Tag import Tag


class Arrays(Type):

    def __str__(self):
        return "Arrays: [" + super().__str__() + \
               ", size = " + \
               str(self.size) + \
               ", of = " + \
               str(self.of) + "]"

    def __init__(self, size_c, type_c):
        super().__init__("[]", Tag.INDEX, size_c * type_c.width)
        self.size = size_c
        self.of = type_c
