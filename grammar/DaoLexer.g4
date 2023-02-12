lexer grammar DaoLexer;

options { language=Python3; }

tokens { INDENT, DEDENT }

@lexer::header{
from antlr4.Token import CommonToken
import re
import importlib
# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))
}

@lexer::members {
@property
def tokens(self):
    try:
        return self._tokens
    except AttributeError:
        self._tokens = []
        return self._tokens

@property
def indents(self):
    try:
        return self._indents
    except AttributeError:
        self._indents = []
        return self._indents

@property
def opened(self):
    try:
        return self._opened
    except AttributeError:
        self._opened = 0
        return self._opened

@opened.setter
def opened(self, value):
    self._opened = value

@property
def lastToken(self):
    try:
        return self._lastToken
    except AttributeError:
        self._lastToken = None
        return self._lastToken

@lastToken.setter
def lastToken(self, value):
    self._lastToken = value

def reset(self):
    super().reset()
    self.tokens = []
    self.indents = []
    self.opened = 0
    self.lastToken = None

def emitToken(self, t):
    super().emitToken(t)
    self.tokens.append(t)

def nextToken(self):
    if self._input.LA(1) == Token.EOF and self.indents:
        for i in range(len(self.tokens)-1,-1,-1):
            if self.tokens[i].type == Token.EOF:
                self.tokens.pop(i)
        self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
        while self.indents:
            self.emitToken(self.createDedent())
            self.indents.pop()
        self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
    next = super().nextToken()
    if next.channel == Token.DEFAULT_CHANNEL:
        self.lastToken = next
    return next if not self.tokens else self.tokens.pop(0)

def createDedent(self):
    dedent = self.commonToken(LanguageParser.DEDENT, "")
    dedent.line = self.lastToken.line
    return dedent

def commonToken(self, type, text, indent=0):
    stop = self.getCharIndex()-1-indent
    start = (stop - len(text) + 1) if text else stop
    return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)

@staticmethod
def getIndentationCount(spaces):
    count = 0
    for ch in spaces:
        if ch == '\t':
            count += 8 - (count % 8)
        else:
            count += 1
    return count
def atStartOfInput(self):
    return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1
}

Import:                          '导入';

Func:                            '函数';
Class:                           '类';
Struct:                          '结构体';
Union:                           '共用体';
Enum:                            '枚举';

If:                              '如果';
ElseIf:                          '或者';
Else:                            '否则';
While:                           '当';
For:                             '对于';

Return:                          '返回';
Continue:                        '跳过';
Break:                           '跳出';
Goto:                            '跳到';

Byte:                            '字节';
Int16:                           '短整数';
Int32:                           '整数';
Int64:                           '长整数';
UInt16:                          '短正整数';
UInt32:                          '正整数';
UInt64:                          '长正整数';
Half:                            '短小数';
Float:                           '小数';
Double:                          '长小数';
Bool:                            '逻辑';
Text:                            '文本';
Char:                            '字符';

TrueLiteral:                     '真';
FalseLiteral:                    '假';
NullLiteral:                     '空';

LeftParen:                       '(';
RightParen:                      ')';
LeftBracket:                     '[';
RightBracket:                    ']';
LeftBrace:                       '{';
RightBrace:                      '}';

Less:                            '<';
LessEqual:                       '<=';
Greater:                         '>';
GreaterEqual:                    '>=';
LeftShift:                       '<<';
RightShift:                      '>>';

Plus:                            '+';
PlusPlus:                        '++';
Minus:                           '-';
MinusMinus:                      '--';
Star:                            '*';
Div:                             '/';
Mod:                             '%';

And:                             '&';
Or:                              '|';
AndAnd:                          '&&';
OrOr:                            '||';
Caret:                           '^';
Not:                             '!';
Tilde:                           '~';

Question:                        '?';
Colon:                           ':';
ColonColon:                      '::';
Semi:                            ';';
Comma:                           ',';

