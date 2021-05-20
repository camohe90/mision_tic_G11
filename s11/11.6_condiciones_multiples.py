edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Bienvenido al bar porque eres mayor de edad")
else:
    tiempo_restante = 18 - edad
    print(f"No puede ingregar al bar por favor vuelve en {tiempo_restante} años")
