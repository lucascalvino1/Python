from tkinter import *
import sqlite3

raiz = Tk()
raiz.title="App BBDD Lucas"

#----Definicion de variables ----#

miId= IntVar()
minombre = StringVar()
miapellido = StringVar()
direcion = StringVar()
coments = StringVar()
pass_word= StringVar()


base = "Baseapp"
#------Funciones ppales ------#

def Connect():

    miConexion = sqlite3.connect(base)
    miCursor= miConexion.cursor()
    miCursor.execute('''
                     CREATE TABLE IF NOT EXISTS REGISTROS (
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     NOMBRE VARCHAR(20),
                     PASSWORD VARCHAR(30),
                     APELLIDO VARCHAR(20),
                     DIRECCION VARCHAR(50),
                     COMENTARIOS VARCHAR(100))
                     ''')
    messagebox.showinfo("Conexión","Conectado exitosamente a la BB.DD.")



def salirAplicacion():
    #valor=messagebox.askquestion("Cerrar","Deseas salir de la aplicación?")
    valor=messagebox.askokcancel("Cerrar","Deseas salir de la aplicación?")

    if valor==True:
        raiz.destroy()
        
def Borrar():
    minombre.set("")
    miId.set("")
    miapellido.set("")
    pass_word.set("")
    direcion.set("")
    coments.set("")
    
def infoAdicional():
    messagebox.showinfo("App de Lucas","Es la app de Lucas")

def avisoLicencia():
    messagebox.showwarning("Licencia","Producto sin licencia y a punto de expirar")

#---- Funciones de botones ---#    

def insert_f():
    
    
    #ID = miId.get()
    Nombre = minombre.get()
    Apellido = miapellido.get()
    password = pass_word.get()
    direccion = direcion.get()
    comment = coments.get()
    
    try:
        miConexion = sqlite3.connect(base)
        miCursor= miConexion.cursor()
        persona=Nombre,password,Apellido,direccion,comment
        miCursor.execute("INSERT INTO REGISTROS(ID,NOMBRE,PASSWORD,APELLIDO,DIRECCION,COMENTARIOS) VALUES (null,?,?,?,?,?)",(Nombre,password,Apellido,direccion,comment))
        
        
        miConexion.commit()
        messagebox.showinfo("Creado correctamente","Fue agregado a la base")
        Borrar()
    except:
        messagebox.showinfo("Error","No pudo ser agregado, revisar el código")
        pass
    
def read_f():
    
    try:
    #persona=[(miId,minombre,miapellido,pass_word,direcion,coments)]
        IDe = miId.get()
        #print(IDe)
        miConexion = sqlite3.connect(base)
        miCursor= miConexion.cursor()
        miCursor.execute("SELECT * FROM REGISTROS WHERE ID=" + str(IDe))
    
        registro=miCursor.fetchall()
    
        minombre.set(registro[0][1])
        miapellido.set(registro[0][3])
        pass_word.set(registro[0][2])
        direcion.set(registro[0][4])
        coments.set(registro[0][5])
    
    except:
        messagebox.showinfo("Error","No pudo ser leído, revisar el código o el ID")
        
        pass

def update_f():
    
    IDe = miId.get()
    Nombre = minombre.get()
    Apellido = miapellido.get()
    password = pass_word.get()
    direccion = direcion.get()
    comment = coments.get()
    
    try:
        miConexion = sqlite3.connect(base)
        miCursor= miConexion.cursor()
        persona=Nombre,password,Apellido,direccion,comment
        #miCursor.execute("UPDATE REGISTROS SET NOMBRE='"+ Nombre + "', PASSWORD='"+ password + "', APELLIDO='" + Apellido + "', DIRECCION='" + direccion + "', COMENTARIOS='" + comment + "' WHERE ID=" + str(IDe) )
        
        # ---- To avoid SQL injection USE THIS ----- #
        miCursor.execute("UPDATE REGISTROS SET NOMBRE=?, PASSWORD=?, APELLIDO=?,DIRECCION=?,COMENTARIOS=? WHERE ID =" + str(IDe) , (persona))
        
        miConexion.commit()
        messagebox.showinfo("Actualización","Info actualizada correctamente")
        
    except:
        messagebox.showinfo("Error","No pudo ser actualizado, revisar el código")
        pass
            
