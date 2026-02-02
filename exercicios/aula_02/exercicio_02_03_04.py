# 2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. 
# Instancie um restaurante e atribua valores aos seus atributos.

# 3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e 
# inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

# 4 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, 
# seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, cidade, delivery, ativo = False):
        self.nome = nome 
        self.categoria = categoria 
        self.cidade = cidade 
        self.delivery = delivery 
        self.ativo = ativo 

    # sobrescrita de dundle method
    def __str__(self):
        return f"nome: {self.nome} | categoria: {self.categoria} | " \
        f"cidade: {self.cidade} | delivery: {self.delivery} | ativo: {self.ativo}"
    


restaurante = Restaurante('Pizzaria Gaucho', 'Pizzaria', 'Franca-SP', True, True)

print(restaurante)