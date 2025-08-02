frase = input("Ingresa una frase: ")


vocales = 0
consonantes = 0


vocales1 = "aeiou"


for letra in frase.lower():
    if letra.isalpha():
        if letra in vocales1:
            vocales += 1
        else:
            consonantes += 1

print("cantidad de vocales:", vocales)
print("cantidad de consonantes:", consonantes)