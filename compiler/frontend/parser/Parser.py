from compiler.error.CompilerError import CompilerError
from compiler.frontend.inter.Node import Node
from compiler.frontend.symbols.Env import Env
from compiler.frontend.inter.Id import Id
from compiler.frontend.symbols.Arrays import Arrays
from compiler.frontend.inter.Stmt import Stmt
from compiler.frontend.inter.Seq import Seq
from compiler.frontend.inter.If import If
from compiler.frontend.inter.Else import Else
from compiler.frontend.inter.While import While
from compiler.frontend.inter.Do import Do
from compiler.frontend.inter.Break import Break
from compiler.frontend.inter.Set import Set
from compiler.frontend.inter.SetElem import SetElem
from compiler.frontend.inter.Or import Or
from compiler.frontend.inter.And import And
from compiler.frontend.inter.Rel import Rel
from compiler.frontend.inter.Arith import Arith
from compiler.frontend.inter.Unary import Unary
from compiler.frontend.lexer.Word import *
from compiler.frontend.inter.Not import Not
from compiler.frontend.inter.Constant import Constant
from compiler.frontend.symbols.Type import Type
from compiler.frontend.lexer.Token import Token
from compiler.frontend.inter.Access import Access
from compiler.frontend.lexer.Lexer import Lexer
from compiler.error.CompilerSystemError import CompilerSystemError

