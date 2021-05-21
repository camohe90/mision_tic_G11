palabra = input("Ingrese 'hola' para continuar")

while palabra != 'hola':
    palabra = input("ERROR -> Ingrese  una nueva palabra")

print("La palabra", palabra, "fue ingresada correctamente")