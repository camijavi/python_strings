from components import clearConsole, pauseConsole


def main():
    clearConsole()
    sentenceValue = input("Ingrese una oración: ").lower().strip()
    wordsList = sentenceValue.split()
    wordsCount = {}

    for wordValue in wordsList:
        currentCount = wordsCount.get(wordValue, 0)
        wordsCount[wordValue] = currentCount + 1

    print(f"Frecuencia de palabras: {wordsCount}")
    pauseConsole()


if __name__ == "__main__":
    main()