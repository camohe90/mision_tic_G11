factorial_n = 1
factorial_m = 1
factorial_nm = 1

numero_n = int(input("Digite el numero n: "))
numero_m = int(input("Digite el numero m: "))

while numero_n < numero_m:
    print("Por favor verifique que n sea mayor que m")
    numero_n = int(input("Digite el numero n: "))
    numero_m = int(input("Digite el numero m: "))

resultado_nm = numero_n -numero_m

for numero in range(1, numero_n+1):
    factorial_n = factorial_n * numero

for numero in range(1, numero_m+1):
    factorial_m = factorial_m * numero

for numero in range(1, resultado_nm+1):
    factorial_nm = factorial_nm * numero

combinacion = factorial_n / (factorial_nm * factorial_m)

print(f"El numero de combiaciones de  {numero_n} y {numero_m} es {combinacion}")