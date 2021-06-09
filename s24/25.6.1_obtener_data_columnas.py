import sqlite3

conexion = sqlite3.connect("db/datos1.db")
print("Conectado exitosamente")

cursor = conexion.cursor()

cursor.execute("SELECT id, nombre from empleados where salario >300 and salario < 1450")

data = cursor.fetchall()

''' for info in data:
    print(info[1]) '''

[print(linea) for linea in data]