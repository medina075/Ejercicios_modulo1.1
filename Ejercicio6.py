while True:
    cant_notas = input("Ingrese la cantidad de notas: ")
    try:
        numero = int(cant_notas)
        break
    except ValueError:
        print("solo numeros")

def promedio():
       lista = []
       for i in range(numero):
           valor1 = float(input(f"Ingrese las notas"))
           if valor1 < 0:
               print("la nota no puede ser menor a 0")
               return
           lista.append(valor1)

       mejor_nota = max(lista)
       peor_nota = min(lista)
       promedio_nota = sum(lista) / len(lista)


       print(f"El promedio es: {promedio_nota}")
       print(f"La mejor nota es:  {mejor_nota}")
       print(f"La peor nota es:  {peor_nota}")
promedio()

