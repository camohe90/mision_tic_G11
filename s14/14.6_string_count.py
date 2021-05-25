frase = "Seguimos aprendiendo a contar caracteres en python a contar"
letra = input("Digite la letra que desea contar: ")

repeticion = frase.count(letra) # Retorna cuantas veces encontre el paramentro en la lista definida
repeticion2 = frase.count(letra,0,20)

print(f"La letra {letra} se repite {repeticion} veces, en la frase")
print(f"La letra {letra} se repite {repeticion2} veces, en la frase")
