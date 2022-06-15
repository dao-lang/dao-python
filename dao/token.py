import enum

__ALL__ = ["TokenKind", "Token"]


class TokenKind(enum):
    KW_Import = 1  # 导入
    KW_Func = 2  # 函数
    KW_Class = 3  # 类
    KW_Struct = 4  # 结构体
    KW_Union = 5  # 联合体
    KW_Enum = 6  # 枚举

    KW_If = 10  # 如果
    KW_ElseIf = 11  # 或者
    KW_Else = 12  # 否则
    KW_While = 13  # 当
    KW_For = 14  # 对于
    KW_Return = 15  # 返回
    KW_Continue = 16  # 跳过
    KW_Break = 17  # 跳出
    KW_Goto = 18  # 跳到

    KW_True = 20  # 真
    KW_False = 21  # 假
    KW_Null = 22  # 空1

    OP_LeftParen = 30  # (
    OP_RightParen = 31  # )

    OP_LeftBracket = 32  # [
    OP_RightBracket = 33  # ]
    OP_LeftBrace = 34  # {
    OP_RightBrace = 35  # }

    OP_Less = 36  # <
    OP_LessEqual = 37  # <=
    OP_Greater = 38  # >
    OP_GreaterEqual = 39  # >=
    OP_LeftShift = 40  # <<
    OP_RightShift = 41  # >>

    OP_Plus = 42  # +
    OP_PlusPlus = 43  # ++
    OP_Minus = 44  # -
    OP_MinusMinus = 45  # --
    OP_Star = 46  # *
    OP_Div = 47  # /
    OP_Mod = 48  # %

    OP_And = 49  # &
    OP_Or = 50  # |
    OP_AndAnd = 51  # &&
    OP_OrOr = 52  # ||
    OP_Caret = 53  # ^
    OP_Not = 54  # !
    OP_Tilde = 55  # ~

    OP_Question = 56  # ?
    OP_QuestionAssign = 57  # ?=
    OP_Colon = 58  # :
    OP_ColonColon = 59  # ::
    OP_Semi = 60  # ;
    OP_Comma = 61  # ,

    OP_Assign = 62  # =
    OP_StarAssign = 63  # *=
    OP_DivAssign = 64  # /=
    OP_ModAssign = 65  # %=
    OP_PlusAssign = 67  # +=
    OP_MinusAssign = 68  # -=
    OP_LeftShiftAssign = 69  # <<=
    OP_RightShiftAssign = 70  # >>=
    OP_AndAssign = 71  # &=
    OP_XorAssign = 72  # ^=
    OP_OrAssign = 73  # |=

    OP_Equal = 74  # ==
    OP_NotEqual = 75  # !=

    OP_Arrow = 76  # ->
    OP_Dot = 77  # .
    OP_Ellipsis = 78  # ...

    OP_Newline = 79  # (\r)?\n

    Literal_Integer = 80
    Literal_Float = 81
    Literal_Text = 82

    Identifier = 90
    WhiteSpace = 91
    Begin = 92
    End = 93
    Eof = 99


class Token:
    def __init__(self, kind, text=None, line=None, col=None):
        self.kind = kind
        self.text = text
        self.line = line
        self.col = col

    def __repr__(self):
        return f"{self.kind}"
