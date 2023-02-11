parser grammar DaoParser;

options { tokenVocab=DaoLexer; language=Python3; }

fileInput
    : statement* EOF
    ;

statement
    : expression? Newline
    | varDeclaration
    ;

varDeclaration
    : varDeclarationSpecifier Newline
    ;

varDeclarationSpecifier
    : typeName identifier ('=' expression)?
    | varDeclarationSpecifier ',' identifier ('=' expression)?
    ;

expression
    : assignmentExpression
    ;

assignmentExpression
    : conditionalExpression
    | unaryExpression assignmentOperator assignmentExpression
    ;

assignmentOperator
    : '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|='
    ;

conditionalExpression
    : logicalOrExpression ('?' expression ':' conditionalExpression)?
    ;

logicalOrExpression
    : logicalAndExprression
    | logicalOrExpression '||' logicalAndExprression
    ;

logicalAndExprression
    : inclusiveOrExprression
    | logicalAndExprression '&&' inclusiveOrExprression
    ;

inclusiveOrExprression
    : exclusiveOrExprression
    | inclusiveOrExprression '|' exclusiveOrExprression
    ;

exclusiveOrExprression
    : andExprression ('^' andExprression)*
    ;

andExprression
    : relationalExprression
    | andExprression '&' relationalExprression
    ;

relationalExprression
    : shiftExpression (relationalOperator shiftExpression)*
    ;

relationalOperator
    : '==' | '!=' | '<' | '>' | '<=' | '>='
    ;

shiftExpression
    : additiveExpression
    | shiftExpression op=('<<'|'>>') additiveExpression
    ;

additiveExpression
    : multiplicativeExpression
    | additiveExpression op=('+'|'-') multiplicativeExpression
    ;

multiplicativeExpression
    : castExpression
    | multiplicativeExpression op=('*'|'/'|'%') castExpression
    ;

castExpression
    : '(' typeName ')' castExpression
    | unaryExpression
    ;

unaryExpression
    : ('++'| '--')* (postfixExpression | unaryOperator castExpression)
    ;

unaryOperator
    : '&' | '*' | '+' | '-' | '~' | '!'
    ;

postfixExpression
    : primaryExpression
    | postfixExpression ('[' expression ']' | '(' argumentExpressionList? ')' | ('.' | '->') identifier | ('++' | '--'))
    ;

primaryExpression
    : identifier
    | StringLiteral
    | IntegerLiteral
    | FloatLiteral
    | TrueLiteral
    | FalseLiteral
    | NullLiteral
    | '(' expression ')'
    ;

constantExpression
    : conditionalExpression
    ;

argumentExpressionList
    : assignmentExpression (',' assignmentExpression)*
    ;

identifier
    : Identifier
    ;

dotName
    : identifier ('.' identifier)*
    ;

typeName
    : dotName
    | Byte
    | Int16
    | Int32
    | Int64
    | UInt16
    | UInt32
    | UInt64
    | Half
    | Float
    | Double
    | Bool
    | Text
    ;

funcName
    : (dotName '::')? identifier
    ;