suma_par= 0
suma_impar = 0

print("Vamos a sumar los numero pares de  1-100")

for numeros in range(2,101,2):
    print(numeros, end=",")
    suma_par = suma_par + numeros
print()

print(f"La suma de los numeros pares  de 1-10 es {suma_par}")

print("Vamos a sumar los numero impares de  1-100")

for numeros in range(1,101,2):
    print(numeros, end=",")
    suma_impar = suma_impar + numeros
print()
print(f"La suma de los numeros de impares 1-100 es {suma_impar}")