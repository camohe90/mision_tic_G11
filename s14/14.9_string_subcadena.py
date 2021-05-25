frase = "Bienvenidos a una nueva sesion del curso de python una version actualizada"

sub_cadena = input("Digite la cadena que desea validar: ")

resultado = frase.find(sub_cadena) # busca en el string y retorna la posición donde encuentra el parametro que se le envia a la funcion

print(resultado)