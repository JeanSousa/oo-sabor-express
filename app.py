# Importando o modulo inteiro de requests, ja instalado no venv
import requests
import json


url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

# utilizando verbo http get 
response = requests.get(url)


print(response) # <Response [200]> retorna status code


if response.status_code == 200:
    # salvando os dados json em uma variavel
    # o metodo .json traz um json da resposta
    dados_json = response.json()
    
    # dicionario
    dados_restaurante = {}

    for item in dados_json:
        nome_do_restaurante = item['Company']

        # verificando se o nome do restaurante não existe no dicionario
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        # adicionando itens ao dicionario para cada restaurante
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })


    # printando apenas um restaurante
    print(dados_restaurante['McDonald’s'])

else:
    print(f"O erro foi {response.status_code}")

# for key, value 
for nome_do_restaurante, dados in dados_restaurante.items(): # items do restaurante
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    # criação do arquivo 
    # open(NOME ARQUIVO, OPERAÇÃO W WRITE) as alias
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        # modulo json cria o arquivo passando os dados, o arquivo do open e identação
        json.dump(dados, arquivo_restaurante, indent=4)