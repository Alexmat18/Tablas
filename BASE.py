from sqlite3 import *

baseDeDatos=connect("puntoDeVenta.db")
#se crea el cursor
cr=baseDeDatos.cursor()
#se crea la ventana principal 

cr.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    cantidad INTEGER NOT NULL
)
''')