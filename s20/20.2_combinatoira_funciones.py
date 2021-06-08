from funciones import combinatoria

numero_n = int(input("Digite el numero n: "))
numero_m = int(input("Digite el numero m: "))

while numero_n < numero_m:
    print("Por favor verifique que n sea mayor que m")
    numero_n = int(input("Digite el numero n: "))
    numero_m = int(input("Digite el numero m: "))

resultados_combinacion = combinatoria(numero_n, numero_m)
print("El resultado es", resultados_combinacion)