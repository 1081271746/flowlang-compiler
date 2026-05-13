# Generated from gramatica.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,96,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,9,
        0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,5,4,55,8,4,10,4,12,4,
        58,9,4,1,5,5,5,61,8,5,10,5,12,5,64,9,5,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,81,8,8,1,8,1,8,1,8,1,8,1,8,
        1,8,5,8,89,8,8,10,8,12,8,92,9,8,1,9,1,9,1,9,0,1,16,10,0,2,4,6,8,
        10,12,14,16,18,0,3,1,0,16,17,1,0,14,15,1,0,8,13,94,0,20,1,0,0,0,
        2,35,1,0,0,0,4,37,1,0,0,0,6,43,1,0,0,0,8,56,1,0,0,0,10,62,1,0,0,
        0,12,65,1,0,0,0,14,69,1,0,0,0,16,80,1,0,0,0,18,93,1,0,0,0,20,21,
        5,1,0,0,21,25,5,19,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,
        25,23,1,0,0,0,25,26,1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,
        3,0,0,29,30,5,19,0,0,30,31,5,0,0,1,31,1,1,0,0,0,32,36,3,4,2,0,33,
        36,3,6,3,0,34,36,3,12,6,0,35,32,1,0,0,0,35,33,1,0,0,0,35,34,1,0,
        0,0,36,3,1,0,0,0,37,38,5,4,0,0,38,39,5,22,0,0,39,40,5,18,0,0,40,
        41,3,16,8,0,41,42,5,19,0,0,42,5,1,0,0,0,43,44,5,5,0,0,44,45,3,14,
        7,0,45,46,5,18,0,0,46,47,3,8,4,0,47,48,5,6,0,0,48,49,5,18,0,0,49,
        50,3,10,5,0,50,51,5,2,0,0,51,52,5,19,0,0,52,7,1,0,0,0,53,55,3,2,
        1,0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,9,
        1,0,0,0,58,56,1,0,0,0,59,61,3,2,1,0,60,59,1,0,0,0,61,64,1,0,0,0,
        62,60,1,0,0,0,62,63,1,0,0,0,63,11,1,0,0,0,64,62,1,0,0,0,65,66,5,
        7,0,0,66,67,3,16,8,0,67,68,5,19,0,0,68,13,1,0,0,0,69,70,3,16,8,0,
        70,71,3,18,9,0,71,72,3,16,8,0,72,15,1,0,0,0,73,74,6,8,-1,0,74,81,
        5,23,0,0,75,81,5,22,0,0,76,77,5,20,0,0,77,78,3,16,8,0,78,79,5,21,
        0,0,79,81,1,0,0,0,80,73,1,0,0,0,80,75,1,0,0,0,80,76,1,0,0,0,81,90,
        1,0,0,0,82,83,10,5,0,0,83,84,7,0,0,0,84,89,3,16,8,6,85,86,10,4,0,
        0,86,87,7,1,0,0,87,89,3,16,8,5,88,82,1,0,0,0,88,85,1,0,0,0,89,92,
        1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,17,1,0,0,0,92,90,1,0,0,0,
        93,94,7,2,0,0,94,19,1,0,0,0,7,25,35,56,62,80,88,90
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Inicio'", "'FinSi'", "'Fin'", "'Proceso'", 
                     "'Si'", "'Sino'", "'Mostrar'", "'>='", "'<='", "'=='", 
                     "'!='", "'>'", "'<'", "'+'", "'-'", "'*'", "'/'", "':'", 
                     "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INICIO", "FINSI", "FIN", "PROCESO", 
                      "SI", "SINO", "MOSTRAR", "MAYORIGUAL", "MENORIGUAL", 
                      "IGUAL", "DIFERENTE", "MAYOR", "MENOR", "SUMA", "RESTA", 
                      "MULT", "DIV", "DOSPUNTOS", "PUNTOYCOMA", "LPAREN", 
                      "RPAREN", "ID", "NUMBER", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_processStmt = 2
    RULE_ifStmt = 3
    RULE_ifBlock = 4
    RULE_elseBlock = 5
    RULE_showStmt = 6
    RULE_condition = 7
    RULE_expr = 8
    RULE_comparator = 9

    ruleNames =  [ "program", "statement", "processStmt", "ifStmt", "ifBlock", 
                   "elseBlock", "showStmt", "condition", "expr", "comparator" ]

    EOF = Token.EOF
    INICIO=1
    FINSI=2
    FIN=3
    PROCESO=4
    SI=5
    SINO=6
    MOSTRAR=7
    MAYORIGUAL=8
    MENORIGUAL=9
    IGUAL=10
    DIFERENTE=11
    MAYOR=12
    MENOR=13
    SUMA=14
    RESTA=15
    MULT=16
    DIV=17
    DOSPUNTOS=18
    PUNTOYCOMA=19
    LPAREN=20
    RPAREN=21
    ID=22
    NUMBER=23
    WS=24
    COMMENT=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIO(self):
            return self.getToken(gramaticaParser.INICIO, 0)

        def PUNTOYCOMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.PUNTOYCOMA)
            else:
                return self.getToken(gramaticaParser.PUNTOYCOMA, i)

        def FIN(self):
            return self.getToken(gramaticaParser.FIN, 0)

        def EOF(self):
            return self.getToken(gramaticaParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = gramaticaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(gramaticaParser.INICIO)
            self.state = 21
            self.match(gramaticaParser.PUNTOYCOMA)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 176) != 0):
                self.state = 22
                self.statement()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(gramaticaParser.FIN)
            self.state = 29
            self.match(gramaticaParser.PUNTOYCOMA)
            self.state = 30
            self.match(gramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def processStmt(self):
            return self.getTypedRuleContext(gramaticaParser.ProcessStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(gramaticaParser.IfStmtContext,0)


        def showStmt(self):
            return self.getTypedRuleContext(gramaticaParser.ShowStmtContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = gramaticaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.processStmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.ifStmt()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.showStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcessStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCESO(self):
            return self.getToken(gramaticaParser.PROCESO, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def DOSPUNTOS(self):
            return self.getToken(gramaticaParser.DOSPUNTOS, 0)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(gramaticaParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_processStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcessStmt" ):
                listener.enterProcessStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcessStmt" ):
                listener.exitProcessStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcessStmt" ):
                return visitor.visitProcessStmt(self)
            else:
                return visitor.visitChildren(self)




    def processStmt(self):

        localctx = gramaticaParser.ProcessStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_processStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(gramaticaParser.PROCESO)
            self.state = 38
            self.match(gramaticaParser.ID)
            self.state = 39
            self.match(gramaticaParser.DOSPUNTOS)
            self.state = 40
            self.expr(0)
            self.state = 41
            self.match(gramaticaParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(gramaticaParser.SI, 0)

        def condition(self):
            return self.getTypedRuleContext(gramaticaParser.ConditionContext,0)


        def DOSPUNTOS(self, i:int=None):
            if i is None:
                return self.getTokens(gramaticaParser.DOSPUNTOS)
            else:
                return self.getToken(gramaticaParser.DOSPUNTOS, i)

        def ifBlock(self):
            return self.getTypedRuleContext(gramaticaParser.IfBlockContext,0)


        def SINO(self):
            return self.getToken(gramaticaParser.SINO, 0)

        def elseBlock(self):
            return self.getTypedRuleContext(gramaticaParser.ElseBlockContext,0)


        def FINSI(self):
            return self.getToken(gramaticaParser.FINSI, 0)

        def PUNTOYCOMA(self):
            return self.getToken(gramaticaParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = gramaticaParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(gramaticaParser.SI)
            self.state = 44
            self.condition()
            self.state = 45
            self.match(gramaticaParser.DOSPUNTOS)
            self.state = 46
            self.ifBlock()
            self.state = 47
            self.match(gramaticaParser.SINO)
            self.state = 48
            self.match(gramaticaParser.DOSPUNTOS)
            self.state = 49
            self.elseBlock()
            self.state = 50
            self.match(gramaticaParser.FINSI)
            self.state = 51
            self.match(gramaticaParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_ifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def ifBlock(self):

        localctx = gramaticaParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 176) != 0):
                self.state = 53
                self.statement()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_elseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBlock" ):
                listener.enterElseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBlock" ):
                listener.exitElseBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBlock" ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = gramaticaParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 176) != 0):
                self.state = 59
                self.statement()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOSTRAR(self):
            return self.getToken(gramaticaParser.MOSTRAR, 0)

        def expr(self):
            return self.getTypedRuleContext(gramaticaParser.ExprContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(gramaticaParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_showStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShowStmt" ):
                listener.enterShowStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShowStmt" ):
                listener.exitShowStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowStmt" ):
                return visitor.visitShowStmt(self)
            else:
                return visitor.visitChildren(self)




    def showStmt(self):

        localctx = gramaticaParser.ShowStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_showStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(gramaticaParser.MOSTRAR)
            self.state = 66
            self.expr(0)
            self.state = 67
            self.match(gramaticaParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExprContext,i)


        def comparator(self):
            return self.getTypedRuleContext(gramaticaParser.ComparatorContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = gramaticaParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.expr(0)
            self.state = 70
            self.comparator()
            self.state = 71
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def NUMBER(self):
            return self.getToken(gramaticaParser.NUMBER, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(gramaticaParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(gramaticaParser.RPAREN, 0)

        def MULT(self):
            return self.getToken(gramaticaParser.MULT, 0)

        def DIV(self):
            return self.getToken(gramaticaParser.DIV, 0)

        def SUMA(self):
            return self.getToken(gramaticaParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(gramaticaParser.RESTA, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 74
                self.match(gramaticaParser.NUMBER)
                pass
            elif token in [22]:
                self.state = 75
                self.match(gramaticaParser.ID)
                pass
            elif token in [20]:
                self.state = 76
                self.match(gramaticaParser.LPAREN)
                self.state = 77
                self.expr(0)
                self.state = 78
                self.match(gramaticaParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 88
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 82
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 83
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 84
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 86
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 87
                        self.expr(5)
                        pass

             
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAYORIGUAL(self):
            return self.getToken(gramaticaParser.MAYORIGUAL, 0)

        def MENORIGUAL(self):
            return self.getToken(gramaticaParser.MENORIGUAL, 0)

        def IGUAL(self):
            return self.getToken(gramaticaParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(gramaticaParser.DIFERENTE, 0)

        def MAYOR(self):
            return self.getToken(gramaticaParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(gramaticaParser.MENOR, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = gramaticaParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




