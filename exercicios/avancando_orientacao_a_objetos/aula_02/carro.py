# 3 - Crie uma nova classe chamada Carro que herda da classe Veiculo.
# 4 - No construtor da classe Carro, utilize o método super() para chamar o construtor da 
# classe pai e atribua o atributo específico cor à classe filha.

from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor 

    def ligar(self):
        print(f"O carro {self._modelo} está ligado")
    
