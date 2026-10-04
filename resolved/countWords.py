from components import clearConsole, pauseConsole


def main():
    clearConsole()
    sentenceValue = input("Ingrese una oración: ").strip()
    wordsList = sentenceValue.split()
    wordsCount = len(wordsList)

    print(f"La oración contiene {wordsCount} palabra(s).")
    pauseConsole()


if __name__ == "__main__":
    main()