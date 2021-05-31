"""Solicitar al usuario que ingrese una lista de numero, digite x para finalizar y que ingrese un numero   que desea limite, con ese limite desea saber  cuales numeros menor que este en la lista original y generar un lista con esos numeros"""

numero = 0
numeros_ingresados = [] 
numeros_menores = []

while numero != "x":
    numero = input("Digite el numero que desea almacenar: ")
    numeros_ingresados.append(numero)

print("*****Datos ingresados Correctamente****")
del numeros_ingresados[-1]

limite = int(input("Digite el numero que desea validar: "))

print(numeros_ingresados)

for datos in numeros_ingresados:
    if(int(datos) < limite):
        numeros_menores.append(int(datos))

print(f"Los numero menores que {limite} son {numeros_menores}")

