import sys
from antlr4 import *

from dao.generated.DaoLexer import DaoLexer


def main():
    if len(sys.argv) == 1:
        print("dao: fatal error: no input files")
    else:
        src_file = sys.argv[1]
        lexer = DaoLexer(FileStream(src_file, encoding="utf8"))
        print(src_file)


if __name__ == '__main__':
    main()
