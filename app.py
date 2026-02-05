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

    # WITH = GARANTE QUE O ARQUIVO SERA FECHADO MESMO SE OCORRER UM ERRO
    # É A FORMA CORRETA E SEGURA DO PYTHON TRABALHAR COM ARQUIVOS ** Você não precisa chamar arquivo_restaurante.close().

    # OPEN = ABRE OU CRIA O ARQUIVO EM MODO ESCRITA "w" SE O ARQUIVO JA EXISTIR É SOBREESCRITO
    # open(NOME ARQUIVO, OPERAÇÃO W WRITE) as alias
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        # JSON.DUMP() = CONVERTE UM OBJETO PYTHON EM JSON

        # modulo json cria o arquivo passando json.dump(dados, arquivo criado com open, identação)
        json.dump(dados, arquivo_restaurante, indent=4)