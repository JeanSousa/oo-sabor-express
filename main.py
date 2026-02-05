# importando FastAPI do modulo
# importando tambem Query do modulo para trabalhar com query params
from fastapi import FastAPI, Query
import requests

# criando um objeto do fastapi ele registra as rotas aqui com o decorator
# no uvicorn temos que apontar para esse objeto assim
# uvicorn main:app --reload
app = FastAPI()


# usando decorator para criar rota get
@app.get('/api/hello')
def hello_world():
    # docstring que aparecera no endpoint /docs
    '''
    Endpoint que exibe mensagem incrivel do mundo da programação
    '''
    return {"Hello":"World"}


@app.get('/api/restaurantes/')
# recebendo argumento restaurante do tipo string 
# iremos trabalhar com Query param então  importo query do modulo fastapi
# Query(valor default none)
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        # salvando os dados json em uma variavel
        # o metodo .json traz um json da resposta
        dados_json = response.json()

        if restaurante is None:
            return {"Dados" : dados_json}

        dados_restaurante = []

        for item in dados_json:
            if item["Company"] == restaurante:

                # adicionando itens ao dicionario para cada restaurante
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })


        return {'Restaurante' : restaurante, 'Cardapio': dados_restaurante}

    else:
        return {'Erro':f'{response.status_code} - {response.text}'}