from components import clearConsole, pauseConsole, printWarning


def main():
    clearConsole()
    textValue = input("Ingrese un texto: ")
    characterValue = input("Ingrese un carácter a buscar: ").strip()

    if len(characterValue) != 1:
        printWarning("Debe ingresar exactamente un carácter.")
        pauseConsole()
        return

    countValue = textValue.lower().count(characterValue.lower())
    print(f"El carácter '{characterValue}' aparece {countValue} veces.")
    pauseConsole()


if __name__ == "__main__":
    main()