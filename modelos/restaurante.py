from modelos.avaliacao import Avaliacao

# CLASSE EM PYTHON
class Restaurante:
    # atributo de classe
    restaurantes = []
    # define que os atributos serão para esse objeto referenciado no momento
    def __init__(self, nome, categoria):
        # .title() para a primeira letra ser maiuscula, também poderia ser .capitalize()
        self._nome = nome.title()
        self._categoria = categoria.upper() # upper todas as letras maiúsculas
        # ATIVO ESTA PROTECTED PRA NÃO DAR PROBLEMA COM A PROPERTY ATIVO DE MESMO NOME
        self._ativo = False 

        # CRIAMOS A AVALIACAO NA CRIACAO DO RESTAURANTE, NÃO É RECEBIDA COMO PARAMETRO
        self._avaliacao = []


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
        return f'{self._nome} | {self._categoria}'

    # POSSO DEFINIR O STR ASSIM E COMO VARS RETORNA UM DICT TRANSFORMO ELE EM STRING
    # def __str__(self):
    #     return str(vars(self))

    # CLASS METHOD É UM DECORATOR PARA DIZER QUE SE TRATA DE UM MÉTODO DE CLASSE
    # POR CONVENÇÃO ELE TEM O ARGUMENTO cls QUE REPRESENTA A PROPRIA CLASSE
    @classmethod
    def listar_restaurantes(cls):
        # Aqui abro chaves para fazer a operação no print
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')

        # AQUI O cls É A MESMA COISA QUE A CLASSE COM O METODO RESTAURANTES "Restaurante.restaurantes"
        for restaurante in cls.restaurantes:
            # ljust ajusta para ocupar no maximo 25 colunas
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')


    # O DECORATOR PROPERTY MODIFICA COMO UM ATRIBUTO É LIDO NO PYTHON (É COMO SE FOSSE UM PRESENTER)
    @property
    def ativo(self):
        # AQUI ESTAMOS RETORNANDO O CHECK MAS NO MUNDO REAL FAZEMOS SOMAS E ETC
        return "☒" if self._ativo == True else "☐"
    # OBS: SE O ATRIBUTO FOR PUBLICO IRA LANÇAR ESSE ERRO
    # AttributeError: property 'ativo' of 'Restaurante' object has no setter
    # DA O ERRO PORQUE NO CONSTRUTOR ELE TENTA ACESSAR A PROPERTY ATIVO AI DA UMA RECURSAO

    def alternar_estado(self):
        # PEGA A LOGICA CONTRARIA SE ESTA ATIVO VAI FICAR INANTIVO
        self._ativo = not self._ativo


    def receber_avaliacao(self, cliente, nota):
        # crio uma instancia de avaliação para colocar na lista
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    # transformo em uma property porque vai ser acessado como um atributo 
    # pois não recebe parametros e se parecee mais com um atributo
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        # arredondando com round 1 casas decimais da media
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media


# instanciando a classe / criando objeto
# restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_praca.alternar_estado() # vai ficar com estado true pois era false

# restaurante_praca.ativo =  True;
# SE TENTAR ALTERAR ASSIM DA ERRO, POIS NÃO EXISTE SETTER PARA ELE
# POIS ELE É ENCAPSULADO COMO PROTEGIDO
# AttributeError: property 'ativo' of 'Restaurante' object has no setter

# restaurante_pizza = Restaurante('pizza Express', 'Italiana')


# Aqui não precisou criar uma instancia 
# é um método da classe
# Restaurante.listar_restaurantes()
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

