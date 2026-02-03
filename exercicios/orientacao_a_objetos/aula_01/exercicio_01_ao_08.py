# 1 - Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

# 2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

# 3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma 
# mensagem informando se o restaurante está ativo ou inativo.

# 4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene 
# em uma variável chamada categoria.

# 5 - Altere o valor do atributo nome para 'Bistrô'.

# 6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 
# 'Pizza Place' e categoria 'Fast Food'.

# 7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

# 8 - Mude o estado da instância restaurante_pizza para ativo.

# 9 - Imprima no console o nome e a categoria da instância restaurante_praca.




class Restaurante:
    nome = ''
    categoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

# exibe metodos e atributos
# print(dir(restaurante_praca))

# exercicio 2
print(restaurante_praca.nome) # Praça

# exercicio 3
print(f"O restaurante {restaurante_praca.nome} esta Ativo" 
    if restaurante_praca.ativo else f"O restaurante {restaurante_praca.nome} está Inativo")
# resultado
# O restaurante Praça está Inativo

# Exercicio 4
categoria = Restaurante.categoria

print(categoria) # string vazia

# Exercicio 5
restaurante_praca.nome = "Bistrô"

print(restaurante_praca.nome) # Bistrô


# 6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 
# 'Pizza Place' e categoria 'Fast Food'.
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# printa atributos de uma instancia
print(vars(restaurante_pizza)) # {'nome': 'Pizza Place', 'categoria': 'Fast Food'}


# 7 - Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
print(restaurante_pizza.categoria) # Fast Food

# 8 - Mude o estado da instância restaurante_pizza para ativo.
restaurante_pizza.ativo = True 
print(vars(restaurante_pizza))
# {'nome': 'Pizza Place', 'categoria': 'Fast Food', 'ativo': True}


# 9 - Imprima no console o nome e a categoria da instância restaurante_praca.
print(restaurante_praca.nome) # Bistrô
print(restaurante_praca.categoria) # Italiana

