from components import clearConsole, pauseConsole


def main():
    clearConsole()
    tagsValue = input("Ingrese etiquetas separadas por coma: ")
    cleanTagsSet = {
        tagValue.strip().lower()
        for tagValue in tagsValue.split(",")
        if tagValue.strip()
    }
    orderedTagsList = sorted(cleanTagsSet)
    tagsSummary = "|".join(orderedTagsList)

    print(f"Resumen de etiquetas: {tagsSummary}")
    pauseConsole()


if __name__ == "__main__":
    main()