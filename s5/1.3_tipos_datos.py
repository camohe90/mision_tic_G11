"""Realizar un programa que simule a una persona que saluda a otra persona, deben solicitar que el usuario ingrese nombre, apellido, comida favorita y color favorito. El sistema debe imprimir dos mensajes 1 Salundado al usuario, 2 Diciendo algun comentario referente a la comida y al color ingresado"""

print("Manejo de información de entrada con python")
print("--------------------------------------------------")

primer_nombre = input("Por favor ingrese su nombre: ") #Guardo la información ingresada por teclado en la variable primer_nombre
primer_apellido = input("Por favor ingrese su apellido: ")#Guardo la información ingresada por teclado en la variable primer_apellido

print("Hola", primer_nombre, primer_apellido, "es un gusto saludarte")
print(type(primer_nombre))
print(type(primer_apellido))