Assign:                          '=';
StarAssign:                      '*=';
DivAssign:                       '/=';
ModAssign:                       '%=';
PlusAssign:                      '+=';
MinusAssign:                     '-=';
LeftShiftAssign:                 '<<=';
RightShiftAssign:                '>>=';
AndAssign:                       '&=';
XorAssign:                       '^=';
OrAssign:                        '|=';

Equal:                           '==';
NotEqual:                        '!=';

Arrow:                           '->';
Dot:                             '.';
Ellipsis:                        '...';

Newline
 : ( {self.atStartOfInput()}?   SPACES
   | ( '\r'? '\n' | '\r' | '\f' ) SPACES?
   )
   {
tempt = Lexer.text.fget(self)
newLine = re.sub("[^\r\n\f]+", "", tempt)
spaces = re.sub("[\r\n\f]+", "", tempt)
la_char = ""
try:
    la = self._input.LA(1)
    la_char = chr(la)       # Python does not compare char to ints directly
except ValueError:          # End of file
    pass
# Strip newlines inside open clauses except if we are near EOF. We keep NEWLINEs near EOF to
# satisfy the final newline needed by the single_put rule used by the REPL.
try:
    nextnext_la = self._input.LA(2)
    nextnext_la_char = chr(nextnext_la)
except ValueError:
    nextnext_eof = True
else:
    nextnext_eof = False
if self.opened > 0 or nextnext_eof is False and (la_char == '\r' or la_char == '\n' or la_char == '\f' or la_char == '#'):
    self.skip()
else:
    indent = self.getIndentationCount(spaces)
    previous = self.indents[-1] if self.indents else 0
    self.emitToken(self.commonToken(self.NEWLINE, newLine, indent=indent))      # NEWLINE is actually the '\n' char
    if indent == previous:
        self.skip()
    elif indent > previous:
        self.indents.append(indent)
        self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
    else:
        while self.indents and self.indents[-1] > indent:
            self.emitToken(self.createDedent())
            self.indents.pop()
    }
 ;


BlockComment:                    '/*' .*? '*/' -> skip;
LineComment:                     '//' ~[\r\n]* -> skip;

IntegerLiteral:                  Digit+;
FloatLiteral:                    Digit* '.' Digit+ | Digit+ '.';

fragment Digit:                  [0-9];

StringLiteral:                   '"' SCharSequence? '"';

fragment SCharSequence:          SChar+;
fragment SChar:                  ~'"' | '\\"';

Identifier:                      IdentifierStart IdentifierContinue*;

fragment SPACES:                 [ \t]+;
fragment COMMENT:                '#' ~[\r\n\f]*;
fragment LINE_JOINING:           '\\' SPACES? ( '\r'? '\n' | '\r' | '\f' );

fragment IdentifierStart
    : [a-zA-Z_]
    | ChineseChar
    ;

fragment IdentifierContinue
    : [a-zA-Z0-9_]
    | ChineseChar
    ;

// 中文字符集 https://www.qqxiuzi.cn/zh/hanzi-unicode-bianma.php
fragment ChineseChar
    : '\u4E00'..'\u9FA5'
    | '\u9FA6'..'\u9FFF'
    | '\u3400'..'\u4DBF'
    | '\u{20000}'..'\u{2A6DF}'
    | '\u{2A700}'..'\u{2B738}'
    | '\u{2B740}'..'\u{2B81D}'
    | '\u{2B820}'..'\u{2CEA1}'
    | '\u{2CEB0}'..'\u{2EBE0}'
    | '\u{30000}'..'\u{3134A}'
    | '\u2F00'..'\u2FD5'
    | '\u2E80'..'\u2EF3'
    | '\uF900'..'\uFAD9'
    | '\u{2F800}'..'\u{2FA1D}'
    | '\uE815'..'\uE86F'
    | '\uE400'..'\uE5E8'
    | '\uE600'..'\uE6CF'
    | '\u31C0'..'\u31E3'
    | '\u2FF0'..'\u2FFB'
    | '\u3105'..'\u312F'
    | '\u31A0'..'\u31BA'
    | '\u3007'
    ;
