factorial = 1

numero_factorial = int(input("Digite el numero que desea conocer el factorial: "))

for numero in range(1, numero_factorial+1):
    factorial = factorial * numero

print(f"El factorial de {numero_factorial} es: {factorial}")