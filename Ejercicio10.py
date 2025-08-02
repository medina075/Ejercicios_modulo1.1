def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en un texto.

    Parámetros:
        texto (str): Cadena de texto a analizar.

    Retorna:
        dict: Diccionario donde las claves son palabras en minúsculas
              y los valores son la cantidad de veces que aparece cada palabra.

    El conteo no distingue entre mayúsculas y minúsculas.
    """
    frecuencia = {}
    palabras = texto.lower().split()  # Convierte a minúsculas y divide el texto en palabras

    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

    return frecuencia


def mostrar_resultado(frecuencia):
    """
    Muestra el contenido del diccionario de frecuencia de palabras de forma legible.

    Parámetros:
        frecuencia (dict): Diccionario con palabras y sus frecuencias.
    """
    print("\nFrecuencia de palabras:")
    for palabra, cantidad in frecuencia.items():
        print(f"{palabra}: {cantidad}")


def main():
    """
    Función principal que solicita al usuario un texto,
    llama a la función de conteo y muestra el resultado.
    """
    texto_usuario = input("Ingrese un texto para analizar: ")
    resultado = contar_palabras(texto_usuario)
    mostrar_resultado(resultado)


# Ejecutar el programa
main()
