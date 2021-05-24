numeros_guardados = []

numeros_almacenar = int(input("Digite la cantidad de numeros que desea almacenar: "))

while numeros_almacenar <= 0:
    print("Por favor ingrese un numero positivo")
    numeros_almacenar = int(input("Digite la cantidad de numeros que desea almacenar: "))

for contador in range (numeros_almacenar):
    numeros_guardados.append(int(input(f"Digite el numero {contador +1} que desea almacenar: ")))

print(f"Estos son los numeros guardados: {numeros_guardados}")
