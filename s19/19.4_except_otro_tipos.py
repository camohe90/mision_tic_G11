from sys import exc_info

try:
    numero = int(input("Digite un numero"))
    print("El resultado de la division es", 1/numero +"hola")
except (ValueError, TypeError, IndexError):
    print("Hay un error con el tipo de datos que usted ingreso")
    error = exc_info()
    print(error[0])
except ZeroDivisionError:
    print("Hay una division entre cero")
    error = exc_info()
    print(type(error))
    print(error)
except:
    print("Se encontro otro error")
    error = exc_info()
    print(error[0])