def contar_palabras(frase = "ERROR123"):
    """Esta funcion retorna la cantidad de palabras que tiene un frase
        
        Parametros:
        frase: string 

        return:
        numero: int cantidad de palabras 
    """
    if frase == "ERROR123":
        return "Por favor revise la frase que ingreso"
    else:
        lista_mensaje = frase.split()
        return len(lista_mensaje)

frase_inicial = input("Digite la frase que desea verificar: ")
print(f"La frase ingresada tiene {contar_palabras(frase_inicial)} palabras")

print(contar_palabras())