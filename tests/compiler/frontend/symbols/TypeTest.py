
import unittest
from compiler.frontend.symbols.Type import Type
from compiler.frontend.lexer.Tag import Tag


class TypeTest(unittest.TestCase):

    def test001_type_case1(self):
        print("test001_type_case1: Begin")
        print(Type.Int)
        self.assertEqual(Type.Int.width, 4)
        self.assertEqual(Type.Int.lexeme, "int")
        self.assertEqual(Type.Int.tag, Tag.BASIC)

    def test002_numeric_case1(self):
        print("\n======================================================================")
        print("test002_numeric_case1: Begin")
        type_c = Type.Int
        print(Type.numeric(type_c))
        self.assertTrue(Type.numeric(type_c))
        type_c = Type.Bool
        print(Type.numeric(type_c))
        self.assertFalse(Type.numeric(type_c))

    def test003_max_case1(self):
        print("\n======================================================================")
        print("test003_max_case1: Begin")
        type_c1 = Type.Int
        type_c2 = Type.Float
        print(Type.max(type_c1, type_c2))
        self.assertEqual(Type.max(type_c1, type_c2), Type.Float)


if __name__ == '__main__':
    unittest.main()


