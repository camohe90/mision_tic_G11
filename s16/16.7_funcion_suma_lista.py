numeros = [1,2,3,4,5,6,7,8,9,10]

def sumatoria(numeros_lista):
    """Esta funcion retorna la sumatoria de todos lo elementos de una lista
        
        Parametros:
        numero_lista: list

        return:
        numero: int sumatoria de los elementos  
    """
    suma = 0

    for numero in numeros_lista:
        suma = suma + numero
    return suma

print(sumatoria(numeros))