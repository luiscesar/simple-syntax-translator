import unittest
from tests.TestContext import *
from compiler.frontend.symbols.Env import Env
from compiler.frontend.lexer.Word import Word
from compiler.frontend.lexer.Tag import Tag
from compiler.frontend.symbols.Type import Type
from compiler.frontend.inter.Id import Id


class EnvironmentTest(unittest.TestCase):

    def test001_env_init_case1(self):
        print(test_separator)
        print("test001_env_init_case1: Begin")
        env = Env(None)
        self.assertIsNotNone(env)
        print("env = " + str(env))

    def test002_env_put_case1(self):
        print(test_separator)
        print("test002_env_put_case1: Begin")
        env = Env(None)
        x = Word("x", Tag.ID)
        print("x = " + str(x))
        id_x = Id(x, Type.Int, 10)
        print("id_x = " + str(id_x))
        env.put(x, id_x)
        print("env = " + str(env))

    def test003_env_get_case2(self):
        print(test_separator)
        print("test003_env_get_case2: Begin")
        env = Env(None)
        x = Word("x", Tag.ID)
        print("x = " + str(x))
        id_x = Id(x, Type.Int, 10)
        print("id_x = " + str(id_x))
        env.put(x, id_x)
        id_y = env.get(x)
        print("id_y = " + str(id_y))
        self.assertEqual(id_y, id_x)


if __name__ == '__main__':
    unittest.main()
