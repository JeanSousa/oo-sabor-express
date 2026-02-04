# Importando o modulo inteiro de requests, ja instalado no venv
import requests


url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

# utilizando verbo http get 
response = requests.get(url)


print(response) # <Response [200]> retorna status code


if response.status_code == 200:
    # salvando os dados json em uma variavel
    # o metodo .json traz um json da resposta
    dados_json = response.json()
    print(dados_json)

else:
    print(f"O erro foi {response.status_code}")