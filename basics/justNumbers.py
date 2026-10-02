from components import clearConsole, pauseConsole, printWarning, printSuccess


def main():
    clearConsole()
    codeValue = input("Ingrese un código: ").strip()

    if codeValue.isdigit():
        numberValue = int(codeValue)
        printSuccess(f"El código contiene solo dígitos. Entero convertido: {numberValue}")
    else:
        printWarning("El código no contiene solo dígitos.")

    pauseConsole()


if __name__ == "__main__":
    main()