import unittest

from tests.TestContext import *
from compiler.common.Switcher import Switcher


class SwitcherTest(unittest.TestCase):

    def test001_switcher_init_case1(self):
        print(test_separator)
        print("test001_switcher_init_case1: Begin")
        switcher = Switcher("test")
        self.assertIsNotNone(switcher)
        print("switcher = " + str(switcher))

    def test002_switcher_call_case1(self):
        print(test_separator)
        print("test002_switcher_call_case1: Begin")
        switcher = Switcher("test")
        self.assertIsNotNone(switcher)
        case = 1
        switcher.call(case)

    def test003_switcher_call_case2(self):
        print(test_separator)
        print("test003_switcher_call_case2: Begin")
        switcher = Switcher("test")
        self.assertIsNotNone(switcher)
        case = 2
        switcher.call(case)

    def test004_switcher_call_case3(self):
        print(test_separator)
        print("test004_switcher_call_case3: Begin")
        switcher = Switcher("test")
        self.assertIsNotNone(switcher)
        case = 3
        switcher.call(case)
        case = 2
        switcher.call(case)


if __name__ == '__main__':
    unittest.main()

