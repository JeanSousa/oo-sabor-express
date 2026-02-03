from modelos.cardapio.item_cardapio import ItemCardapio

# prato é herança de item cardapio, herda metodos e atributos da superclasse
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        # classe prato utiliza metodos e atributos da classe superclasse
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return self._nome 