# CLASSE EM PYTHON
class Restaurante:
    # atributo de classe
    restaurantes = []
    # define que os atributos serão para esse objeto referenciado no momento
    def __init__(self, nome, categoria):
        self.nome = nome 
        self.categoria = categoria
        self.ativo = False 
        # Atribuindo novo restaurante criado a lista atributo de classe
        Restaurante.restaurantes.append(self)

    # é um método especiial "DUNDER METHODS"
    # __str__ é um dos métodos que aparecem utilizando o método __dir__ , ele é o método 
    # procurado quando queremos printar uma classe, e aparecerá como foi implementado,
    # por default ele tem o endereço de memória
    # <__main__.Restaurante object at 0x799f9b3ff830>

    # self = referencia da instancia atual que estamos utilizando no momento
    # retorna o atributo nome e categoria
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    # POSSO DEFINIR O STR ASSIM E COMO VARS RETORNA UM DICT TRANSFORMO ELE EM STRING
    # def __str__(self):
    #     return str(vars(self))

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')





# instanciando a classe / criando objeto
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
# Praça | Gourmet | False
# Pizza Express | Italiana | False


# vars ira mostrar os atributos em forma de dicionario
# print(vars(restaurante_praca)) # {'nome': 'Praça', 'categoria': 'Gourmet', 'ativo': False}
# print(vars(restaurante_pizza)) # {'nome': 'Pizza Express', 'categoria': 'Italiana', 'ativo': False}

# dir traz os métodos e atributos e como uma classe funciona
# print(dir(restaurante_praca)) # __init__ = metodo construtor
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
#  '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ativo', 'categoria', 'nome']

