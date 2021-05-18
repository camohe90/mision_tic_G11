#no recomiendo
""" O = 1
I = 0 """

#No recomendado
x = "Camilo Molano"
y,z = x.split()
print(y,z,sep =",")

#Recomendado
nombre = "Camilo Molano"
primer_nombre, primer_apellido = nombre.split()
print(primer_nombre, primer_apellido, sep=",")


def db(x):
    return x*2

def multiplicar_por_dos(numero):
    return numero*2
