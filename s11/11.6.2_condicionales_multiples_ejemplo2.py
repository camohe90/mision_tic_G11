
numero_1, numero_2 = input("Ingrese los dos numeros que desea comprobar separado por espacios").split()

numero_1 = int(numero_1)
numero_2 = int(numero_2)

if numero_1 > numero_2:
    print(f"El numero 1: {numero_1} es mayor que esl numero 2: {numero_2}")
else:
    print(f"El numero2: {numero_2} es mayor que el numero1: {numero_1}")