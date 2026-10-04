from components import clearConsole, pauseConsole, printWarning


def main():
    clearConsole()
    nameValue = input("Ingrese un nombre: ")
    cleanName = nameValue.strip()

    if not cleanName:
        printWarning("No ingresaste un nombre válido.")
        pauseConsole()
        return

    normalizedName = cleanName.title()
    print(f"Nombre normalizado: {normalizedName}")
    pauseConsole()


if __name__ == "__main__":
    main()
