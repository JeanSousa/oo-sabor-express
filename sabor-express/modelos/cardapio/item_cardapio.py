# IMPORTANDO O ABC DESSA FORMA EU IMPORTO OS SIMBOLOS DO MODULO ABC 
# E NÃO ELE INTEIRO, IMPORTO SOMENTE O QUE VOU UTILIZAR POR EXEMPLO 
# SE IMPORTASSE ASSIM import abc
# MEU DECORATOR TINHA QUE TER O NAMESPACE COMPLEETO ASSIM "@abc.abstractmethod"
# A CLASSE FICARIA ASSIM ItemCardapio(abc.ABC)
from abc import ABC, abstractmethod

# CLASSE ABSTRATA
class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome 
        self._preco = preco 

    @abstractmethod
    def aplicar_desconto(self):
        pass
        # AQUI PODERIA LANÇAR UMA EXCEÇÃO CASO NÃO IMPLEMENTE
        # raise NotImplementedError()



    