class Parser:

    def __init__(self, lexer_c):
        self.lex = lexer_c
        self.look = None
        self.top = None
        self.used = 0
        self.move()

    def move(self):
        self.look = self.lex.scan()

    def error(self, string_c):
        #print("Near line " + str(self.lex.line) + ": " + string_c)
        raise CompilerError("Near line " + str(Lexer.line) + ": " + string_c)

    def match(self, int_c):
        if self.look.tag == int_c:
            self.move()
        else:
            self.error("Syntax error")

    def program(self):
        stmt = self.block()
        begin = Node.new_label()
        after = Node.new_label()
        Node.emit_label(begin)
        stmt.gen(begin, after)
        Node.emit_label(after)

    def block(self):
        self.match('{')
        saved_env = self.top
        self.top = Env(self.top)
        self.decls()
        stmt = self.stmts()
        self.match('}')
        self.top = saved_env
        return stmt

    def decls(self):
        while self.look.tag == Tag.BASIC:
            type_c = self.type()
            token_c = self.look
            self.match(Tag.ID)
            self.match(';')
            id_c = Id(token_c, type_c, self.used)
            self.top.put(token_c, id_c)
            self.used = self.used + type_c.width

    def type(self):
        type_c = self.look
        self.match(Tag.BASIC)
        if not (self.look.tag == '['):
            return type_c
        else:
            return self.dims(type_c)

    def dims(self, type_c):
        self.match('[')
        token_c = self.look
        self.match(Tag.NUM)
        self.match(']')
        if self.look.tag == '[':
            type_c = self.dims(type_c)
        return Arrays(token_c.value, type_c)

    def stmts(self):
        if self.look.tag == '}':
            return Stmt.NULL
        else:
            return Seq(self.stmt(), self.stmts())

    def stmt(self):
        switcher = {
            ';': self.semi_colon_tag,
            Tag.IF: self.if_tag,
            Tag.WHILE: self.while_tag,
            Tag.DO: self.do_tag,
            Tag.BREAK: self.break_tag,
            '{': self.block_tag
        }
        return switcher.get(self.look.tag, self.assign_tag)()

    def semi_colon_tag(self):
        self.move()
        return Stmt.NULL

    def if_tag(self):
        self.match(Tag.IF)
        self.match('(')
        x = self.bool()
        self.match(')')
        s1 = self.stmt()
        if not (self.look.tag == Tag.ELSE):
            return If(x, s1)
        else:
            self.match(Tag.ELSE)
            s2 = self.stmt()
            return Else(x, s1, s2)

    def while_tag(self):
        while_node = While()
        saved_stmt = Stmt.Enclosing
        Stmt.Enclosing = while_node
        self.match(Tag.WHILE)
        self.match('(')
        x = self.bool()
        self.match(')')
        s1 = self.stmt()
        while_node.init(x, s1)
        Stmt.Enclosing = saved_stmt
        return while_node

    def do_tag(self):
        do_node = Do()
        saved_stmt = Stmt.Enclosing
        Stmt.Enclosing = do_node
        self.match(Tag.DO)
        s1 = self.stmt()
        self.match(Tag.WHILE)
        self.match('(')
        x = self.bool()
        self.match(')')
        self.match(';')
        do_node.init(x, s1)
        Stmt.Enclosing = saved_stmt
        return do_node

    def break_tag(self):
        self.match(Tag.BREAK)
        self.match(';')
        return Break()

    def block_tag(self):
        return self.block()

    def assign_tag(self):
        return self.assign()

    def assign(self):
        t = self.look
        self.match(Tag.ID)
        id_c = self.top.get(t)
        if id_c is None:
            self.error(str(t) + " undeclared")
        if self.look.tag == '=':
            self.move()
            stmt = Set(id_c, self.bool())
        else:
            x = self.offset(id_c)
            self.match('=')
            stmt = SetElem(x, self.bool())
        self.match(';')
        return stmt

    def bool(self):
        x = self.join()
        while self.look.tag == Tag.OR:
            tok = self.look
            self.move()
            x = Or(tok, x, self.join())
        return x

    def join(self):
        x = self.equality()
        while self.look.tag == Tag.AND:
            tok = self.look
            self.move()
            x = And(tok, x, self.equality())
        return x

    def equality(self):
        x = self.rel()
        while (self.look.tag == Tag.EQ) or (self.look.tag == Tag.NE):
            tok = self.look
            self.move()
            x = Rel(tok, x, self.rel())
        return x

    def rel(self):
        x = self.expr()
        switcher = {
            '<': self.rel_tag,
            Tag.LE: self.rel_tag,
            Tag.GE: self.rel_tag,
            '>': self.rel_tag
        }
        return switcher.get(self.look.tag, lambda x: x)(x)

    def rel_tag(self, x):
        tok = self.look
        self.move()
        return Rel(tok, x, self.expr())

    def expr(self):
        x = self.term()
        while (self.look.tag == '+') or (self.look.tag == '-'):
            tok = self.look
            self.move()
            x = Arith(tok, x, self.term())
        return x

    def term(self):
        x = self.unary()
        while (self.look.tag == '*') or (self.look.tag == '/'):
            tok = self.look
            x = Arith(tok, x, self.unary())
        return x

    def unary(self):
        if self.look.tag == '-':
            self.move()
            return Unary(Word.MINUS, self.unary())
        elif self.look.tag == '!':
            tok = self.look
            self.move()
            return Not(tok, self.unary())
        else:
            return self.factor()

    def factor(self):
        switcher = {
            '(': self.case_open_parentheses,
            Tag.NUM: self.case_num,
            Tag.REAL: self.case_real,
            Tag.TRUE: self.case_true,
            Tag.FALSE: self.case_false,
            Tag.ID: self.case_id
        }
        return switcher.get(self.look.tag, self.default_factor)()

    def case_open_parentheses(self):
        self.move()
        x = self.bool()
        self.match(')')
        return x

    def case_num(self):
        x = Constant(self.look, Type.Int)
        self.move()
        return x

    def case_real(self):
        x = Constant(self.look, Type.Float)
        self.move()
        return x

    def case_true(self):
        x = Constant.TRUE
        self.move()
        return x

    def case_false(self):
        x = Constant.FALSE
        self.move()
        return x

    def case_id(self):
        s = str(self.look)
        id_c = self.top.get(self.look)
        if id_c is None:
            self.error(s + " undeclared")
        self.move()
        if not (self.look.tag == '['):
            return id_c
        else:
            return self.offset(id_c)

    def default_factor(self):
        self.error("syntax error")

    def offset(self, a):
        result = None
        try:
            type_c = a.type
            self.match('[')
            i = self.bool()
            self.match(']')
            type1 = type_c.of
            w = Constant.int(type1.width)
            t1 = Arith(Token('*'), i, w)
            loc = t1
            while self.look.tag == '[':
                self.match('[')
                i = self.bool()
                self.match(']')
                type_c = type_c.of
                w = Constant(type_c.width)
                t1 = Arith(Token('*'), i, w)
                t2 = Arith(Token('+'), loc, t1)
                loc = t2

            result = Access(a, loc, type1)
        except Exception as err:
            exception = CompilerSystemError(err)
            print("ERROR")
            raise exception

        return result
