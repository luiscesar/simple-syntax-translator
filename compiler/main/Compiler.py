
from compiler.frontend.lexer.Lexer import Lexer
from compiler.frontend.parser.Parser import Parser
from compiler.error.CompilerError import CompilerError
from compiler.error.CompilerSystemError import CompilerSystemError
import sys

try:
    if len(sys.argv) != 2:
        raise ValueError('Please provide an File Name.')
    file_name = sys.argv[1]
    lex = Lexer(file_name)
    parser = Parser(lex)
    parser.program()
    print("\n")
except CompilerError as err:
    print("Compiler Error: " + str(err))
except CompilerSystemError as err:
    print("Compiler System ERROR: Compiler System Error: " + str(err))
except Exception as err:
    print("Compiler System ERROR: Unexpected error: " + str(err))

