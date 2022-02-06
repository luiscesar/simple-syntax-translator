import unittest
from tests.TestContext import *
from compiler.frontend.symbols.Type import Type
from compiler.frontend.symbols.Arrays import Arrays


class ArraysTest(unittest.TestCase):

    def test001_arrays_init_case1(self):
        print(test_separator)
        print("test001_arrays_init_case1: Begin")
        arrays = Arrays(10, Type.Int)
        print("arrays = " + str(arrays))


