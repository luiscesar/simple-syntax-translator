

class Token:

    def __str__(self):
        return str(self.tag)

    def __init__(self, t):
        self.tag = t

    def __eq__(self, other):
        if not isinstance(other, Token):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.tag == other.tag

