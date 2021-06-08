
direcciones = [3,4,5,6,7,8,9]

def agregar_datos(lista, elemento):
    if elemento in lista:
        raise ValueError(f"ERROR -> No se pueden añador elementos duplicados {elemento}", 12312312312)
    lista.append(elemento)

try:
    agregar_datos(direcciones,10)
except ValueError as error:
    print(error.args)
else:
    print("Elementos agregados correctamente")
finally:
    print(f"La lista resultante es {direcciones}")


try:
    agregar_datos(direcciones,3)
except ValueError as error:
    print(error.args)
else:
    print("Elementos agregados correctamente")
finally:
    print(f"La lista resultante es {direcciones}")