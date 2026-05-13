import os
import subprocess
import sys


VALID_TESTS_DIR = "tests/valid"
INVALID_TESTS_DIR = "tests/invalid"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def get_test_files(folder):
    files = []

    if not os.path.exists(folder):
        return files

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            files.append(os.path.join(folder, filename))

    return sorted(files)


def run_test(test_path):
    """
    Copia el contenido de una prueba en input.txt y ejecuta main.py.
    """
    test_content = read_file(test_path)
    write_file(INPUT_FILE, test_content)

    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    return result.stdout, result.stderr


def extract_error_type(stdout):
    """
    Detecta el tipo de error reportado por main.py.
    """
    if "[ERROR] Errores lexicos encontrados:" in stdout:
        return "lexico"

    if "[ERROR] Errores sintacticos encontrados:" in stdout:
        return "sintactico"

    if "[ERROR] Errores semanticos encontrados:" in stdout:
        return "semantico"

    return "no detectado"


def extract_error_message(stdout):
    """
    Extrae una linea representativa del error.
    """
    lines = stdout.splitlines()

    for line in lines:
        clean_line = line.strip()

        if clean_line.startswith("Error "):
            return clean_line

    return "No se encontro mensaje especifico de error."


def extract_program_output(stdout):
    """
    Extrae la salida del programa generado despues de la palabra 'Salida:'.
    """
    lines = stdout.splitlines()

    for index, line in enumerate(lines):
        if line.strip() == "Salida:":
            if index + 1 < len(lines):
                next_line = lines[index + 1].strip()

                if next_line:
                    return next_line

            return "Sin salida visible"

    return "No ejecutado"


def valid_test_passed(stdout, stderr):
    """
    Una prueba valida aprueba si genera codigo Python,
    no reporta errores y no hay errores internos.
    """
    return (
        "[OK] Codigo Python generado en output_program.py" in stdout
        and "[ERROR]" not in stdout
        and stderr.strip() == ""
    )


def invalid_test_passed(stdout):
    """
    Una prueba invalida aprueba si el compilador detecta
    error lexico, sintactico o semantico.
    """
    return (
        "[ERROR] Errores lexicos encontrados:" in stdout
        or "[ERROR] Errores sintacticos encontrados:" in stdout
        or "[ERROR] Errores semanticos encontrados:" in stdout
    )


def add_separator(report, char="=", size=60):
    report.append(char * size)


def add_valid_result(report, test_name, status, stdout, stderr):
    report.append(f"--- {test_name} ---")
    report.append("Estado esperado : VALIDA")
    report.append(f"Resultado       : {status}")

    if status == "APROBADA":
        report.append("Fases ejecutadas: Lexico, Sintactico, Semantico, IR, Python")
        report.append("Archivo Python  : output_program.py")
        report.append(f"Salida programa : {extract_program_output(stdout)}")
    else:
        report.append("Detalle         : La prueba valida no completo todas las fases.")

    if stderr.strip():
        report.append("Errores internos:")
        report.append(stderr.strip())

    report.append("")


def add_invalid_result(report, test_name, status, stdout, stderr):
    report.append(f"--- {test_name} ---")
    report.append("Estado esperado : INVALIDA")
    report.append(f"Resultado       : {status}")

    if status == "APROBADA":
        report.append(f"Error detectado : {extract_error_type(stdout)}")
        report.append(f"Mensaje         : {extract_error_message(stdout)}")
    else:
        report.append("Detalle         : La prueba invalida no fue detectada como error.")

    if stderr.strip():
        report.append("Errores internos:")
        report.append(stderr.strip())

    report.append("")


def main():
    report = []
    total_tests = 0
    passed_tests = 0
    failed_tests = 0

    add_separator(report)
    report.append("FLOWLANG COMPILER - REPORTE AUTOMATICO DE PRUEBAS")
    add_separator(report)
    report.append("")

    # ==============================
    # PRUEBAS VALIDAS
    # ==============================
    report.append("[1] PRUEBAS VALIDAS")
    add_separator(report, "-")

    valid_tests = get_test_files(VALID_TESTS_DIR)

    for test_path in valid_tests:
        total_tests += 1
        test_name = os.path.basename(test_path)

        stdout, stderr = run_test(test_path)

        if valid_test_passed(stdout, stderr):
            passed_tests += 1
            status = "APROBADA"
        else:
            failed_tests += 1
            status = "FALLO"

        add_valid_result(report, test_name, status, stdout, stderr)

    # ==============================
    # PRUEBAS INVALIDAS
    # ==============================
    report.append("[2] PRUEBAS INVALIDAS")
    add_separator(report, "-")

    invalid_tests = get_test_files(INVALID_TESTS_DIR)

    for test_path in invalid_tests:
        total_tests += 1
        test_name = os.path.basename(test_path)

        stdout, stderr = run_test(test_path)

        if invalid_test_passed(stdout):
            passed_tests += 1
            status = "APROBADA"
        else:
            failed_tests += 1
            status = "FALLO"

        add_invalid_result(report, test_name, status, stdout, stderr)

    # ==============================
    # RESUMEN FINAL
    # ==============================
    add_separator(report)
    report.append("RESUMEN FINAL")
    add_separator(report)
    report.append(f"Total de pruebas    : {total_tests}")
    report.append(f"Pruebas aprobadas   : {passed_tests}")
    report.append(f"Pruebas fallidas    : {failed_tests}")
    report.append(f"Archivo generado    : {OUTPUT_FILE}")

    final_report = "\n".join(report)

    write_file(OUTPUT_FILE, final_report)

    print(final_report)


if __name__ == "__main__":
    main()