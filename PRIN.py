from sqlite3 import * 
from tkinter import messagebox
from tkinter import *
from tkinter import ttk #libreria para trabajar con tablas
from customtkinter import *
import customtkinter
#----------------------------------------------
#funcion para cerrar la ventana principal
def cerrarVentanaPrincipal():
    app.destroy()
#--------------------------------------------
def actualizarTabla():
    for item in tabla.get_children():
        tabla.delete(item)
    cr.execute('SELECT * FROM productos')
    productos = cr.fetchall()
    for producto in productos:
        tabla.insert("", "end", values=producto)
#-----------------------------------------------------------------------------------------------------------------
#funcion para eliminar las palabras en base al ID, se crea una ventana emergente para mejor estetica
def eliminarProducto():#funcion para realizar la funcion de eliminar palabras
    def eliminar():#funcion para eliminar la palabra
        #validacion de los campos
        if IdEliminado.get() == "":
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID.")
        else:
            id_palabra = IdEliminado.get() #se guarda el numero ingresado por el usuario
            IdEliminado.delete(0, END)
            cr.execute('DELETE FROM productos WHERE id = ?', (id_palabra,))#se elimina la palabra en base al ID
            baseDeDatos.commit()#GUARDA LOS Cambios en la base de datos
            messagebox.showinfo("Accion exitosa", f"El producto con ID {id_palabra} fue eliminado con exito")#muestra un mensaje una vez se eliminó la palabra
            actualizarTabla()
            ventanaEliminar.destroy()#Se destruye la ventana emergente una vez se elimina la palabra

    # Crear ventana emergente
    ventanaEliminar = CTkToplevel(app)
    ventanaEliminar.title("Eliminar Producto")
    ventanaEliminar.grab_set()

    # Etiqueta y campo de entrada para el ID
    etiqueta1 = CTkLabel(ventanaEliminar, text="Ingrese el ID del producto a eliminar:")
    etiqueta1.grid(row=0, column=0, pady=10)
    IdEliminado = CTkEntry(ventanaEliminar)
    IdEliminado.grid(row=1, column=0, pady=5)

    # Botón para eliminar la palabra en la ventana emergente para eliminar la palabra
    botonEliminar = CTkButton(ventanaEliminar, text="Eliminar", command=eliminar)
    botonEliminar.grid(row=2, column=0, pady=10)

#---------------------------------------------
# funcion para agregar la palabra
def agregarProducto():
    # Crear ventana emergente para agregar producto
    def cerrarAgregar():
        ventanaAgregar.destroy()
    ventanaAgregar = CTkToplevel(app)
    ventanaAgregar.title("Agregar Producto")
    ventanaAgregar.grab_set()
    #------------------------------------------------
    #funcion para el boton de agragar

    def agregar():
        #validacion de los campos
        if nombrePalabra.get() == "" or precio.get() == "" or cantidad.get() == "" :
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return
        else:
            #se almacena el valor de las varibles en las cajas
            nuevaProd = str(nombrePalabra.get())
            nuevoprec = precio.get()
            cantidad1=cantidad.get()
            precio.delete(0, END)
            cantidad.delete(0, END)
            nombrePalabra.delete(0, END)
            cr.execute('''
                INSERT INTO productos (nombre, precio,cantidad)
                VALUES (?,?,?)''', (nuevaProd, nuevoprec, cantidad1))
            baseDeDatos.commit()
            messagebox.showinfo("Accion exitosa", "El producto fue agregado con exito")
            actualizarTabla()
            ventanaAgregar.destroy()
    #--------------------------------------------------------------
    ventanaAgregar.title("Agregar Producto")
    #etiqueta para dar la bienvenida
    etiqueta1=CTkLabel(ventanaAgregar, text="Agregue un producto nuevo", font=fontm)
    etiqueta1.grid(row=0, column=0, sticky="wens", columnspan=4)
    #etiqueta y entry para la palbra
    etiqueta2=CTkLabel(ventanaAgregar, text='Ingrese el nombre del producto: ', font=fontm)
    etiqueta2.grid(row=1, column=0, sticky='wens', columnspan=2)
    nombrePalabra=CTkEntry(ventanaAgregar)
    nombrePalabra.grid(row=1, column=2, sticky='wens', columnspan=4)
    #etiqueta para EL precio
    etiqueta3=CTkLabel(ventanaAgregar, text='Ingrese el precio: ', font=fontm)
    etiqueta3.grid(row=2, column=0, sticky='wens', columnspan=2)
    precio=CTkEntry(ventanaAgregar, height=5, width=30)
    precio.grid(row=2, column=2, sticky='wens', columnspan=3, pady=5, padx=3)
    #Etiqueta de la cantidad
    etiqueta4=CTkLabel(ventanaAgregar, text='Cantidad de producto disponible: ', font=fontm)
    etiqueta4.grid(row=3, column=0, sticky='wens', columnspan=2)
    cantidad=CTkEntry(ventanaAgregar, height=5, width=30)
    cantidad.grid(row=3, column=2, sticky='wens', columnspan=3, pady=5, padx=3)
    #Boton para cerrar la ventana principal
    cerrarAgregar=CTkButton(ventanaAgregar, text='Cerrar', command=cerrarAgregar)
    cerrarAgregar.grid(row=7, column=3)
    #boton de agregar
    botonAgregar = CTkButton(ventanaAgregar, text="Agregar", command=agregar)
    botonAgregar.grid(row=7, column=0)

#funcion para modificar  los datos
def moficarDatos():
    def cerrarModi():
        VentanaModificar.destroy()
    #-------------------------------------
    #creacionde  funciones para cada tipo de actualizacion
    def guardar():
        pass
    VentanaModificar=CTkToplevel(app)
    VentanaModificar.title("Eliminar Producto")
    VentanaModificar.grab_set()
    #boton de guardar
    guardarMod=CTkButton(VentanaModificar, text="Guardar")

#---------------------------------
baseDeDatos=connect("puntoDeVenta.db")
#se crea el cursor
cr=baseDeDatos.cursor()
#creacion de la  tabla
cr.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    cantidad INTEGER NOT NULL
)
''')
#se crea la ventana principal
app=CTk()
#se crea el titulo
app.title("Comerciarl los trigales")
# Crea la instancia de la fuente primero
mi_fuente = customtkinter.CTkFont(family="Arial", size=15)
fontm=mi_fuente
#--------------------------------------------------------------#funcion para hacer que la ventana se cierrre


tabla = ttk.Treeview(app, columns=("ID","Producto", "Precio","Cantidad"), show="headings")
tabla.column("ID", width=20, anchor="center")
tabla.heading("ID", text="ID")
tabla.heading("Producto", text="Producto")
tabla.heading("Precio", text="Precio")
tabla.heading("Cantidad", text="Cantidad")
tabla.grid(row=0, column=0, columnspan=3)

# Llenar la tabla con datos
cr.execute('SELECT * FROM productos')
palabras = cr.fetchall()
for palabra in palabras:
    tabla.insert("", "end", values=palabra)

#------------------------------------------------------
#boton de agregar
resul=CTkButton(app, text="Agregar", command=agregarProducto)
resul.grid(row=7, column=0, padx=10,pady=10)
#Boton para abrir la ventana de eliminar una palabra
eliminar=CTkButton(app, text="Eliminar producto", command=eliminarProducto)
eliminar.grid(row=7, column=1, padx=10,pady=10)
#Boton para cerrar la ventana principal
cerrarP=CTkButton(app, text='Cerrar', command=cerrarVentanaPrincipal)
cerrarP.grid(row=7, column=2, padx=10,pady=10)
app.mainloop()