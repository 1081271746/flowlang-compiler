class PythonGenerator:
    def __init__(self):
        self.lines = []
        self.indent_level = 0

    def generate(self, ir_code):
        """
        Recibe el código intermedio IR y lo transforma a código Python.
        """
        self.lines = []
        self.indent_level = 0

        for instruction in ir_code:
            op = instruction["op"]

            if op == "ASSIGN":
                self.emit(f"{instruction['target']} = {instruction['value']}")

            elif op == "PRINT":
                self.emit(f"print({instruction['value']})")

            elif op == "IF":
                self.emit(f"if {instruction['condition']}:")

            elif op == "BEGIN_IF":
                self.indent_level += 1

            elif op == "ELSE":
                self.indent_level -= 1
                self.emit("else:")
                self.indent_level += 1

            elif op == "END_IF":
                self.indent_level -= 1

        return "\n".join(self.lines)

    def emit(self, line):
        """
        Agrega una línea de código con la indentación correcta.
        """
        indentation = "    " * self.indent_level
        self.lines.append(indentation + line)