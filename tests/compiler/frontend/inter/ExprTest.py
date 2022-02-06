import unittest
from tests.TestContext import *
from compiler.frontend.inter.Expr import Expr
from compiler.frontend.lexer.Token import Token
from compiler.frontend.lexer.Tag import Tag
from compiler.frontend.symbols.Type import Type
from compiler.frontend.lexer.Word import Word


class ExprTest(unittest.TestCase):

    def test001_expr_init_case1(self):
        print(test_separator)
        print("test001_expr_init_case1: Begin")
        expr = Expr(Token(Tag.AND), Type.Bool)
        self.assertIsNotNone(expr)
        print("expr = " + str(expr))

    def test002_expr_gen_case1(self):
        print(test_separator)
        print("test002_expr_gen_case1: Begin")
        try:
            expr = Expr(Word.TRUE, Type.Bool)
            expr.jumping(1, 10)
        except Exception as err:
            self.fail(str(err))

    def test003_expr_gen_case2(self):
        print(test_separator)
        print("test003_expr_gen_case2: Begin")
        try:
            expr = Expr(Word.TRUE, Type.Bool)
            expr.jumping(1, 0)
        except Exception as err:
            self.fail(str(err))

    def test004_expr_gen_case3(self):
        print(test_separator)
        print("test004_expr_gen_case3: Begin")
        try:
            expr = Expr(Word.TRUE, Type.Bool)
            expr.jumping(0, 10)
        except Exception as err:
            self.fail(str(err))


if __name__ == '__main__':
    unittest.main()
