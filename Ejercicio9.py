contactos = {}

def añadir_contacto():
    """
    Añade un nuevo contacto a la agenda.
    Solicita al usuario el nombre y el número de teléfono.
    Si el nombre ya existe, muestra un mensaje de advertencia.
    """
    nombre = input("Ingrese el nombre del contacto: ").lower()
    if nombre in contactos:
        print("El contacto ya existe.")
    else:
        num_cel = input("Ingrese el número de teléfono: ")
        contactos[nombre] = num_cel
        print("Contacto añadido.")

def buscar_contacto():
    """
    Busca el número de teléfono de un contacto por su nombre.
    Si el contacto no existe, informa al usuario.
    """
    nombre = input("Ingrese el nombre del contacto a buscar: ").lower()
    if nombre in contactos:
        print(f"Teléfono de {nombre}: {contactos[nombre]}")
    else:
        print("Contacto no encontrado.")

def mostrar_contactos():
    """
    Muestra todos los contactos almacenados en contactos.
    Si contactos está vacío, se indica al usuario.
    """
    if not contactos:
        print("La agenda está vacía.")
    else:
        print("Lista de contactos:")
        for nombre, telefono in contactos.items():
            print(f"{nombre}: {telefono}")

def main():
    """
    Muestra el menú principal de la agenda y gestiona la selección del usuario.
    Ejecuta el bucle principal hasta que el usuario decide salir.
    """
    while True:
        print("\n--- AGENDA DE CONTACTOS ---")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            añadir_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            mostrar_contactos()
        elif opcion == "4":
            print("Saliendo de la agenda...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el programa
main()
