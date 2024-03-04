from config import password, user
import pymysql

DROP_TABLE = """ DROP TABLE IF EXISTS users; """

USERS_TABLE = """
    CREATE TABLE IF NOT EXISTS users(
        user_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        city VARCHAR(50) NOT NULL,
        country VARCHAR(50) NOT NULL        
    );
"""

def create_table(connect):
    with connect.cursor() as cursor:
        
            cursor.execute(USERS_TABLE)            
            connect.commit()

def drop_table():
    connect = create_connection()
    
    with connect.cursor() as cursor:
            
            cursor.execute(DROP_TABLE)            
            connect.commit()

def create_connection():
    try:
        global connect    
        if 'connect' in globals():
            print('Conexion reutilizada')
            create_table(connect)        
            #print(connect)
            return connect

        else:    

            connect = pymysql.Connect(
                    host = "127.0.0.1",
                    port = 3306,
                    user = user,
                    password = password,
                    db = 'Proyectos'
                )
            create_table(connect)
            print('Conexion creada')
            return connect
    except Exception as e:
        print(f'Error - create connection - : {e}')