"""Programa que me permita ingresar 10 numeros
    me imprima el promedio de los numeros ingresados
    me imprima el mayor y el menor
    que me genere una lista con los pares y otra con los impares"""

total = 0
numeros_ingresados = []
pares = []
impares = []

for numero in range(10):
    mensaje = f"Ingrese el {numero+1} que desea almacenar: "
    numeros_ingresados.append(int(input(mensaje)))

print(numeros_ingresados)

for numero in range(len(numeros_ingresados)):
    total += numeros_ingresados[numero]
    if numero % 2 == 0:
        pares.append(numeros_ingresados[numero])
    else:
        impares.append(numeros_ingresados[numero])

print(f"El promedio de los numero ingresados es: {total / len(numeros_ingresados)}")
print(f"El numero menor en la lista de numeros ingresados es: {min(numeros_ingresados)}")
print(f"El numero mayor en la lista de numeros ingresados es: {max(numeros_ingresados)}")
print(f"Los numeros pares que hay en la lista de numeros ingresados son {pares}")
print(f"Los numeros impares que hay en la lista de numeros ingresados son{impares}")