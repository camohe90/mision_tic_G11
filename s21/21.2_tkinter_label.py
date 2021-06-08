from tkinter import *

ventana = Tk()


mensaje = Label(ventana, text="Seguimos avanzando con python")
boton_cerrar = Button(ventana, text="Cerrar", command=ventana.destroy)

mensaje.grid(row=0, column=0)
boton_cerrar.grid(row=1, column=0)

ventana.mainloop()

