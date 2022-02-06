import unittest

from tests.TestContext import *
from compiler.frontend.inter.Constant import Constant

class ConstantTest(unittest.TestCase):

    def test001_constant_init_case1(self):
        print(test_separator)
        print("test001_constant_init_case1: Begin")
        const_true = Constant.TRUE
        self.assertIsNotNone(const_true)
        print("const_true = " + str(const_true))
        const_false = Constant.FALSE
        self.assertIsNotNone(const_false)
        print("const_false = " + str(const_false))

    def test002_constant_jumping_case1(self):
        print(test_separator)
        print("test002_constant_jumping_case1: Begin")
        try:
            const_true = Constant.TRUE
            const_true.jumping(1, 10)
        except Exception as err:
            self.fail(str(err))

    def test003_constant_jumping_case2(self):
        print(test_separator)
        print("test003_constant_jumping_case2: Begin")
        try:
            const_false = Constant.FALSE
            const_false.jumping(0, 10)
        except Exception as err:
            self.fail(str(err))

if __name__ == '__main__':
    unittest.main()
