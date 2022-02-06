

class Env:

    def __str__(self):
        return "Env: [table = " + \
               str(self.table) + \
               ", prev = " + str(self.prev) + "]"

    def __init__(self, prev_env):
        self.table = {}
        self.prev = prev_env

    def put(self, word_c, id_c):
        if (word_c is not None) and (id_c is not None):
            self.table[word_c.lexeme] = id_c

    def get(self, word_c):
        result = None
        env_c = self
        while env_c is not None:
            if word_c.lexeme in env_c.table:
                result = env_c.table[word_c.lexeme]
                break
            env_c = self.prev
        return result

