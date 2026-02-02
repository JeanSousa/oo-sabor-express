# Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 
# Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 
# Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
#  Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada 
# com base na profissão da pessoa.


class Pessoa:
    def __init__(self, nome, idade = 0, profissao = ''):
        self._nome = nome 
        self._idade = idade 
        self._profissao = profissao 

    # DUNDER METHOD
    def __str__(self):
        return f"Nome: {self._nome} | Idade: {self._idade} | Profissao: {self._profissao}"
    

    def aniversario(self):
        self._idade += 1


    # Aqui o decorator @property cria uma apresentação para um atributo
    @property
    def saudacao(self):
        if self._profissao:
            return f"Ola sou {self._nome}! Trabalho como {self._profissao}"
        else:
            return f"Ola sou {self._nome}"
        

    @property 
    def idade(self):
        return f"{self._idade} anos"
        


pessoa = Pessoa('Jean', 33, 'Programador')

# utilizando o dunder method str
print(pessoa) # Nome: Jean | Idade: 33 | Profissao: Programador

# AQUI CHAMO O PROPERTY COMO UM ATRIBUTO
print(pessoa.idade) # 33 ANOS

print(pessoa.saudacao) # Ola sou Jean! Trabalho como Programador

pessoa.aniversario() # adicionando idade

print(pessoa.idade) # 34 anos




