numero_1 = int(input("Ingrese el numero 1:"))


if numero_1 <5 :
    print(f"El numero {numero_1} es menor que 5")
elif numero_1 >= 5 and numero_1 < 10:
    print(f"El numero {numero_1} es mayor o igual que 5 y menor que 10")
elif numero_1 >= 10 and numero_1 < 20:
    print(f"El numero {numero_1} es mayor o igual que 10 y menor que 20")
else:
    print(f"El numero {numero_1} es mayor que 20")
