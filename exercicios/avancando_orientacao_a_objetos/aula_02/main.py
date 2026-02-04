# 5 - Em um arquivo chamado main.py, importe a classe Carro.
from carro import Carro

carro_1 = Carro('Honda', 'Accord', 'Preto')
carro_2 = Carro('Toyota', 'Supra', 'Vermelho')
carro_3 = Carro('Nissan', 'Skyline', 'Azul')

def main():
    carro_1.ligar()
    carro_2.ligar()
    carro_3.ligar()


if __name__ ==  '__main__':
    main()