import unittest

from compiler.frontend.lexer.Real import Real
from compiler.frontend.lexer.Tag import Tag


class RealTest(unittest.TestCase):

    def test_test1(self):
        real = Real(0)
        print("real.value = " + str(real.value))
        self.assertEqual(real.value, 0)


if __name__ == '__main__':
    unittest.main()
