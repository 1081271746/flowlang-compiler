# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#program.
    def visitProgram(self, ctx:gramaticaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#statement.
    def visitStatement(self, ctx:gramaticaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#processStmt.
    def visitProcessStmt(self, ctx:gramaticaParser.ProcessStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ifStmt.
    def visitIfStmt(self, ctx:gramaticaParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ifBlock.
    def visitIfBlock(self, ctx:gramaticaParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#elseBlock.
    def visitElseBlock(self, ctx:gramaticaParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#showStmt.
    def visitShowStmt(self, ctx:gramaticaParser.ShowStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#condition.
    def visitCondition(self, ctx:gramaticaParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#expr.
    def visitExpr(self, ctx:gramaticaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#comparator.
    def visitComparator(self, ctx:gramaticaParser.ComparatorContext):
        return self.visitChildren(ctx)



del gramaticaParser