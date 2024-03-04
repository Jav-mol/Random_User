from api import random_user
from bd import create_connection

class User():
    
    def cargar_usuario(self, first, last, age, city, country):
        connection = create_connection()
        try:            
            with connection.cursor() as cursor:

                    query = "INSERT INTO users (first_name, last_name, age, city, country) VALUES (%s,%s,%s,%s,%s)"
                    values = [first,last, age, city, country]

                    cursor.execute(query, values)
                    connection.commit()
        except Exception as e:
            print(f'Error - Cargar usuarios - : {e}')

    def agregar_usuario(self):
        result = random_user()
        try:
            for user in range(len(result)):

                first = result[user]['name'].get('first')
                last = result[user]['name'].get('last')
                age = result[user]['dob'].get('age')
                city = result[user]['location'].get('city')
                country = result[user]['location'].get('country')

                self.cargar_usuario(first,last,age,city,country)
        except Exception as e:
            print(f'Error - Agregar usuarios - : {e}')
        
    def listar_usuarios(self):
        try:
            connection = create_connection()
            query = "SELECT * FROM users"

            with connection.cursor() as cursor:
                cursor.execute(query)

                for user in cursor.fetchall():
                    print(user)

        except Exception as e:
            print(f'Error - Listar usuarios -: {e}')
