
from compiler.frontend.lexer.Word import Word
from compiler.frontend.lexer.Tag import Tag


class Type(Word):

    def __init__(self, s, t, w):
        super().__init__(s, t)
        self.width = w

    def __str__(self):
        return "Type: [" + super().__str__() + ", width = " + str(self.width) + "]"

    def __eq__(self, other):
        return isinstance(other, Type) and \
               super().__eq__(other) and \
               (self.width == other.width)


    @staticmethod
    def numeric(type_c):
        result = (type_c == Type.Char) or (type_c == Type.Int) or (type_c == Type.Float)
        return result

    @staticmethod
    def max(type_c1, type_c2):
        if (not Type.numeric(type_c1)) or (not Type.numeric(type_c2)):
            return None
        elif (type_c1 == Type.Float) or (type_c2 == Type.Float):
            return Type.Float
        elif (type_c1 == Type.Int) or (type_c2 == Type.Int):
            return Type.Int
        else:
            return Type.Char


Type.Int = Type("int", Tag.BASIC, 4)
Type.Float = Type("float", Tag.BASIC, 8)
Type.Char = Type("char", Tag.BASIC, 1)
Type.Bool = Type("bool", Tag.BASIC, 1)

