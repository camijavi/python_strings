from components import clearConsole, pauseConsole


def main():
    clearConsole()
    modulesList = ["autenticacion", "usuarios", "reportes", "seguridad"]
    modulesChain = " | ".join(modulesList)

    print(f"Módulos: {modulesChain}")
    pauseConsole()


if __name__ == "__main__":
    main()