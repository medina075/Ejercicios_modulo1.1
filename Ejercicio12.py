# Diccionario con factores de conversión respecto al metro
diccionario = {
    "metro": 1.0,
    "pie": 3.28084,
    "yarda": 1.09361,
    "centimetro": 100.0,
    "milimetro": 1000.0,
    "kilometro": 0.001,
    "pulgada": 39.3701
}

def convertir_unidad(cantidad, valor, unidad_resultado):
    """
    Convierte una cantidad de una unidad a otra usando factores de conversión.

    Parámetros:
        cantidad (float): Cantidad numérica a convertir.
        valor (str): Unidad de medida original.
        unidad_resultado (str): Unidad de medida deseada.

    Retorna:
        float: Resultado de la conversión, o None si alguna unidad no es válida.
    """
    valor = valor.lower()
    unidad_resultado = unidad_resultado.lower()

    if valor not in diccionario:
        print(f"Unidad de origen no reconocida: {valor}")
        return None
    if unidad_resultado not in diccionario:
        print(f"Unidad de destino no reconocida: {unidad_resultado}")
        return None

    # Convertimos a metros y luego a la unidad destino
    cantidad_en_metros = cantidad / diccionario[valor]
    resultado = cantidad_en_metros * diccionario[unidad_resultado]
    return resultado


def main():
    """
    Función principal que solicita datos al usuario y realiza la conversión.
    Muestra el resultado o un mensaje de error si las unidades no son válidas.
    """
    try:
        cantidad = float(input("Ingrese la cantidad a convertir: "))
        valor = input("Unidad de origen (ej: metro, pie, kilometro): ").lower()
        unidad_resultado = input("Unidad de destino (ej: metro, yarda, pulgada): ").lower()

        resultado = convertir_unidad(cantidad, valor, unidad_resultado)

        if resultado is not None:
            print(f"\n{cantidad} {valor} equivale a {resultado:.4f} {unidad_resultado}")
    except ValueError:
        print("Por favor, ingrese una cantidad numérica válida.")

# Ejecutar el programa
main()
