import unittest
from tests.TestContext import *
from compiler.frontend.inter.Id import Id
from compiler.frontend.lexer.Tag import Tag
from compiler.frontend.lexer.Word import Word
from compiler.frontend.symbols.Type import Type


class IdTest(unittest.TestCase):

    def test001_id_init_case1(self):
        print(test_separator)
        print("test001_id_init_case1: Begin")
        x = Word("x", Tag.ID)
        id_x = Id(x, Type.Int, 10)
        print("id_x = " + str(id_x))

    def test002_id_eq_case1(self):
        print(test_separator)
        print("test002_id_eq_case1: Begin")
        x = Word("x", Tag.ID)
        id_x = Id(x, Type.Int, 10)
        print("id_x = " + str(id_x))
        y = Word("x", Tag.ID)
        id_y = Id(y, Type.Int, 10)
        print("id_y = " + str(id_y))
        self.assertEqual(id_x, id_y)


if __name__ == '__main__':
    unittest.main()