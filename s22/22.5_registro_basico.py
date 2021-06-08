from tkinter import *

clientes = []

# bloque de funciones
def guardar_datos():
    nombre_in = info_nombre.get()
    apellido_in = info_apellido.get()
    cedula_in = info_cedula.get()
    clientes.append(nombre_in +" " + apellido_in + " "+ cedula_in)
    mensaje_salida["text"] = "Cliente Guardado"
    ventana.after(2000,borrar_datos)

def borrar_datos():
    info_nombre.set("")
    info_apellido.set("")
    info_cedula.set("")
    mensaje_salida["text"] =""

#Iniciar ventana
ventana = Tk()
ventana.geometry("800x600")



# Definir variables
info_nombre = StringVar()
info_apellido = StringVar()
info_cedula  = StringVar()

# Definir que elementos tiene mi interfaz grafica
nombre = Label(ventana, text="Nombre: ")
apellido = Label(ventana, text="Apellido")
cedula = Label(ventana,  text="Cédula:")
mensaje_salida = Label(ventana, fg="red")

entrada_nombre = Entry(ventana, width=20, justify=CENTER, textvariable= info_nombre)
entrada_apellido = Entry(ventana, width=20, justify=CENTER, textvariable= info_apellido)
entrada_cedula = Entry(ventana, width=20, justify=CENTER, textvariable= info_cedula)

boton_guardar = Button(ventana, text="Guardar", command=guardar_datos)


# Ubicar los elementos en el grid
nombre.grid(row=0, column=0)
entrada_nombre.grid(row=0, column=1)
apellido.grid(row=1, column=0)
entrada_apellido.grid(row=1, column=1)
cedula.grid(row=2, column=0)
entrada_cedula.grid(row=2, column=1)
boton_guardar.grid(row=3,column=0)
mensaje_salida.grid(row=4, column=0, columnspan=2)



# mainloop
ventana.mainloop()