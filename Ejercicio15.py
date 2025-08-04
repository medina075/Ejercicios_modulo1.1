def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.

    Parámetros:
        calificaciones (list): Lista de números (floats o ints).

    Retorna:
        float: Promedio de las calificaciones. Si la lista está vacía, retorna 0.0.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def obtener_estado(promedio):
    """
    Determina el estado del estudiante según su promedio.

    Parámetros:
        promedio (float): Promedio del estudiante.

    Retorna:
        str: "Aprobado" si el promedio es mayor o igual a 3.0, "Reprobado" en caso contrario.
    """
    return "Aprobado" if promedio >= 3.0 else "Reprobado"


def generar_reporte(estudiantes):
    """
    Genera un reporte de calificaciones para un diccionario de estudiantes.

    Parámetros:
        estudiantes (dict): Diccionario con nombres de estudiantes como claves
                            y listas de calificaciones como valores.

    Muestra en pantalla un reporte con el nombre del estudiante, su promedio y su estado.
    """
    print("\nReporte de Calificaciones:")
    print("-------------------------")
    for nombre, calificaciones in estudiantes.items():
        promedio = calcular_promedio(calificaciones)
        estado = obtener_estado(promedio)
        print(f"- Estudiante: {nombre}, Promedio: {promedio:.2f}, Estado: {estado}")
    print("-------------------------")


# Diccionario principal con estudiantes y sus calificaciones
estudiantes = {
    "Ana": [4.5, 3.8, 4.2],
    "Juan": [2.5, 2.8, 3.0],
    "María": [5.0, 4.7, 4.9],
    "Luis": [2.0, 1.8, 2.5]
}

# Ejecutar la función principal
generar_reporte(estudiantes)
