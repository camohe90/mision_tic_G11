from tkinter import *

def mostrar_mensaje():
    mensaje.configure(text="Estamos volando y nadie nos para con python")

ventana = Tk()

mensaje = Label(ventana, fg="red", bg="white", font=("Arial",))
boton_mostar = Button(ventana, text="Mostrar", command=mostrar_mensaje)
boton_cerrar = Button(ventana, text="Cerrar", command=ventana.destroy)


mensaje.grid(row=0, column=0, columnspan=3)
boton_mostar.grid(row=1, column=0)
boton_cerrar.grid(row=1, column=1)

ventana.mainloop()

