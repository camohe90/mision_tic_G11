numeros = [10,4,5,6,7,8,1,2,4,5]
ordenados = sorted(numeros) #organizar la lisat de menor a mayot
print(ordenados)
print(len(numeros)) #len me permite saber la cantidad de elementos que tiene la lista numeros

numeros.append(100) #agrego el numero 100 a la lista numeros en la final
print(numeros)

numeros.insert(2,340) # insertamos el numero 340 en la posicion 2 y desplaza los demas a la derecha
print(numeros)

numeros.pop(0) #elimanos el elemento que se encuentre en la posición 0
print(numeros)
del numeros[4:8] #eliminamos los elementos que se encuentre desde la poscion 4 hasta (8-1)

print(numeros) 
numeros.remove(4) # eliminar el primer numero 4 que encuentre en la lista
print(numeros)

print(numeros.index(340)) #retorna la posción del numero 340 en la lista

numeros_no_repetidos = set(numeros)

print(list(numeros_no_repetidos))