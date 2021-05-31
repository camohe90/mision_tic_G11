suma =[]
suma2 = []
numeros1 = [1,2,3,4,5]
numeros2 = [1,2,5,3,4]

for elemento in range(len(numeros1)):
    resultado1 = numeros1[elemento] + numeros2 [elemento]
    suma.append(resultado1) 


for elemento in range(len(numeros1)):
    resultado2 = numeros1[elemento] + numeros2 [len(numeros1)-1-elemento]
    suma2.append(resultado2) 

print(suma2)

