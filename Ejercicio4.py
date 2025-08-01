numero = int(input("Ingresa un número entero para crear la tabla de multiplicar: "))

if numero<0:
    print("ingrese un valor valido")
elif numero>=0:
 print(f"Tabla de multiplicar del {numero}:")
 for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")