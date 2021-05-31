def es_par(numero_validar):
    if numero_validar % 2 == 0:
        return "Es par"
    else:
        return "No es par"

print(es_par(1234))
print(es_par(101))