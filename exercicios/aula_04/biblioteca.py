# 5 - Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

# 6 - No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima s
# e o livro está disponível ou não após o empréstimo.

# 7 - No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter 
# a lista de livros disponíveis publicados em um ano específico.

# 8 - Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, 
# instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.


from exercicio_01 import Livro

# 
livro = Livro('Bom dia veronica', 'Rafael Pontes', 2018)

livro.emprestar()

# adicionando o novo livro criado a lista de livros
Livro.livros += [livro]

def main():
    print(livro._disponivel) # False

    Livro.verificar_disponibilidade(2018)

if __name__ == '__main__':
    main()