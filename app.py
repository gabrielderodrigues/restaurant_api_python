import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
print(response)

if response.status_code == 200:
    print('Requisição bem sucedida')
    print(response.json())
else:
    print(f'Erro na requisição | Status {response.status_code}')