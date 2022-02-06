import unittest

from compiler.frontend.lexer.Tag import Tag


class TagTest(unittest.TestCase):

    def test_test1(self):
        tag = Tag()
        self.assertEqual(tag.AND, 256)
        tag1 = Tag()
        tag1.AND = 100
        self.assertEqual(tag.AND, 256)
        self.assertEqual(Tag.AND, 256)
        self.assertEqual(tag1.AND, 100)
        Tag.AND = 100
        self.assertEqual(Tag.AND, 100)
        tag2 = Tag()
        self.assertEqual(tag2.AND, 100)


if __name__ == '__main__':
    unittest.main()
