from tkinter import *

raiz = Tk()
raiz.title('Python CRUD para Mamau')

barramenu = Menu(raiz)

raiz.config(menu = barramenu)

# Menu BBDD
bbddmenu = Menu(barramenu, tearoff= 0)
bbddmenu.add_command(label='Conectar')
bbddmenu.add_command(label='Listado de alumnos')
bbddmenu.add_command(label='Salir')
barramenu.add_cascade(label='BBDD', menu=bbddmenu)

# Menu limpiar
limpiarmenu = Menu(barramenu, tearoff=0)
limpiarmenu.add_command(label='Limpiar campos')
barramenu.add_cascade(label='Limpiar', menu=limpiarmenu)

# Menu Acerca de...
acercamenu = Menu(barramenu, tearoff=0)
acercamenu.add_command(label='Licencia')
acercamenu.add_command(label='Sobre la App')
barramenu.add_cascade(label='Acerca de...', menu=acercamenu)

# FrameCampos
framecampos = Frame(raiz)
framecampos.pack()



raiz.mainloop()