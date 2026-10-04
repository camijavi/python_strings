from components import clearConsole, pauseConsole, printWarning


def main():
    clearConsole()
    identifierValue = input("Ingrese el identificador: ")
    cleanIdentifier = identifierValue.strip().replace(" ", "_").replace("-", "_")

    if not cleanIdentifier:
        printWarning("El identificador quedó vacío después de limpiar.")
    else:
        print(f"Identificador limpio: {cleanIdentifier}")

    pauseConsole()


if __name__ == "__main__":
    main()
