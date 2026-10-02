from components import clearConsole, pauseConsole, printSuccess, printWarning


def main():
    clearConsole()
    textValue = input("Ingrese una palabra o frase: ")
    normalizedText = textValue.replace(" ", "").lower()
    reversedText = normalizedText[::-1]
    isPalindrome = normalizedText == reversedText and normalizedText != ""

    if isPalindrome:
        printSuccess("Es un palíndromo.")
    else:
        printWarning("No es un palíndromo.")

    pauseConsole()


if __name__ == "__main__":
    main()