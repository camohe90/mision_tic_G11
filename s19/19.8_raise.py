numero = int(input("Ingrese un numero"))

try:
    if numero < 10:
        raise ValueError("ERORR -> debe ser un numero mayor","algo mas", 123)
except ValueError as errorcito:
    print("vamos a ver el error")
    print(errorcito.args[2])