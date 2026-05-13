from antlr4.error.ErrorListener import ErrorListener


class CustomErrorListener(ErrorListener):
    def __init__(self, error_type):
        super().__init__()
        self.error_type = error_type
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = (
            f"Error {self.error_type} en línea {line}, columna {column}: {msg}"
        )
        self.errors.append(error_message)

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return self.errors