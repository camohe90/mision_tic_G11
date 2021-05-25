suma = 0
union = 0

nombre = input("Digite su nombre completo")

print(nombre.upper())
print(nombre.lower())
print(nombre.capitalize())
print(f"Su nombre completo es: {nombre}")

lista_nombre = nombre.split()
print(lista_nombre)
union = "".join(lista_nombre)
print(union)
cantidad_caracteres = len(union)

print(f"La cantidad de letras que tiene su nombre es: {cantidad_caracteres}")

for palabra in lista_nombre:
    suma = suma + len(palabra)

print(f"La cantidad de letras que tiene su nombre es: {suma}")