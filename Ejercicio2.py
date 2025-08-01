edad = int(input("Ingrese su edad: "))
if edad<0:
    print("ingrese un valor valido")
if edad>=25:
    print(f"Segun su edad usted es un mayor de edad de {edad} años")
elif 18<=edad<25:
    print(f"Usted es mayor de edad y ademas es un joven adulto de {edad} años")
elif 0<edad<=17:
    print(f"usted es un menor de edad de {edad} años")