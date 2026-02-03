# 1 - Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, 
# autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

class Livro:

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo 
        self._autor = autor 
        self._ano_publicacao = ano_publicacao
        self._disponivel = True 

# 2 - Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, 
# autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

    def __str__(self):
        return f"Titulo: {self._titulo} | Autor: {self._autor} | Ano: {self._ano_publicacao}"
    
# 3 - Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
# Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

    def emprestar(self):
        self._disponivel = False 

# 4 - Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro 
# e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano]

        if not livros_disponiveis:
            print(f"Não há livros disponiveis no ano {ano}")
            return 
        
        print(f"Livros disponiveis no ano de {ano} :\n")
        for livros in livros_disponiveis:
            print(f" - {livros}")
            



livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)
livro3 = Livro("Python Cookbook", "Samuel Developer", 2020)


print(livro1)

livro1.emprestar()

print(livro1._disponivel) # False


Livro.livros = [livro1, livro2, livro3] 

Livro.verificar_disponibilidade(2020)
# Livros disponiveis no ano de 2020 :

#  - Titulo: Data Science Fundamentals | Autor: Jane Smith | Ano: 2020
#  - Titulo: Python Cookbook | Autor: Samuel Developer | Ano: 2020


