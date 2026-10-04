from components import clearConsole, pauseConsole, printWarning


def main():
    clearConsole()
    configValue = input("Ingrese la configuración (clave=valor;...): ").strip()
    configPartsList = [partValue for partValue in configValue.split(";") if partValue.strip()]
    configData = {}

    for partValue in configPartsList:
        if "=" not in partValue:
            printWarning(f"Se ignoró el segmento inválido: {partValue}")
            continue

        keyValue, valueData = partValue.split("=", 1)
        cleanKey = keyValue.strip()
        cleanValue = valueData.strip()

        if not cleanKey:
            printWarning(f"Se ignoró una clave vacía en el segmento: {partValue}")
            continue

        configData[cleanKey] = cleanValue

    print(f"Diccionario de configuración: {configData}")
    pauseConsole()


if __name__ == "__main__":
    main()
