from tkinter import *

# bloque de funciones
def mostrar_mensaje():
    nombre = entrada_texto.get()
    mensaje.configure(text = "Hola " + nombre)
    entrada_texto.delete(0, END)

ventana = Tk()

# Definir que elementos tiene mi interfaz grafica
entrada_texto = Entry(ventana, width=20, justify=CENTER)
mensaje = Label(ventana, fg="red", bg="white", font=("times new roma",10))
boton_mostar = Button(ventana, text="Mostrar", command=mostrar_mensaje)
boton_cerrar = Button(ventana, text="Cerrar", command=ventana.destroy)


# Ubicar los elementos en la pantalla
entrada_texto.grid(row=0, column=0)
mensaje.grid(row=1, column=0)
boton_mostar.grid(row=1, column=1)
boton_cerrar.grid(row=1, column=2)


ventana.mainloop()