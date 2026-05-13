from generated.gramaticaVisitor import gramaticaVisitor


class IRGenerator(gramaticaVisitor):
    def __init__(self):
        self.instructions = []

    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)

        return self.instructions

    def visitProcessStmt(self, ctx):
        variable_name = ctx.ID().getText()
        expression = self.expr_to_text(ctx.expr())

        self.instructions.append({
            "op": "ASSIGN",
            "target": variable_name,
            "value": expression
        })

    def visitShowStmt(self, ctx):
        expression = self.expr_to_text(ctx.expr())

        self.instructions.append({
            "op": "PRINT",
            "value": expression
        })

    def visitIfStmt(self, ctx):
        condition = self.condition_to_text(ctx.condition())

        self.instructions.append({
            "op": "IF",
            "condition": condition
        })

        self.instructions.append({
            "op": "BEGIN_IF"
        })

        # Bloque del Si
        for statement in ctx.ifBlock().statement():
            self.visit(statement)

        self.instructions.append({
            "op": "ELSE"
        })

        # Bloque del Sino
        for statement in ctx.elseBlock().statement():
            self.visit(statement)

        self.instructions.append({
            "op": "END_IF"
        })

    def condition_to_text(self, ctx):
        left = self.expr_to_text(ctx.expr(0))
        comparator = ctx.comparator().getText()
        right = self.expr_to_text(ctx.expr(1))

        return f"{left} {comparator} {right}"

    def expr_to_text(self, ctx):
        return ctx.getText()