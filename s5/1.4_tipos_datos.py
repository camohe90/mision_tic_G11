"""Realizar un programa que simule a una persona que saluda a otra persona, deben solicitar que el usuario ingrese nombre, apellido, edad comida favorita y color favorito. El sistema debe imprimir dos mensajes 1 Salundado al usuario, 2 Diciendo algun comentario referente a la comida y al color ingresado"""


print("Manejo de información de entrada con python")
print("--------------------------------------------------")

primer_nombre = input("Por favor ingrese su nombre: ") #Guardo la información ingresada por teclado en la variable primer_nombre
edad = int(input("Por favor ingrese edad: ")) #Guardo la información ingresada por teclado en la variable edad

print("Hola", primer_nombre, "es un gusto saludarte, veo que tu tienes", edad +10, "años")
print(type(primer_nombre))
print(type(edad))