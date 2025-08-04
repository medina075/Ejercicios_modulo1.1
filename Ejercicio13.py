# Lista para almacenar el inventario de productos
inventario = []

def agg_producto():
    """
    Agrega un nuevo producto al inventario.
    Solicita al usuario el nombre, precio y cantidad del producto.
    """
    nombre = input("Ingrese el nombre del producto: ").strip()
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
    except ValueError:
        print("Error: precio o cantidad no válidos.")
        return

    producto = {
        "nombre": nombre.lower(),
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print("Producto agregado correctamente.")


def realizar_venta():
    """
    Realiza una venta actualizando la cantidad del producto en el inventario.
    Si el producto no existe o no hay suficiente cantidad, muestra un mensaje de error.
    """
    nombre = input("Ingrese el nombre del producto a vender: ").strip().lower()
    try:
        cantidad_venta = int(input("Ingrese la cantidad a vender: "))
    except ValueError:
        print("Cantidad no válida.")
        return

    for producto in inventario:
        if producto["nombre"] == nombre:
            if producto["cantidad"] >= cantidad_venta:
                producto["cantidad"] -= cantidad_venta
                total = cantidad_venta * producto["precio"]
                print(f"Venta realizada. Total: ${total:.2f}")
                return
            else:
                print("No hay suficiente stock disponible.")
                return

    print("Producto no encontrado en el inventario.")


def mostrar_inventario():
    """
    Muestra todos los productos del inventario con su nombre, precio y cantidad disponible.
    """
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\n--- INVENTARIO ---")
        for producto in inventario:
            print(f"Nombre: {producto['nombre'].capitalize()}, "
                  f"Precio: ${producto['precio']:.2f}, "
                  f"Cantidad: {producto['cantidad']}")


def menu():
    """
    Muestra el menú principal del sistema de inventario y gestiona las opciones del usuario.
    """
    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agg_producto()
        elif opcion == "2":
            realizar_venta()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar directamente
menu()
