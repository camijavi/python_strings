from components import clearConsole, pauseConsole


def main():
    clearConsole()
    fileName = input("Ingrese el nombre del archivo: ").strip().lower()

    hasCsvExtension = fileName.endswith(".csv")
    startsWithReport = fileName.startswith("report")

    print(f"¿Termina en .csv?: {hasCsvExtension}")
    print(f"¿Comienza con 'report'?: {startsWithReport}")
    pauseConsole()


if __name__ == "__main__":
    main()