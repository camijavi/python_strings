from components import clearConsole, pauseConsole, printWarning, printSuccess


def main():
    clearConsole()
    emailValue = input("Ingrese un correo electrónico: ").strip()

    atPosition = emailValue.find("@")
    dotAfterAtPosition = emailValue.find(".", atPosition + 1) if atPosition != -1 else -1
    isValidBasicEmail = atPosition > 0 and dotAfterAtPosition > atPosition + 1

    if isValidBasicEmail:
        printSuccess("El correo cumple con la validación básica.")
    else:
        printWarning("El correo no cumple con la validación básica.")

    pauseConsole()


if __name__ == "__main__":
    main()