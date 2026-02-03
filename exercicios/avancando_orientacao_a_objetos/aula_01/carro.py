# 3 - Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. 
# No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade 
# de portas do carro.

# 4 - Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro 
# que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.

# 5 - Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. 
# Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.

from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas 

    # PARA EXTENDER UM METODO DA SUPER CLASSE UTILIZO "super().__str__()"
    def __str__(self):
        return f"{super().__str__().ljust(15)} | Portas: {self._portas}"
