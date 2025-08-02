def comparar(lista1, lista2):
    """
    Compara dos listas y devuelve una tupla con tres conjuntos:
    - Elementos comunes a ambas listas.
    - Elementos únicos de la primera lista.
    - Elementos únicos de la segunda lista.

    Parámetros:
        lista1 (list): Primera lista de elementos.
        lista2 (list): Segunda lista de elementos.

    Retorna:
        tuple: Una tupla con tres sets:
            (comunes, solo_en_lista1, solo_en_lista2)
    """
    set1 = set(lista1)
    set2 = set(lista2)

    comunes = set1 & set2
    solo_en_lista1 = set1 - set2
    solo_en_lista2 = set2 - set1

    return (comunes, solo_en_lista1, solo_en_lista2)


def mostrar_resultados(comunes, solo1, solo2):
    """
    Muestra los conjuntos resultantes de la comparación entre listas.

    Parámetros:
        comunes (set): Elementos comunes en ambas listas.
        solo1 (set): Elementos únicos de la primera lista.
        solo2 (set): Elementos únicos de la segunda lista.
    """
    print("\nElementos comunes en ambas listas:")
    print(comunes)

    print("\nElementos únicos en la primera lista:")
    print(solo1)

    print("\nElementos únicos en la segunda lista:")
    print(solo2)


def main():
    """
    Función principal que solicita dos listas al usuario,
    llama a la función de comparación y muestra los resultados.
    """
    lista1 = input("Ingrese los elementos de la primera lista (separados por comas): ").split(",")
    lista2 = input("Ingrese los elementos de la segunda lista (separados por comas): ").split(",")

    # Eliminamos espacios extra
    lista1 = [item.strip() for item in lista1]
    lista2 = [item.strip() for item in lista2]

    comunes, solo1, solo2 = comparar(lista1, lista2)
    mostrar_resultados(comunes, solo1, solo2)


# Ejecutar el programa
main()
