# Generated from DaoParser.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DaoParser import DaoParser
else:
    from DaoParser import DaoParser

# This class defines a complete generic visitor for a parse tree produced by DaoParser.

class DaoParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DaoParser#fileInput.
    def visitFileInput(self, ctx:DaoParser.FileInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#statement.
    def visitStatement(self, ctx:DaoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#varDeclaration.
    def visitVarDeclaration(self, ctx:DaoParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#varDeclarationSpecifier.
    def visitVarDeclarationSpecifier(self, ctx:DaoParser.VarDeclarationSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#expression.
    def visitExpression(self, ctx:DaoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:DaoParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:DaoParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#conditionalExpression.
    def visitConditionalExpression(self, ctx:DaoParser.ConditionalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:DaoParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#logicalAndExprression.
    def visitLogicalAndExprression(self, ctx:DaoParser.LogicalAndExprressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#inclusiveOrExprression.
    def visitInclusiveOrExprression(self, ctx:DaoParser.InclusiveOrExprressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#exclusiveOrExprression.
    def visitExclusiveOrExprression(self, ctx:DaoParser.ExclusiveOrExprressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#andExprression.
    def visitAndExprression(self, ctx:DaoParser.AndExprressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#relationalExprression.
    def visitRelationalExprression(self, ctx:DaoParser.RelationalExprressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#relationalOperator.
    def visitRelationalOperator(self, ctx:DaoParser.RelationalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#shiftExpression.
    def visitShiftExpression(self, ctx:DaoParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:DaoParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:DaoParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#castExpression.
    def visitCastExpression(self, ctx:DaoParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#unaryExpression.
    def visitUnaryExpression(self, ctx:DaoParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#unaryOperator.
    def visitUnaryOperator(self, ctx:DaoParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#postfixExpression.
    def visitPostfixExpression(self, ctx:DaoParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:DaoParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#constantExpression.
    def visitConstantExpression(self, ctx:DaoParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#argumentExpressionList.
    def visitArgumentExpressionList(self, ctx:DaoParser.ArgumentExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#identifier.
    def visitIdentifier(self, ctx:DaoParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#dotName.
    def visitDotName(self, ctx:DaoParser.DotNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#typeName.
    def visitTypeName(self, ctx:DaoParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DaoParser#funcName.
    def visitFuncName(self, ctx:DaoParser.FuncNameContext):
        return self.visitChildren(ctx)



del DaoParser