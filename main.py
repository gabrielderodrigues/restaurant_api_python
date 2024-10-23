from fastapi import FastAPI, Query
import requests

from models.menu_item import MenuItem

app = FastAPI()

@app.get('/api/v1/restaurants/')
def get_restaurants(restaurant_name: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        json_data = response.json()
        if restaurant_name is None:
            return {'data': json_data}
        
        menu_items = []
        
        for restaurant in json_data:
            if restaurant['Company'] == restaurant_name:
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
                processed_companies.add(item.company)
                
                with open(f"{item.company}.txt", 'w', encoding='utf-8') as file:
                    file.write(f"Menu for {item.company}\n")
                    file.write("=" * 30 + "\n")
                    for inner_item in menu_items:
                        if inner_item.company == item.company:
                            file.write(f"{inner_item}\n")
                            
        return {'data': menu_items}
    else:
        print(f'Erro na requisição | Status {response.status_code}')