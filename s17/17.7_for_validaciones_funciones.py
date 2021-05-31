
numero = 0
numeros_ingresados = [] 

def numeros_menores(numeros, numero_limite):
    menores =[]
    del numeros[-1]

    for numero in numeros:
        if (int (numero) < numero_limite):
            menores.append(int(numero))
    return menores


while numero != "x":
    numero = input("Digite el numero que desea almacenar: ")
    numeros_ingresados.append(numero)
print("*****Datos ingresados Correctamente****")

limite = int(input("Digite el numero que desea validar: "))

resultado_numeros_menores = numeros_menores(numeros_ingresados, limite)

print(f"Lo numero menores que {limite} son {resultado_numeros_menores}")