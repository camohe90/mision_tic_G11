numeros_guardados = []
suma = 0

numeros_almacenar = int(input("Digite la cantidad de numeros que desea almacenar: "))

# Valido que el usuario ingrese un numero mayor  que 0 
while numeros_almacenar <= 0:
    print("Por favor ingrese un numero positivo")
    numeros_almacenar = int(input("Digite la cantidad de numeros que desea almacenar: "))

# Le pido al usuario que ingrese los numeros que desea almacenar y los guardo en la lista numeros_guardados
for contador in range (numeros_almacenar):
    numeros_guardados.append(int(input(f"Digite el numero {contador +1} que desea almacenar: ")))


# Recorro la lista numeros guardados y sumo solo los pares
for numero in numeros_guardados:
    if numero % 2 == 0:
        suma = suma +numero

print(f"La suma de los numero pares es {suma}")

