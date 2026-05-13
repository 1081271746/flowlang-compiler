import sys
import subprocess
from antlr4 import *

sys.path.append("generated")

from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from semantic_analyzer.semantic_analyzer import SemanticAnalyzer
from codegen.ir_generator import IRGenerator
from codegen.python_generator import PythonGenerator
from errors.custom_error_listener import CustomErrorListener


def main():
    try:
        input_stream = FileStream("input.txt", encoding="utf-8")

        # Listener para errores lexicos
        lexer_error_listener = CustomErrorListener("lexico")

        # Fase lexica
        lexer = gramaticaLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(lexer_error_listener)

        token_stream = CommonTokenStream(lexer)

        # Listener para errores sintacticos
        parser_error_listener = CustomErrorListener("sintactico")

        # Fase sintactica
        parser = gramaticaParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(parser_error_listener)

        tree = parser.program()

        # Validar errores lexicos
        if lexer_error_listener.has_errors():
            print("[ERROR] Errores lexicos encontrados:")
            for error in lexer_error_listener.get_errors():
                print(error)
            return

        print("[OK] Analisis lexico completado")

        # Validar errores sintacticos
        if parser_error_listener.has_errors():
            print("\n[ERROR] Errores sintacticos encontrados:")
            for error in parser_error_listener.get_errors():
                print(error)
            return

        print("[OK] Analisis sintactico completado")

        # Fase semantica
        semantic_analyzer = SemanticAnalyzer()
        semantic_errors = semantic_analyzer.visit(tree)

        if semantic_errors:
            print("\n[ERROR] Errores semanticos encontrados:")
            for error in semantic_errors:
                print(error)
            return

        print("[OK] Analisis semantico completado")

        print("\nTabla de simbolos:")
        for name, info in semantic_analyzer.symbol_table.get_all().items():
            print(f" - {name}: {info}")

        # Generacion de codigo intermedio
        ir_generator = IRGenerator()
        ir_code = ir_generator.visit(tree)

        print("\n[OK] Codigo intermedio generado:")
        for instruction in ir_code:
            print(instruction)

        # Generacion de codigo Python
        python_generator = PythonGenerator()
        python_code = python_generator.generate(ir_code)

        with open("output_program.py", "w", encoding="utf-8") as file:
            file.write(python_code)

        print("\n[OK] Codigo Python generado en output_program.py")
        print("\nCodigo Python generado:")
        print(python_code)

        # Ejecutar el programa Python generado
        result = subprocess.run(
            [sys.executable, "output_program.py"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )

        with open("output.txt", "w", encoding="utf-8") as file:
            file.write("=== CODIGO PYTHON GENERADO ===\n")
            file.write(python_code)
            file.write("\n\n=== SALIDA DEL PROGRAMA ===\n")
            file.write(result.stdout)

            if result.stderr:
                file.write("\n=== ERRORES DE EJECUCION ===\n")
                file.write(result.stderr)

        print("\n[OK] Programa Python ejecutado")
        print("Salida:")
        print(result.stdout)

        print("[OK] Resultado guardado en output.txt")

    except Exception as e:
        print("[ERROR] Error durante la compilacion")
        print(e)


if __name__ == "__main__":
    main()