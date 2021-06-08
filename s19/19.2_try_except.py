numeros_cedula = [1,2,3,4,5,6,7,8,9,10]

try:
    print(contador)
except:
    print("Ocurrio un error")

try:
    numero = int (input("Digite un numero"))
except:
    print("Ocurrio error de tipo de dato")

try: 
    print(len(numeros_cedula))
    print(numeros_cedula[15]) 
except:
    print("Ocurrio un error de indice")

try:
    print(4 + "hola")
except:
    print("Ocurrio un error de tipo de datos ")