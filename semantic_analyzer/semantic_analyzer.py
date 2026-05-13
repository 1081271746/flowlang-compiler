from antlr4.tree.Tree import TerminalNodeImpl

from generated.gramaticaVisitor import gramaticaVisitor
from generated.gramaticaParser import gramaticaParser
from semantic_analyzer.symbol_table import SymbolTable


class SemanticAnalyzer(gramaticaVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []

    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)

        return self.errors

    def visitProcessStmt(self, ctx):
        variable_name = ctx.ID().getText()

        # Primero revisamos si la expresion usa variables no definidas
        self.check_expr(ctx.expr())

        # Despues registramos la variable creada
        self.symbol_table.define(variable_name)

    def visitShowStmt(self, ctx):
        self.check_expr(ctx.expr())

    def visitIfStmt(self, ctx):
        # Revisar condicion del Si
        self.check_condition(ctx.condition())

        # Revisar bloque del Si
        for statement in ctx.ifBlock().statement():
            self.visit(statement)

        # Revisar bloque del Sino
        for statement in ctx.elseBlock().statement():
            self.visit(statement)

    def check_condition(self, ctx):
        self.check_expr(ctx.expr(0))
        self.check_expr(ctx.expr(1))

    def check_expr(self, ctx):
        """
        Revisa todos los identificadores dentro de una expresion.
        Detecta casos como:
        x
        x + 1
        (x + y) * 4
        """

        ids_found = self.find_ids(ctx)

        for token in ids_found:
            variable_name = token.getText()

            if not self.symbol_table.exists(variable_name):
                line = token.symbol.line
                column = token.symbol.column

                error_message = (
                    f"Error semantico en linea {line}, columna {column}: "
                    f"variable '{variable_name}' no definida."
                )

                if error_message not in self.errors:
                    self.errors.append(error_message)

    def find_ids(self, node):
        """
        Recorre recursivamente el arbol de la expresion
        y devuelve todos los tokens ID encontrados.
        """
        ids = []

        if isinstance(node, TerminalNodeImpl):
            if node.symbol.type == gramaticaParser.ID:
                ids.append(node)
            return ids

        for i in range(node.getChildCount()):
            child = node.getChild(i)
            ids.extend(self.find_ids(child))

        return ids