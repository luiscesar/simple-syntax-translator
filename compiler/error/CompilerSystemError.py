

class CompilerSystemError(BaseException):

    def __init__(self, error):
        super().__init__(error)
        self.message = "CompilerException: " + str(error)

    def __str__(self):
        return super().__str__() + ", message = " + str(self.message)

