from tkinter import *
import sqlite3 as sq3
#from asyncio.windows_events import NULL # Nos permite trabajar con la BBDD y registros NULL
from tkinter import messagebox

'''
========================
        FUNCIONAL
========================
'''

#Conexion a la base de datos
def conectar():
    global con
    global cur
    con = sq3.connect("my_db.db") 
    cur = con.cursor()
    messagebox.showinfo("STATUS","Conectado a la BBDD!")
    
    #SQL para crear la tabla escuela
    instruct1= '''CREATE TABLE IF NOT EXISTS escuelas (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,  
    nombre varchar(45) DEFAULT NULL,
    localidad varchar(45) DEFAULT NULL,
    provincia varchar(45) DEFAULT NULL,
    capacidad INTEGER DEFAULT NULL)'''
    
    #SQL para crear la tabla alumnos 
    instruct2= '''CREATE TABLE  IF NOT EXISTS alumnos (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_escuela INTEGER DEFAULT NULL,
    legajo INTEGER DEFAULT NULL,
    nombre varchar(45) DEFAULT NULL,
    nota decimal(10,0) DEFAULT NULL,
    grado INTEGER DEFAULT NULL,
    email varchar(45) NOT NULL,
    FOREIGN KEY (id_escuela) REFERENCES escuelas(id))'''
    
    cur.execute(instruct1)
    cur.execute(instruct2)
    
    #DATOS PARA LAS TABLAS
    lista1=[(1,'Normal 1','Quilmes','Buenos Aires',250),(2,'Gral. San Martín','San Salvador','Jujuy',100),(3,'Belgrano','Belgrano','Córdoba',150),(4,'EET Nro 2','Avellaneda','Buenos Aires',500),(5,'Esc. N° 2 Tomás Santa coloma','Capital Federal','Buenos Aires',250)]
    lista2=[(1,2,1000,'Ramón Mesa',8,1,'rmesa@mail.com'),(2,2,1002,'Tomás Smith',8,1,''),(4,1,101,'Juan Perez',10,3,''),(5,1,105,'Pedro González',9,3,''),(6,5,190,'Roberto Luis Sánchez',8,3,'robertoluissanchez@gmail.com'),(7,2,106,'Martín Bossio',8,3,''),(8,4,100,'Paula Remmi',3,1,'mail@mail.com'),(9,4,1234,'Pedro Gómez',6,2,'')]

    
    try:
        cur.executemany("INSERT INTO escuelas VALUES (?,?,?,?,?)",lista1)
        cur.executemany("INSERT INTO alumnos VALUES (?,?,?,?,?,?,?)",lista2)
    except:
        pass
    
    con.commit()


#DATOS PARA LAS TABLAS
lista1=[(1,'Normal 1','Quilmes','Buenos Aires',250),(2,'Gral. San Martín','San Salvador','Jujuy',100),(3,'Belgrano','Belgrano','Córdoba',150),(4,'EET Nro 2','Avellaneda','Buenos Aires',500),(5,'Esc. N° 2 Tomás Santa coloma','Capital Federal','Buenos Aires',250)]
lista2=[(1,2,1000,'Ramón Mesa',8,1,'rmesa@mail.com'),(2,2,1002,'Tomás Smith',8,1,''),(4,1,101,'Juan Perez',10,3,''),(5,1,105,'Pedro González',9,3,''),(6,5,190,'Roberto Luis Sánchez',8,3,'robertoluissanchez@gmail.com'),(7,2,106,'Martín Bossio',8,3,''),(8,4,100,'Paula Remmi',3,1,'mail@mail.com'),(9,4,1234,'Pedro Gómez',6,2,'')]


#Salir
def salir():
    respuesta= messagebox.askquestion("CONFIRMACION","Está seguro que quiere salir?")
    if respuesta == "yes":
        try:
            con.close()
        except:
            pass
        raiz.destroy()
        
#Limpiar
def limpiar():
    legajo.set("")
    alumnos.set("")
    email.set("")
    calificacion.set("0.0")
    escuela.set("Seleccione...")
    localidad.set("")
    provincia.set("")
    legajo_input.config(state="normal")
    
