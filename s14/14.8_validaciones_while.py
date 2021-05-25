nombre = input("Digite su primer nombre: ")

while not(nombre.isalpha()):
    print("No se registro correctamente el nombre, ya que tienes caracteres espaciales o numeros")
    nombre = input("Digite su primer nombre: ")

print(f"Hola {nombre} es un gusto saludarte")