import os

from dao.token import TokenKind, Token

__ALL__ = ["Lexer"]


class Lexer:
    def __init__(self, src_file=None):
        self._src = None
        self._pos = None
        self._line = None
        self._col = None
        self._intents = None

        self._c = None
        self._n = None
        self._nn = None

        self.load(src_file)

    def load_file(self, src_file):
        if not os.path.exists(src_file):
            raise FileNotFoundError(src_file)

        with open(src_file, "r") as f:
            src = f.read()

        return self.load(src)

    def load(self, src):
        self._src = src
        self._pos = -1
        self._line = 0
        self._col = -1
        self._intents = []

        self._c = None
        self._n = None
        self._nn = None

        self._next_char()

    def next_token(self):
        pass

    def _next_char(self, step=1):
        total = len(self._src)

        self._pos += step
        self._c = None if self._pos >= total else self._src[self._pos]
        self._n = None if self._pos + 1 >= total else self._src[self._pos + 1]
        self._nn = None if self._pos + 2 >= total else self._src[self._pos + 2]

        self._col += step
        return self._pos < total
