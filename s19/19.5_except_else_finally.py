

try:
    resultado = 14 + "30"
except TypeError:
    print("ERROR -> Se intentó sumar un numero y un cadena")
else: 
    print("Operacion realizada correctamente")
finally:
    print("Pase lo que pase yo me ejecuto y soy el cierre de try")

try:
    resultado = 14 + 30
except TypeError:
    print("ERROR -> Se intentó sumar un numero y un cadena")
else: 
    print("Operacion realizada correctamente")
finally:
    print("Pase lo que pase yo me ejecuto y soy el cierre de try", resultado)