#Licencia
def licencia():
    mensaje='''
                GNU GENERAL PUBLIC LICENSE
                CRUD PYTHON Version 1, November 2022
                Copyright (C) 2022 Marcia.
                Everyone is permitted to copy and distribute verbatim copies
                of this license document, but changing it is not allowed.
        '''
    messagebox.showinfo("LICENCIA",mensaje)
    

#Sobre la app
def sobre_app():
    messagebox.showinfo("ACERCA DE...", "Creado por Marcia \n para Codo a Codo 4.0 - Big Data \n 2022")       


#---------------
#     CRUD
#---------------

#Leer
def leer():
    query='''SELECT alumnos.legajo, alumnos.nombre, alumnos.nota, alumnos.email, escuelas.nombre, escuelas.localidad, escuelas.provincia
        FROM alumnos INNER JOIN escuelas 
        ON alumnos.id_escuela = escuelas._id 
        WHERE alumnos.legajo=
        '''
    try:
        cur.execute(query+legajo.get())
    except:
        pass

    resultado=cur.fetchall()
    if resultado == []:
        messagebox.showerror("ERROR", "Número de legajo inexistente")
    else:
        legajo.set(resultado[0][0])
        alumnos.set(resultado[0][1])
        calificacion.set(resultado[0][2])
        email.set(resultado[0][3])
        escuela.set(resultado[0][4])
        localidad.set(resultado[0][5])
        provincia.set(resultado[0][6])
        legajo_input.config(state="disabled")

# Crear Legajo
def crear():
    id_escuela = buscar_escuelas(True)
    id_escuela = int(id_escuela[0])
    datos = id_escuela, legajo.get(), alumnos.get(), calificacion.get(), email.get() #escuela.get(), localidad.get(), provincia.get()    

    cur.execute('INSERT INTO alumnos(id_escuela, legajo, nombre, nota, email) VALUES(?,?,?,?,?)', datos)
    con.commit()

    messagebox.showinfo('STATUS', 'Registro exitoso')

    limpiar()

# Actualizar
def actualizar():
    id_escuela=int(buscar_escuelas(TRUE)[0])
    datos= id_escuela , alumnos.get(), calificacion.get(), email.get()
    cur.execute("UPDATE alumnos SET id_escuela=?, nombre=?, nota=?, email=?", datos)
    con.commit()
    messagebox.showinfo("STATUS", "Registro actualizado.")
    limpiar()

#Eliminar
def eliminar():
    respuesta=messagebox.askquestion("CONFIRMACION","Esta seguro que quiere eliminar el registro?")
    if respuesta == "yes":
            nro_legajo=legajo.get()
            cur.execute("DELETE FROM alumnos WHERE legajo="+ nro_legajo)
            con.commit()
            limpiar()

# Listado de Alumnos
def listado_alumnos():
    query='''SELECT alumnos.legajo, alumnos.nombre, escuelas.nombre, escuelas.provincia
        FROM alumnos INNER JOIN escuelas 
        ON alumnos.id_escuela = escuelas._id
        '''
    cur.execute(query)
    resultado = cur.fetchall()
    texto = ''
    for alumno in resultado:
        texto += str(alumno)
        texto += '\n'
    
    messagebox.showinfo('ALUMNOS', texto)

# Funciones Auxiliares
def buscar_escuelas(boolean):
    con = sq3.connect('my_db.db')
    cur = con.cursor()

    if boolean:
        cur.execute('SELECT _id, localidad, provincia FROM escuelas WHERE nombre = ?',(escuela.get(),))
    else:
        cur.execute('SELECT nombre FROM escuelas')

    resultado = cur.fetchall()

    escuelas = []
    for escuela_elm in resultado:
        if boolean:
            id_escuela = escuela_elm[0]
            localidad.set(escuela_elm[1])
            provincia.set(escuela_elm[2])
        
        escuelas.append(escuela_elm[0])

    con.close()
    return escuelas

