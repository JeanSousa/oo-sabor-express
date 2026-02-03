# 1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
# Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor 
        self.ano = ano 
        Carro.carros.append(self)


    def __str__(self):
        return f"Modelo: {self.modelo} | Cor: {self.cor} | Ano: {self.ano}"
    

    def listar_carros():
        for carro in Carro.carros:
            print(f"Modelo: {carro.modelo} | Cor: {carro.cor} | Ano: {carro.ano}")



carro_1 = Carro('logan', 'prata', 2010)

print(carro_1) # Modelo: logan | Cor: prata | Ano: 2010


carro_2 = Carro('hb20', 'branco', 2014)

Carro.listar_carros()
# Modelo: logan | Cor: prata | Ano: 2010
# Modelo: hb20 | Cor: branco | Ano: 2014