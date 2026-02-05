import requests 
import json


endpoint = "https://api.github.com/users/JeanSousa"

response = requests.get(endpoint)

if response.status_code == 200:
    response_json = response.json()

    usuario_json = {}

    nome_usuario = response_json["name"]

    print(nome_usuario)

    usuario_json[nome_usuario] = []

    usuario_json[nome_usuario].append({
        "login": response_json["login"],
        "photo": response_json["avatar_url"],
        "city": response_json["location"]
    })

    for nome_usuario, value in usuario_json.items():
        with open(f"{nome_usuario}.json", "w") as arquivo_criado:
            json.dump(value, arquivo_criado, indent=4)



else:
    print(f"Status Code Error : {response.status_code}")