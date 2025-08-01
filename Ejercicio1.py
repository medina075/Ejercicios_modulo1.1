peso = float(input("Digite su peso en Kgs: "))
estatura = float(input("Digite su estatura en  metros: "))

imc = peso / (estatura * estatura)

#imc = peso / (estatura**2)

print(f"Segun su peso de {peso} y su altura de {estatura} su Indice de masa corporal es de {imc:.2f}.")