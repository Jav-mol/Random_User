import requests

def random_user():

    URL = 'https://randomuser.me/api/'
    
    number_user = int(input('Ingrese la cantidad de usuarios: '))

    response = requests.get(url=URL, params={'results': number_user})

    if response.status_code == 200:
        payload = response.json()
        
        results = payload.get('results')

        return results
        
if __name__ == '__main__':
    pass
    