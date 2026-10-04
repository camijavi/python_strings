import os
import subprocess
import sys
from components import clearConsole, pauseConsole, printError, printWarning

baseDirectory = os.path.dirname(os.path.abspath(__file__))

menuCategorias = {
    "1": {
        "titulo": "Operaciones Básicas",
        "programas": [
            {"nombre": "Caracteres en una cadena", "archivo": os.path.join("basics", "charactersInAString.py")},
            {"nombre": "Limpieza de identificador", "archivo": os.path.join("basics", "identifierCleaning.py")},
            {"nombre": "Solo números", "archivo": os.path.join("basics", "justNumbers.py")},
            {"nombre": "Mayúsculas y minúsculas", "archivo": os.path.join("basics", "uppercaseLowercaseLetters.py")},
            {"nombre": "Validar correo básico", "archivo": os.path.join("basics", "validateBasicEmail.py")},
        ],
    },
    "2": {
        "titulo": "Búsqueda y Verificación",
        "programas": [
            {"nombre": "Contar caracteres", "archivo": os.path.join("search", "countCharacters.py")},
            {"nombre": "Palíndromo", "archivo": os.path.join("search", "palindrome.py")},
            {"nombre": "Prefijo y extensión de archivo", "archivo": os.path.join("search", "prefix&Extension.py")},
            {"nombre": "Buscar una palabra", "archivo": os.path.join("search", "searchForAWord.py")},
        ],
    },
    "3": {
        "titulo": "Estructuras de Datos",
        "programas": [
            {"nombre": "Lista a cadena", "archivo": os.path.join("structures", "listToChain.py")},
            {"nombre": "Conjunto de palabras únicas", "archivo": os.path.join("structures", "setOfWords.py")},
            {"nombre": "Cadena a lista", "archivo": os.path.join("structures", "stringToList.py")},
            {"nombre": "Frecuencia de palabras", "archivo": os.path.join("structures", "wordsFrequency.py")},
        ],
    },
    "4": {
        "titulo": "Integración",
        "programas": [
            {"nombre": "Registro de configuración", "archivo": os.path.join("integration", "configurationLog.py")},
            {"nombre": "Limpieza y resumen de etiquetas", "archivo": os.path.join("integration", "labelCleaning&Summary.py")},
        ],
    },
    "5": {
        "titulo": "Ejercicios Resueltos",
        "programas": [
            {"nombre": "Construir un diccionario", "archivo": os.path.join("resolved", "buildADictionary.py")},
            {"nombre": "Contar palabras", "archivo": os.path.join("resolved", "countWords.py")},
            {"nombre": "Eliminar tecnologías redundantes", "archivo": os.path.join("resolved", "eliminateRedundantTechnologies.py")},
            {"nombre": "Normalizar un nombre", "archivo": os.path.join("resolved", "normalizeAName.py")},
            {"nombre": "Separar tecnologías", "archivo": os.path.join("resolved", "separateTechnologie.py")},
        ],
    },
}


def ejecutarPrograma(rutaRelativa):
    rutaCompleta = os.path.join(baseDirectory, rutaRelativa)
    if not os.path.isfile(rutaCompleta):
        printError(f"No se encontró el archivo: {rutaRelativa}")
        pauseConsole()
        return

    try:
        entornoEjecucion = os.environ.copy()
        pythonPathActual = entornoEjecucion.get("PYTHONPATH", "")
        entornoEjecucion["PYTHONPATH"] = (
            f"{baseDirectory}:{pythonPathActual}" if pythonPathActual else baseDirectory
        )
        subprocess.run([sys.executable, rutaCompleta], cwd=baseDirectory, env=entornoEjecucion)
    except KeyboardInterrupt:
        print("\nEjecución cancelada por el usuario.")
        pauseConsole()
    except Exception as errorEjecucion:
        printError(f"Error al ejecutar el programa: {errorEjecucion}")
        pauseConsole()


def gestionarSubmenu(claveCategoria):
    datosCategoria = menuCategorias[claveCategoria]
    tituloCategoria = datosCategoria["titulo"]
    listaProgramas = datosCategoria["programas"]

    while True:
        clearConsole()
        print("=" * 55)
        print(f"   MENÚ: {tituloCategoria.upper()}")
        print("=" * 55)
        for indice, itemPrograma in enumerate(listaProgramas, start=1):
            print(f" {indice}. {itemPrograma['nombre']}")
        print(" 0. Volver al menú principal")
        print("=" * 55)

        try:
            opcionSeleccionada = input("Seleccione una opción: ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if opcionSeleccionada == "0":
            break

        if opcionSeleccionada.isdigit():
            numeroOpcion = int(opcionSeleccionada)
            if 1 <= numeroOpcion <= len(listaProgramas):
                programaSeleccionado = listaProgramas[numeroOpcion - 1]
                ejecutarPrograma(programaSeleccionado["archivo"])
                continue

        printWarning("Opción no válida. Intente nuevamente.")
        pauseConsole()


def iniciarMenu():
    while True:
        clearConsole()
        print("=" * 55)
        print("   MENÚ PRINCIPAL - EJERCICIOS DE PYTHON STRINGS")
        print("=" * 55)
        for claveOpcion, categoria in menuCategorias.items():
            print(f" {claveOpcion}. {categoria['titulo']}")
        print(" 0. Salir")
        print("=" * 55)

        try:
            opcionPrincipal = input("Seleccione una opción: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n")
            break

        if opcionPrincipal == "0":
            clearConsole()
            print("¡Gracias por usar el sistema! Hasta pronto.\n")
            break

        if opcionPrincipal in menuCategorias:
            gestionarSubmenu(opcionPrincipal)
        else:
            printWarning("Opción no válida. Intente nuevamente.")
            pauseConsole()


if __name__ == "__main__":
    iniciarMenu()
