
def sumar(numero_1, numero_2):
    resultado = numero_1 + numero_2
    return f"El resultado de la suma es: {resultado}"

def multiplicar(numero_1, numero_2 ):
    resultado = numero_1 * numero_2
    return f"El resultado de la multiplicacion es: {resultado}"

def restar(numero_1, numero_2):
    resultado = numero_1 - numero_2
    return f"El resultado de la resta es: {resultado}"

def dividir(numero_1, numero_2 ):
    resultado = numero_1 /  numero_2
    return f"El resultado de la division es: {resultado}"


print("Bienvenido a la super calculadora de fundamentos de python")

numero1 = int(input("Digite el numero 1: "))
numero2 = int (input("Digite el numero 2: "))

resultado_1 = sumar(numero1, numero2)
print(resultado_1)
print(restar(numero1, numero2))
print(multiplicar(numero1, numero2))
print(dividir(numero1, numero2))