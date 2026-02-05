# importando FastAPI do modulo
from fastapi import FastAPI

# criando um objeto do fastapi
app = FastAPI()


# usando decorator app para criar rota get
@app.get('/api/hello')
def hello_world():
    return {"Hello":"World"}
