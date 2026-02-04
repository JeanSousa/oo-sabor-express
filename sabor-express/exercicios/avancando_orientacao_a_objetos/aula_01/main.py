# 7 - Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.

# 8 - Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, 
# crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

# 9 - Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

from carro import Carro
from moto import Moto


def main():
    carro_1 = Carro('Honda', 'Fit', 5)
    carro_2 = Carro('Toyota', 'Yaris', 5)
    carro_3 = Carro('Chevrolet', 'Onix', 5)

    moto_1 = Moto('Honda', 'CB600', 'Esportiva')
    moto_2 = Moto('Honda', 'Fan 160', 'Casual')
    moto_3 = Moto('Yamaha', 'R1', 'Esportiva')

    print(carro_1)
    print(carro_2)
    print(carro_3)
    print(moto_1)
    print(moto_2)
    print(moto_3)

    # Marca: Honda           | Modelo: Fit                    | ligado: False           | Portas: 5
    # Marca: Toyota          | Modelo: Yaris                  | ligado: False           | Portas: 5
    # Marca: Chevrolet       | Modelo: Onix                   | ligado: False           | Portas: 5
    # Marca: Honda           | Modelo: CB600                  | ligado: False           | Tipo: Esportiva
    # Marca: Honda           | Modelo: Fan 160                | ligado: False           | Tipo: Casual
    # Marca: Yamaha          | Modelo: R1                     | ligado: False           | Tipo: Esportiva


# definindo para rodar diretamente esse arquivo
if __name__ == '__main__':
    main()