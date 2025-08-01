palabra_original =input(str("Ingrese una palabra u oracion"))# 5 Caracteres
palabra = palabra_original.replace(" ", "").lower()# Elimina los espacios en blanco

invertido = "" # Variable para almacenar el texto invertido
for i in range(len(palabra) - 1, -1, -1): # 0 hasta 4
    invertido = invertido + palabra[i]

if invertido == palabra:
    print(f"{palabra_original} es un palíndromo")
else:
    print(f"{palabra_original} no es un palíndromo")