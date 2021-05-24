numero1 = 0
numero2 = 1

numero_fibonacci = int(input("Digite hasta que numero de fibonacci desea conocer la secuencia:"))

while numero_fibonacci <=0:
    print("Por favor ingrese un numero mayor a cero")
    numero_fibonacci = int(input("Digite hasta que numero de fibonacci desea conocer la secuencia:"))

if numero_fibonacci ==1:
    print("Este es el primer numero de fibonacci", numero1)
    print(f"Este es el primer numero de fibonacci {numero1} ")

else:
    print("Esta es la secuencia de Fibonacci")
    for contador in range(0,numero_fibonacci):
        print(numero1)
        total = numero1 + numero2
        numero1 = numero2
        numero2 = total
