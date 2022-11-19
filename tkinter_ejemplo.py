from tkinter import *

raiz = Tk()
raiz.title('Python CRUD')

barramenu = Menu(raiz)

raiz.config(menu = barramenu)

#Menu BBDD
bbddmenu = Menu(barramenu, tearoff= 0)
bbddmenu.add_command(label='Conectar')
bbddmenu.add_command(label='Listado de alumnos')
bbddmenu.add_command(label='Salir')
barramenu.add_cascade(label='BBDD', menu=bbddmenu)

raiz.mainloop()