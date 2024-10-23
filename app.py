import requests

from models.menu_item import MenuItem

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
print(response)

if response.status_code == 200:
    print('Requisição bem sucedida!')
    json_data = response.json()
    
    menu_items = []
    
    for restaurant in json_data:
        company_name = restaurant['Company']
        menu_item = MenuItem(
            company=restaurant['Company'],
            item=restaurant['Item'],
            price=restaurant['price'],
            description=restaurant['description']
        )
        menu_items.append(menu_item)
        
    for item in menu_items:
        print(item)
        
    processed_companies = set()
        
    for item in menu_items:
        if item.company not in processed_companies:
            processed_companies.add(item.company)  # Marcar a empresa como processada
            
            # Criar um arquivo para a empresa
            with open(f"{item.company}.txt", 'w', encoding='utf-8') as file:
                file.write(f"Menu for {item.company}\n")
                file.write("=" * 30 + "\n")
                # Adicionar os itens da empresa ao arquivo
                for inner_item in menu_items:
                    if inner_item.company == item.company:
                        file.write(f"{inner_item}\n")
        
else:
    print(f'Erro na requisição | Status {response.status_code}')