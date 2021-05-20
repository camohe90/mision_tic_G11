numero_1 = int(input("Ingrese el numero 1:"))
numero_2 = int(input("Ingrese el numero 2:"))

if numero_1 == numero_2:
    resultado = numero_1 * numero_2
    print(f"El resultado es: {resultado}")
else:
    if numero_1 > numero_2:
        resultado = numero_1 - numero_2
        print(f"El resultado es: {resultado}")
    else:
        resultado = numero_1 + numero_2
        print(f"El resultado es: {resultado}")