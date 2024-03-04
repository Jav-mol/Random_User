from user import User
from bd import drop_table

def insert_user():
    User().agregar_usuario()

def option_invalid():
    print('Ingrese una opcion valida')

def listar_usuarios():
    User().listar_usuarios()

def quit():
    return True

options = """1) Agregar usuarios
2) Borrar tabla
3) Listar Usuarios
4) Salir 
=> """

functions = {
    '1':insert_user,
    '2':drop_table,
    '3':listar_usuarios,
    '4':quit
}

while True:
    option = input(options)
    
    funcion = functions.get(option, option_invalid)
    
    if funcion():
        break
    
    