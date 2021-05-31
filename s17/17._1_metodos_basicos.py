frutas = ["Lulo", "Piña", "Coco","Mango", "Pera", "Manzana", "Banano"]
frutas2 = ("Lulo", "Piña", "Coco","Mango", "Pera", "Manzana", "Banano")

numeros = [10,5,4,6,20,8,14,2,1]
numeros2 = (10,5,4,6,20,8,14,2,1)
varios_elementos = ["hola", [2,3,4], 10.5]


print(frutas[1], ",", frutas2[1])

print(frutas[1:6], ",", frutas2[1:6])

print(min(frutas), ",", min(frutas2))
print(max(frutas), ",", max(frutas2))

frutas.append("Uva")
print(frutas)

#frutas2.append("Uva") No puedo agregarle elementos a una tupla
#print(frutas2)

print("antes de ordenar la lista")
print(frutas)
print("Despues de ordenar la lista")
frutas.sort()
print(frutas)

#frutas2.sort()   No puedo aplicar el metodo sort a una tupla
#print(frutas2)

print(sorted(frutas))
print("Ya se ejecuto")
nueva_tupla = tuple(sorted(frutas2))
print(frutas2)
print(nueva_tupla)
