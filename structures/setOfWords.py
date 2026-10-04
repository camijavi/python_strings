from components import clearConsole, pauseConsole


def main():
    clearConsole()
    phraseValue = input("Ingrese una frase: ")
    wordsList = phraseValue.lower().split()
    uniqueWords = set(wordsList)

    print(f"Palabras únicas: {uniqueWords}")
    pauseConsole()


if __name__ == "__main__":
    main()
