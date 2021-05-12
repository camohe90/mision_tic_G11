
num1 = 20 
num2 = -15
num3 = 7
num4 = 40403440340340214024.23

# enteros en python
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
print(pow(4,3))

#flotantes en python
numero_flotante = round(num1 / num3 ,2)
print(numero_flotante)
print(type(numero_flotante))
print(4e7)
print(type(4e7))

#números complejos
x = 2 + 3j
print(type(x)) 
print(x.real)
print(x.imag)

#string
frase = "Esto es una cadena de texto" #Esto es un string
print(frase)
print(type(frase))
print(frase[0])
print(frase[-1])
print(frase[4])
print(len(frase))

#lista
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
print(lista[0])
print(lista[-1])
print(lista[4:9])
print(lista[0:7])
print(len(lista))

lista = ["hola", 1 , 2.2 , [3,2,3]]
print(type(lista))
print(lista[-1])
print(type(lista[-1]))
print(lista[-1][1])
print(type(lista[-1][1]))
print(lista[2])
print(type(lista[2]))

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros[1] = 4
numeros[-1] = 300
print(len(numeros))
numeros.append(2.5)
print(len(numeros))
numeros.append("HOLA LISTA")
print(len(numeros))
print(numeros)

data_que_no_cambia = (1,2,3,4, "numero", 2.2, "hola") #son inmutables
print(data_que_no_cambia[-1])
print(data_que_no_cambia[1])
#tupla[0] = "Cambiando la tupla"

conjuntos = {1,5,2,3,4,5,6,7,8,2,3,2,1,2,1,2}
print(conjuntos)

futbolistas = {
     1: "Ospina", 
	13 : "Mina",
    10 : "James",
	1 : "Jorge",
    9 : "Falcao", 
	19 : "Muriel",
    11: "Cuadrado", 
	18 : "Fabra",
    6: "Barrios",  
	3: "Murillo",
    'defensa1' : "Zapata"
}

print(futbolistas[13])
print(futbolistas['defensa1'])