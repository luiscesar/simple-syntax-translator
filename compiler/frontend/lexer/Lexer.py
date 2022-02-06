
from compiler.frontend.lexer.Word import Word
from compiler.frontend.symbols.Type import Type
from compiler.frontend.lexer.Token import Token
from compiler.frontend.lexer.Num import Num
from compiler.frontend.lexer.Real import Real
from compiler.frontend.lexer.Tag import Tag


from compiler.error.CompilerSystemError import CompilerSystemError

class Lexer:

    line = 1

    single_token_list= [';', '[', ']', '{', '}', '(', ')', '+', '-', '=', '<', '>']

    def __str__(self):
        return "Lexer: [peek = " + \
               str(self.peek) + \
               ", words = " + \
               str(self.words) + "]"

    def __init__(self, file_name):
        self.peek = ''
        self.has_to_move = True
        self.words = {}
        self.double_lexemes = {}
        reserve(self, Word.IF)
        reserve(self, Word.ELSE)
        reserve(self, Word.WHILE)
        reserve(self, Word.DO)
        reserve(self, Word.BREAK)
        reserve(self, Word.TRUE)
        reserve(self, Word.FALSE)
        reserve(self, Type.Int)
        reserve(self, Type.Char)
        reserve(self, Type.Bool)
        reserve(self, Type.Float)
        load_double_lexemes(self)
        self.f = open(file_name)

    def readch(self):
        if self.has_to_move:
            self.peek = self.f.read(1)

    def readch_next(self, c):
        self.has_to_move = True
        self.readch()
        if not (self.peek == c):
            self.has_to_move = False
            return False
        return True

    def scan(self):
        try:
            while True:
                self.readch()
                if (self.peek == ' ') or (self.peek == '\t'):
                    self.has_to_move = True
                    continue
                elif self.peek == '\n':
                    self.has_to_move = True
                    Lexer.line = Lexer.line + 1
                else:
                    break
            if self.peek in self.double_lexemes:
                return self.double_lexemes.get(self.peek)(self)
            else:
                if self.peek.isdigit():
                    num_value = 0
                    self.has_to_move = True
                    while True:
                        num_value = num_value * 10 + int(self.peek, 10)
                        self.readch()
                        if not self.peek.isdigit():
                            break
                    if not (self.peek == '.'):
                        self.has_to_move = False;
                        return Num(num_value)
                    else:
                        float_value = float(num_value)
                        d = 10
                        while True:
                            self.readch()
                            if not (self.peek.isdigit()):
                                break
                            else:
                                float_value = float_value + int(self.peek, 10) / d
                                d = 10 * d
                    self.has_to_move = False
                    return Real(float_value)
                else:
                    if self.peek.isalpha():
                        lexeme_c = ""
                        self.has_to_move = True
                        while True:
                            lexeme_c = lexeme_c + str(self.peek)
                            self.readch()
                            if not (self.peek.isalpha() or self.peek.isdigit()):
                                break
                        self.has_to_move = False
                        if lexeme_c in self.words:
                            return self.words[lexeme_c]
                        else:
                            word_new = Word(lexeme_c, Tag.ID)
                            self.words[lexeme_c] = word_new
                            return word_new
                    else:
                        token = Token(self.peek)
                        self.has_to_move = True;
                        return token
        except Exception as err:
            exception = CompilerSystemError(err)
            print("Lexer: ERROR: " + str(err))
            raise exception

    def is_separator(self, item):
        return (item == '\n') or (item == ' ') or (item == '\t')

    def set_has_to_move(self):
        if self.is_separator(self.peek):
            self.has_to_move = True
        else:
            self.has_to_move = False


def reserve(lexer, word):
    lexer.words[word.lexeme] = word


def load_double_lexemes(lexer):
    lexer.double_lexemes['&'] = lambda x: Word.AND if x.readch_next('&') else Token('&')
    lexer.double_lexemes['|'] = lambda x: Word.OR if x.readch_next('|') else Token('|')
    lexer.double_lexemes['='] = lambda x: Word.EQ if x.readch_next('=') else Token('=')
    lexer.double_lexemes['!'] = lambda x: Word.NE if x.readch_next('=') else Token('!')
    lexer.double_lexemes['<'] = lambda x: Word.LE if x.readch_next('=') else Token('<')
    lexer.double_lexemes['>'] = lambda x: Word.GE if x.readch_next('=') else Token('>')


def or_lexeme(lexer):
    if lexer.readch_next('|'):
        return Word.OR
    else:
        return Token('|')


def and_lexeme(lexer):
    if lexer.readch_next('&'):
        return Word.AND
    else:
        return Token('&')


def eq_lexeme(lexer):
    if lexer.readch_next('='):
        return Word.EQ
    else:
        return Token('=')


def ne_lexeme(lexer):
    if lexer.readch_next('='):
        return Word.NE
    else:
        return Token('!')


def le_lexeme(lexer):
    if lexer.readch_next('='):
        return Word.LE
    else:
        return Token('<')


def ge_lexeme(lexer):
    if lexer.readch_next('='):
        return Word.GE
    else:
        return Token('>')

