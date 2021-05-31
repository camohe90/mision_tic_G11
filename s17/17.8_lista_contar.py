repeticion = []

notas_ingresadas = input("Digite la nota que desea registrar separada por comas: ")

notas = notas_ingresadas.split(",")

print(notas)
notas_filtradas = set(notas)
print(notas_filtradas)

for nota in sorted(notas_filtradas):
    repeticion.append(f"La {nota} se repite {notas.count(nota)}")

print(repeticion)