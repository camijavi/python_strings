from components import clearConsole, pauseConsole


def main():
    clearConsole()
    technologiesValue = input("Ingrese tecnologías separadas por coma: ")
    technologiesList = [
        technologyValue.strip().lower()
        for technologyValue in technologiesValue.split(",")
        if technologyValue.strip()
    ]
    uniqueTechnologies = set(technologiesList)

    print(f"Tecnologías únicas: {uniqueTechnologies}")
    pauseConsole()


if __name__ == "__main__":
    main()
