# CLASSE EM PYTHON
class Restaurante:
    # atributo de classe
    restaurantes = []
    # define que os atributos serão para esse objeto referenciado no momento
    def __init__(self, nome, categoria):
        self.nome = nome 
        self.categoria = categoria
        # ATIVO ESTA PROTECTED PRA NÃO DAR PROBLEMA COM A PROPERTY ATIVO DE MESMO NOME
        self._ativo = False 
        # Atribuindo novo restaurante criado a lista atributo de classe
        Restaurante.restaurantes.append(self)

    # é um método especiial "DUNDER METHODS" (métodos com duplo sublinhado)
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
        # Aqui abro chaves para fazer a operação no print
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            # ljust ajusta para ocupar no maximo 25 colunas
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')


    # O DECORATOR PROPERTY MODIFICA COMO UM ATRIBUTO É LIDO NO PYTHON (É COMO SE FOSSE UM PRESENTER)
    @property
    def ativo(self):
        # AQUI ESTAMOS RETORNANDO O CHECK MAS NO MUNDO REAL FAZEMOS SOMAS E ETC
        return "☒" if self._ativo == True else "☐"
    
    

    # OBS: SE O ATRIBUTO FOR PUBLICO IRA LANÇAR ESSE ERRO
    # AttributeError: property 'ativo' of 'Restaurante' object has no setter
    # DA O ERRO PORQUE NO CONSTRUTOR ELE TENTA ACESSAR A PROPERTY ATIVO AI DA UMA RECURSAO


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