def localizar_escuela(event):
    con = sq3.connect('my_db.db')
    cur = con.cursor()
    cur.execute('SELECT localidad, provincia FROM escuelas WHERE nombre = ?', (escuela.get(),))
    resultado = cur.fetchall()

    localidad.set(resultado[0][0])
    provincia.set(resultado[0][1])

    con.close()



'''
========================
    INTERFAZ GRÁFICA
========================
'''
raiz = Tk()
raiz.title("Python CRUD - Mamau")

barramenu = Menu(raiz)
raiz.config(menu = barramenu)

#Menú BBDD
bbddmenu = Menu (barramenu , tearoff = 0)
bbddmenu.add_command(label="Conectar", command=conectar)
bbddmenu.add_command(label="Listado de alumnos", command=listado_alumnos)
bbddmenu.add_command(label="Salir", command=salir)
barramenu.add_cascade(label="BBDD", menu= bbddmenu)

#Menu Limpiar
limpiarmenu = Menu(barramenu, tearoff=0)
limpiarmenu.add_command(label="Limpiar Campos", command=limpiar)
barramenu.add_cascade(label="Limpiar", menu= limpiarmenu)

#Menu Acerca de
acercamenu = Menu(barramenu, tearoff=0)
acercamenu.add_command(label="Licencia", command=licencia)
acercamenu.add_command(label="Sobre la app", command=sobre_app)
barramenu.add_cascade(label="Acerca de", menu=acercamenu)

#FrameCampos
framecampos = Frame(raiz)
framecampos.config(background='CadetBlue')
framecampos.pack()

legajo = StringVar()
alumnos = StringVar()
email = StringVar()
escuela = StringVar()
calificacion = DoubleVar()
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

# Manejo MENU desplegable escuela

# escuela_input= Entry(framecampos, textvariable=escuela)
schools = buscar_escuelas(False)
escuela.set('Seleccione...')
escuela_input = OptionMenu(framecampos, escuela, *schools, command = localizar_escuela)
escuela_input.grid(row=4, column=1, padx=10, pady=10)

#------------------------------------------------

localidad_input= Entry(framecampos, textvariable=localidad)
localidad_input.grid(row=5, column=1, padx=10, pady=10)

provincia_input= Entry(framecampos, textvariable=provincia)
provincia_input.grid(row=6, column=1, padx=10, pady=10)

#seccion Labels
legajolabel= Label(framecampos, text="Legajo", background='CadetBlue')
legajolabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

alumnoslabel= Label(framecampos, text="Alumno", background='CadetBlue')
alumnoslabel.grid(row=1, column=0, padx=10, pady=10 , sticky="w")

emaillabel= Label(framecampos, text="Email", background='CadetBlue')
emaillabel.grid(row=2, column=0, padx=10, pady=10 , sticky="w")

calificacionlabel= Label(framecampos, text="Calificación", background='CadetBlue')
calificacionlabel.grid(row=3, column=0, padx=10, pady=10 , sticky="w")

escuelalabel= Label(framecampos, text="Escuela", background='CadetBlue')
escuelalabel.grid(row=4, column=0, padx=10, pady=10 , sticky="w")

localidadlabel= Label(framecampos, text="Localidad", background='CadetBlue')
localidadlabel.grid(row=5, column=0, padx=10, pady=10 , sticky="w")

provincialabel= Label(framecampos, text="Provincia", background='CadetBlue')
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
boton_crear = Button(framebotones,text="Crear", command=crear)
boton_crear.grid(row=0, column=0, pady=10 )

#leer
boton_leer = Button(framebotones,text="Leer",command=leer)
boton_leer.grid(row=0, column=1,  pady=10 )

#actualizar
boton_actualizar = Button(framebotones,text="Actualizar", command=actualizar)
boton_actualizar.grid(row=0, column=2,   pady=10 )

#borrar
boton_borrar = Button(framebotones,text="Borrar", command=eliminar)
boton_borrar.config(bg="red",fg="white")
boton_borrar.grid(row=0, column=3, pady=10 )


#framecopy
framecopy = Frame(raiz)
framecopy.pack()

copylabel= Label(framecopy, text="Copyright 2022 - Marcia")
copylabel.config(background='LightYellow')
copylabel.grid(row=0, column=0)

raiz.mainloop()