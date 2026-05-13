# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#program.
    def enterProgram(self, ctx:gramaticaParser.ProgramContext):
        pass

    # Exit a parse tree produced by gramaticaParser#program.
    def exitProgram(self, ctx:gramaticaParser.ProgramContext):
        pass


    # Enter a parse tree produced by gramaticaParser#statement.
    def enterStatement(self, ctx:gramaticaParser.StatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#statement.
    def exitStatement(self, ctx:gramaticaParser.StatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#processStmt.
    def enterProcessStmt(self, ctx:gramaticaParser.ProcessStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#processStmt.
    def exitProcessStmt(self, ctx:gramaticaParser.ProcessStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ifStmt.
    def enterIfStmt(self, ctx:gramaticaParser.IfStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ifStmt.
    def exitIfStmt(self, ctx:gramaticaParser.IfStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ifBlock.
    def enterIfBlock(self, ctx:gramaticaParser.IfBlockContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ifBlock.
    def exitIfBlock(self, ctx:gramaticaParser.IfBlockContext):
        pass


    # Enter a parse tree produced by gramaticaParser#elseBlock.
    def enterElseBlock(self, ctx:gramaticaParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by gramaticaParser#elseBlock.
    def exitElseBlock(self, ctx:gramaticaParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by gramaticaParser#showStmt.
    def enterShowStmt(self, ctx:gramaticaParser.ShowStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#showStmt.
    def exitShowStmt(self, ctx:gramaticaParser.ShowStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#condition.
    def enterCondition(self, ctx:gramaticaParser.ConditionContext):
        pass

    # Exit a parse tree produced by gramaticaParser#condition.
    def exitCondition(self, ctx:gramaticaParser.ConditionContext):
        pass


    # Enter a parse tree produced by gramaticaParser#expr.
    def enterExpr(self, ctx:gramaticaParser.ExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#expr.
    def exitExpr(self, ctx:gramaticaParser.ExprContext):
        pass


    # Enter a parse tree produced by gramaticaParser#comparator.
    def enterComparator(self, ctx:gramaticaParser.ComparatorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#comparator.
    def exitComparator(self, ctx:gramaticaParser.ComparatorContext):
        pass



del gramaticaParser