def delete_f():
    IDe = miId.get()
    try:
        miConexion = sqlite3.connect(base)
        miCursor= miConexion.cursor()
        
        miCursor.execute("DELETE FROM REGISTROS WHERE ID=" + str(IDe) )
        miConexion.commit()
        messagebox.showinfo("Eliminar registro","Se eliminó correctamente")
        Borrar()
        
    except:
        messagebox.showinfo("Error","No pudo ser eliminado, revisar el ID o el código")
        pass
    
    pass

    
#-----------Menu---------#


barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Conectar",command=Connect)
bbddMenu.add_command(label="Salir",command=salirAplicacion)


borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar todo",command=Borrar)
borrarMenu.add_command(label="Borrar todo pero en ingles",command=Borrar)


crudMenu = Menu(barraMenu,tearoff=0)

crudMenu.add_command(label="Create",command=insert_f)
crudMenu.add_command(label="Update",command=update_f)
crudMenu.add_command(label="Read",command=read_f)
crudMenu.add_command(label="Delete",command=delete_f)

archivoAyuda = Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)

archivoAyuda.add_command(label="Acerca de..",command=infoAdicional)

archivoAyuda.add_command(label="Reportar problema")

barraMenu.add_cascade(label="BBDD",menu=bbddMenu)

barraMenu.add_cascade(label="Borrar",menu=borrarMenu)


barraMenu.add_cascade(label="CRUD",menu=crudMenu)

barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)


#-------------------Frame principal-------------##



miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

minombre=StringVar()

CuadroId=Entry(miFrame, textvariable=miId)
CuadroId.grid(row=0,column=1,pady=10,padx=10)
CuadroId.config(fg="red",justify="left")

CuadroNombre=Entry(miFrame, textvariable=minombre)
CuadroNombre.grid(row=1,column=1,pady=10,padx=10)
CuadroNombre.config(fg="red",justify="left")

CuadroApellido=Entry(miFrame,textvariable=miapellido)
CuadroApellido.grid(row=3,column=1,pady=10,padx=10)

CuadroPassword=Entry(miFrame,textvariable=pass_word)
CuadroPassword.grid(row=2,column=1,pady=10,padx=10)
CuadroPassword.config(show="*")

CuadroDireccion=Entry(miFrame,textvariable=direcion)
CuadroDireccion.grid(row=4,column=1)

textoComentario=Entry(miFrame,textvariable=coments)
textoComentario.grid(row=5,column=1,padx=15,pady=15)

#scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
#scrollVert.grid(row=5, column=2, sticky="nsew")

#textoComentario.config(yscrollcommand=scrollVert.set)

idLabel=Label(miFrame,text="Id:")
idLabel.grid(row=0,column=0,sticky="e")

nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=1,column=0,sticky="e")

ApellidoLabel=Label(miFrame,text="Apellido:")
ApellidoLabel.grid(row=3,column=0, sticky="e")

PasswordLabel=Label(miFrame,text="Password:")
PasswordLabel.grid(row=2,column=0, sticky="e")

direccionLabel=Label(miFrame,text="Direccion:")
direccionLabel.grid(row=4,column=0,sticky="e")

comentariosLabel=Label(miFrame,text="Comentarios:")
comentariosLabel.grid(row=5,column=0,sticky="e")




    
        
        

    
#-------Botones --------#

frame2 = Frame(raiz)
frame2.pack()
botonCreate=Button(frame2, text="Create", command=insert_f)

botonCreate.grid(row=1,column=0,padx=7,pady=7)
#botonCreate.pack()



botonRead=Button(frame2, text="Read", command=read_f)

botonRead.grid(row=1,column=1,padx=7,pady=7)
#botonRead.pack()


botonUpdate=Button(frame2, text="Update", command=update_f)

botonUpdate.grid(row=1,column=2,padx=7,pady=7)
#botonUpdate.pack()

botonDelete=Button(frame2, text="Delete", command=delete_f)

botonDelete.grid(row=1,column=3,padx=7,pady=7)
#botonDelete.pack()


raiz.mainloop()