numero_usarios = [10,24,35,4,5,6,7,8,9,10]
suma = 0
suma2 = 0

print(sum(numero_usarios))

for numero in numero_usarios:
    suma = suma + numero

print("La suma del primer for es:", suma)

cantidad_elementos = len(numero_usarios)

for posicion in range(cantidad_elementos):
    print(numero_usarios[posicion])
    suma2 = suma2 + numero_usarios[posicion]

print("La suma del segundo for es", suma2)

