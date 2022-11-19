from tkinter import *
'''
========================
    INTERFAZ GRÁFICA
========================
'''
raiz = Tk() #Nombe de nuestra ventana principal, objeto de la clase Tk
raiz.title("Python CRUD - Comisión 22622")

barramenu = Menu(raiz) #barramenu es un onjeto de la clase Menu que se ubicara en raiz
raiz.config(menu = barramenu)#Con este renglon asignamos a el objeto raiz el objeto menu, pero esta vacio

#Menú BBDD
bbddmenu = Menu (barramenu , tearoff = 0) # Lo ubicar en barramenu
bbddmenu.add_command(label="Conectar") #agrega otra opcion al objeto barramenu
bbddmenu.add_command(label="Listado de alumnos")
bbddmenu.add_command(label="Salir")
barramenu.add_cascade(label="BBDD", menu= bbddmenu)

#Menu Limpiar
limpiarmenu = Menu(barramenu, tearoff=0)
limpiarmenu.add_command(label="Limpiar Campos")
barramenu.add_cascade(label="Limpiar", menu= limpiarmenu)

#Menu Acerca de
acercamenu = Menu(barramenu, tearoff=0)
acercamenu.add_command(label="Licencia")
acercamenu.add_command(label="Sobre la app")
barramenu.add_cascade(label="Acerca de", menu=acercamenu)

#FrameCampos
framecampos = Frame(raiz)
framecampos.pack() #si no le pasas argumentos, lo que hace pack es "a groso modo" ubica este objeto debajo del objeto anterior

#Creamos las variables para guardar los datos de los entrys
#no son clases de python, son de tkinter
legajo = StringVar()
alumnos = StringVar()
email = StringVar()
escuela = StringVar()
calificacion = DoubleVar() # Numero con decimales
localidad=StringVar()
provincia =StringVar()

    
'''
IntVar() #declara variable de tipo entero
DoubleVar()#declara variable de tipo flotante
StringVar()#declara variable de tipo texto
BooleanVar()#declara variable de tipo booleano
'''

#Usar el metodo grid() para el posicionamiento dentro de framecampos
legajo_input= Entry(framecampos, textvariable=legajo)
legajo_input.grid(row=0, column=1, padx=10, pady=10)

alumnos_input= Entry(framecampos, textvariable=alumnos)
alumnos_input.grid(row=1, column=1, padx=10, pady=10)

email_input= Entry(framecampos, textvariable=email)
email_input.grid(row=2, column=1, padx=10, pady=10)

calificacion_input= Entry(framecampos, textvariable=calificacion)
calificacion_input.grid(row=3, column=1, padx=10, pady=10)

escuela_input= Entry(framecampos, textvariable=escuela)
escuela_input.grid(row=4, column=1, padx=10, pady=10)

localidad_input= Entry(framecampos, textvariable=localidad)
localidad_input.grid(row=5, column=1, padx=10, pady=10)

provincia_input= Entry(framecampos, textvariable=provincia)
provincia_input.grid(row=6, column=1, padx=10, pady=10)

#seccion Labels
legajolabel= Label(framecampos, text="Legajo")
legajolabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

alumnoslabel= Label(framecampos, text="Alumnos")
alumnoslabel.grid(row=1, column=0, padx=10, pady=10 , sticky="w")

emaillabel= Label(framecampos, text="Email")
emaillabel.grid(row=2, column=0, padx=10, pady=10 , sticky="w")

calificacionlabel= Label(framecampos, text="Calificación")
calificacionlabel.grid(row=3, column=0, padx=10, pady=10 , sticky="w")

escuelalabel= Label(framecampos, text="Escuela")
escuelalabel.grid(row=4, column=0, padx=10, pady=10 , sticky="w")

localidadlabel= Label(framecampos, text="Localidad")
localidadlabel.grid(row=5, column=0, padx=10, pady=10 , sticky="w")

provincialabel= Label(framecampos, text="Provincia")
provincialabel.grid(row=6, column=0, padx=10, pady=10, sticky="w")


'''
Sticky
        n
    nw      ne
w               e
    sw      se
        s
'''

#framebotones
framebotones = Frame(raiz)
framebotones.pack()

#Crear
boton_crear = Button(framebotones,text="Crear")
boton_crear.grid(row=0, column=0, pady=10 )

#leer
boton_leer = Button(framebotones,text="Leer")
boton_leer.grid(row=0, column=1,  pady=10 )

#actualizar
boton_actualizar = Button(framebotones,text="Actualizar")
boton_actualizar.grid(row=0, column=2,   pady=10 )

#borrar
boton_borrar = Button(framebotones,text="Borrar")
boton_borrar.grid(row=0, column=3, pady=10 )


#framecopy
framecopy = Frame(raiz)
framecopy.pack()

copylabel= Label(framecopy, text="2022 copyright C22622")
copylabel.grid(row=0, column=0)

raiz.mainloop() #No cierre la ventana cuando termine el programa, que la cierre el usuario