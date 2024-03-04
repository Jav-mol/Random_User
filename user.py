from api import random_user
from bd import create_connection

class User():
    result = random_user()
    connection = create_connection()
        
    def cargar_usuario(self, first, last, age, city, country):
        
        with self.connection.cursor() as cursor:
                
                query = "INSERT INTO users (first_name, last_name, age, city, country) VALUES (%s,%s,%s,%s,%s)"
                values = [first,last, age, city, country]
                
                cursor.execute(query, values)
                self.connection.commit()
            
    def agregar_usuario(self):
    
        for user in range(len(self.result)):
            
            first = self.result[user]['name'].get('first')
            last = self.result[user]['name'].get('last')
            age = self.result[user]['dob'].get('age')
            city = self.result[user]['location'].get('city')
            country = self.result[user]['location'].get('country')
            
            self.cargar_usuario(first,last,age,city,country)
                
    #def __str__(self) -> str:
    #    return f'Usuario: {self.name} - {self.last_name} Age: {self.age} City: {self.city} Country: {self.country}'

