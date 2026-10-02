from components import clearConsole, pauseConsole, printWarning


def main():
    clearConsole()
    dataValue = input("Ingrese pares clave=valor separados por ';': ").strip()
    partsList = [partValue for partValue in dataValue.split(";") if partValue.strip()]
    dataDictionary = {}

    for partValue in partsList:
        if "=" not in partValue:
            printWarning(f"Se ignoró el segmento inválido: {partValue}")
            continue

        keyValue, valueData = partValue.split("=", 1)
        cleanKey = keyValue.strip()
        cleanValue = valueData.strip()

        if not cleanKey:
            printWarning(f"Se ignoró un segmento con clave vacía: {partValue}")
            continue

        dataDictionary[cleanKey] = cleanValue

    print(f"Diccionario generado: {dataDictionary}")
    pauseConsole()


if __name__ == "__main__":
    main()