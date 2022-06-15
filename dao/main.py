import sys

from .lexer import Lexer


def main():
    if len(sys.argv) == 1:
        print("gcc: fatal error: no input files")
    else:
        lexer = Lexer(sys.argv[1])
        src_file = sys.argv[1]
        print(src_file)


if __name__ == '__main__':
    main()
