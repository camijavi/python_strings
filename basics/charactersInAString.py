from components import clearConsole, pauseConsole, printWarning


def main():
    clearConsole()
    textValue = input("Ingrese un texto: ").strip()

    if not textValue:
        printWarning("No ingresaste un texto válido.")
        pauseConsole()
        return

    firstCharacter = textValue[0]
    lastCharacter = textValue[-1]
    textLength = len(textValue)
    reversedText = textValue[::-1]

    print(f"Primer carácter: {firstCharacter}")
    print(f"Último carácter: {lastCharacter}")
    print(f"Longitud: {textLength}")
    print(f"Texto invertido: {reversedText}")
    pauseConsole()


if __name__ == "__main__":
    main()