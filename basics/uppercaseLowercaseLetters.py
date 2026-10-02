from components import clearConsole, pauseConsole, printWarning


def main():
    clearConsole()
    textValue = input("Ingrese un texto: ").strip()

    if not textValue:
        printWarning("No ingresaste un texto válido.")
        pauseConsole()
        return

    upperText = textValue.upper()
    lowerText = textValue.lower()
    titleText = textValue.title()

    print(f"Mayúsculas: {upperText}")
    print(f"Minúsculas: {lowerText}")
    print(f"Formato título: {titleText}")
    pauseConsole()


if __name__ == "__main__":
    main()