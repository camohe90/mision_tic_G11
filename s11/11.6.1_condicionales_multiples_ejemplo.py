
calificacion_1, calificacion_2, calificacion_3 = input("Ingrese las tres calificaciones parciales separadas por espacios").split()
promedio = ((float(calificacion_1) + float(calificacion_2) + float(calificacion_3)) / 3)

if promedio >= 70:
    print("El alumno aprobo")
else:
    print("El alumno no aprobo")