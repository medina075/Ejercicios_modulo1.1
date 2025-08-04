# Saldo inicial del usuario
saldo = 1000.0


def consultar_saldo():
    """
    Muestra el saldo actual del usuario.
    """
    print(f"\nSaldo actual: ${saldo:.2f}")


def consignar():
    """
    Solicita una cantidad al usuario y la suma al saldo.
    Solo permite cantidades positivas.
    """
    global saldo
    try:
        cantidad = float(input("Ingrese la cantidad a consignar: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
        else:
            saldo += cantidad
            print(f"consignacion exitosa. Nuevo saldo: ${saldo:.2f}")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")


def retirar():
    """
    Solicita una cantidad al usuario y la descuenta del saldo si es posible.
    Solo permite cantidades positivas y no mayores al saldo disponible.
    """
    global saldo
    try:
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
        elif cantidad > saldo:
            print("saldo insuficiente.")
        else:
            saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")


def menu():
    """
    Muestra el menú del cajero automático y permite al usuario realizar operaciones
    hasta que decida salir.
    """
    while True:
        print("\n--- CAJERO AUTOMÁTICO ---")
        print("1. Consultar saldo")
        print("2. Consignar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            consignar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar el programa directamente
menu()
