# 8 - Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, 
# instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

from exercicio_01 import Livro

livro_main1 = Livro("Python para Iniciantes", "Carlos Coder", 2021)
livro_main2 = Livro("Web Development Essentials", "Laura Developer", 2023)

# print utilizando o metodo DUNDER METHOD (metodos com dois underescore) __str__
print(livro_main1)
print(livro_main2)