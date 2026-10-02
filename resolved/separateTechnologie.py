from components import clearConsole, pauseConsole


def main():
    clearConsole()
    technologiesValue = input("Ingrese tecnologías separadas por coma: ")
    technologiesList = [
        technologyValue.strip()
        for technologyValue in technologiesValue.split(",")
        if technologyValue.strip()
    ]

    print(f"Lista limpia de tecnologías: {technologiesList}")
    pauseConsole()


if __name__ == "__main__":
    main()
