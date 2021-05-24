notas = [3,4,5,3,3,1,2,1,2,3,1,2,3]
total = 0

cantidad_notas = len(notas)

for nota in notas:
    total = total + nota

promedio = total / cantidad_notas

print(f"Este es el promedio de las notas {promedio:.2f}")