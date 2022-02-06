

class CompilerError(BaseException):

    def __init__(self, error):
        super().__init__(error)
        #self.message = str(error)

    def __str__(self):
        return super().__str__()

