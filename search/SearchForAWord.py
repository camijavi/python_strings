from components import clearConsole, pauseConsole, printWarning


def main():
    clearConsole()
    phraseValue = input("Ingrese una frase: ")
    wordValue = input("Ingrese la palabra a buscar: ").strip()

    if not wordValue:
        printWarning("Debe ingresar una palabra válida.")
        pauseConsole()
        return

    startPosition = phraseValue.lower().find(wordValue.lower())
    wasFound = startPosition != -1

    print(f"¿La palabra aparece?: {wasFound}")
    if wasFound:
        print(f"Posición inicial: {startPosition}")

    pauseConsole()


if __name__ == "__main__":
    main()