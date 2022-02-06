import unittest
from tests.TestContext import *
from compiler.frontend.inter.Node import Node


class NodeTest(unittest.TestCase):

    def test001_node_init_case1(self):
        print(test_separator)
        print("test001_node_init_case1: Begin")
        node = Node()
        self.assertIsNotNone(node)
        print("node = " + str(node))

    def test002_node_labels_case1(self):
        print(test_separator)
        print("test002_node_labels_case1: Begin")
        node = Node()
        self.assertIsNotNone(node)
        print("node = " + str(node))
        label = Node.new_label()
        self.assertEqual(label, 1)

    def test003_node_lexline_case1(self):
        print(test_separator)
        print("test003_node_lexline_case1: Begin")
        node = Node()
        self.assertIsNotNone(node)
        print("node = " + str(node))
        self.assertEqual(node.lex_line, 1)


if __name__ == '__main__':
    unittest.main()
