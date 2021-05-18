#No recomendado
resultado1 =  x ** 2 + 5
resultado2 = (x + y) * (x -y )

#Recomendado
resultado1 = x**2 + 5
resultado2 = (x+y) * (x-y)

#No recomendado
mi_lista = [ 1, 2, 3, 4, 5, 6, 7 ]

#Recomendado 
mi_lista = [1, 2, 3, 4, 5, 6]

numero1 = 5
numero2 = 6

#No recomendado
print( numero1 , numero2 )
print( numero1 + numero2 )

#Recomendado
print(numero1, numero2)
print(numero1+numero2)

#No recomendado
def funcion(parametro_defecto = 5):

#Recomendada
def funcion(parametro_defecto=5):


def doble(numero):
    numero*2

#No recomendado
doble( 2 )

#Recomendado
doble(2)

#No recomendado
numero1                 = 9
numero2                 = 10
numero_mas_largo = 11

#Recomendado
numero1 = 9
numero2 = 10
numero_mas_largo = 11