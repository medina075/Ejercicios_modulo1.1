
numero_correcto= 75

print("Adivina el número entre 1 y 100")


while True:
    numero = int(input("Ingresa tu número: "))

    if numero < numero_correcto:
        print("El número es mayor.")
    elif numero > numero_correcto:
        print("El número es menor.")
    else:
        print("¡Correcto! Has adivinado el número.")
        break
