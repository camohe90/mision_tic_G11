def valor_absoluto(numero):
    """Esta funcion retorna el valor absoluto
        
        Parametros:
        numero: float

        return:
        numero: float 
    """

    if numero>0:
        return numero
    else: 
        return -numero

#print(valor_absoluto.__doc__)

numero_entrada = float (input("Digite el numero que sea obtener el valor absoluto: "))
print(f"El valor absoluto de {numero_entrada} es {valor_absoluto(numero_entrada)}")

