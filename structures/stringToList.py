from components import clearConsole, pauseConsole


def main():
    clearConsole()
    namesValue = input("Ingrese nombres separados por punto y coma (;): ")
    cleanNamesList = [nameValue.strip() for nameValue in namesValue.split(";") if nameValue.strip()]

    print("Lista de nombres:")
    for nameValue in cleanNamesList:
        print(nameValue)

    pauseConsole()


if __name__ == "__main__":
    main()