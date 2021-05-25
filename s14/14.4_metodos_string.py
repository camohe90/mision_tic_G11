frase = "Bienvenidos a una nueva sesion del curso de Python a las 11"

print(frase)
print(type(frase)) # Type retorna el tipo de datos del parametro (frase)

print(frase.upper()) # Retorna el string con todos sus caracteres en mayuscula
print(frase.lower()) # Retorna el string con todos sus caracteres en minuscula
print(frase.title()) # Retorna el string con todas las palabras iniciando en letra mayuscula

print(frase.lower().replace("python", "cocina")) # busca en el string que se encuentre la palabra que se pasa por primer paramentro y lo reemplaza por el segundo parametro

palabra5 = "perro"
print(palabra5 == "Perro".lower())

palabras = frase.split() # Retorna una lista con los elementos que estan en el string y los separa por el espacio en blanco.
print(palabras)

for palabra in palabras:   
    if len(palabra) > 1 :
        print(palabra.capitalize(), end =" ")
    else:
        print(palabra , end =" ")
print()

print(frase.title()) 


palabras = frase.split() # Retorna una lista con los elementos que estan en el string y los separa por el espacio en blanco.
print(palabras)

print("*.*.".join(palabras)) # Genera un string con los elementos que se encuentre en la lista que le paso como parametro y los separa con el string que se encuentra en las comillas "***"