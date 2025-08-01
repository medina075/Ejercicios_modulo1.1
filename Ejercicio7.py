cant_limon = 0
cant_salchichon = 0
cant_pan = 0
temp = 0
while True:

    seleccionar = int(
        input(
            "Selecciona una opcion de producto: \n 1.pan \n 2.salchichon \n 3.limon \n 4.finalizar compra \n opcion:"))
    if seleccionar < 0 or seleccionar > 4:
        print("Seleccione una opcion valida")
    elif seleccionar == 1:
        cant_pan = int(input("Ingrese la cantidad de pan: "))

    elif seleccionar == 2:
        cant_salchichon = int(input("Ingrese la cantidad de salchichon: "))

    elif seleccionar == 3:
        cant_limon = int(input("Ingrese la cantidad de limon: "))
    elif seleccionar == 4:
        print(f"Total de panes: {cant_pan}")
        print(f"Total de salchichon: {cant_salchichon}")
        print(f"Total de limon: {cant_limon}")
        temp = int(input("¿Desea eliminar algun producto? 1.si 2.no"))
        seleccionar = 0
        if temp == 1:
            eliminar = int(input("Ingrese el item a eliminar:\n 1.pan \n 2.salchichon \n 3.limon "))
            if eliminar == 1:
                cant_pan = 0
            elif eliminar == 2:
                cant_salchichon = 0
            elif eliminar == 3:
                cant_limon = 0
        elif temp == 2:
            break
