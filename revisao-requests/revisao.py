import requests 
import json

endpoint = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(endpoint)

if response.status_code == 200:
    response_json = response.json()

    restaurante_itens = {}
    
    for item in response_json:
        nome_restaurante = item["Company"]
        if nome_restaurante not in restaurante_itens:
            restaurante_itens[nome_restaurante] = []

        restaurante_itens[nome_restaurante].append({
            "item": item["Item"],
            "price": item["price"],
            "description": item["description"]
        })


    print(restaurante_itens["Pizza Hut"])    

else:
    print(f"Erro : {response.status_code}")


for key, value in restaurante_itens.items():
    nome_arquivo = f"{key}.json"
    # aqui abro um arquivo em modo escrita
    with open(nome_arquivo, "w") as arquivo_restaurante:
        json.dump(value, arquivo_restaurante, indent=4)
        


