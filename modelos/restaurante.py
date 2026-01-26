# CLASSE EM PYTHON
# classe = abstração do mundo real onde conseguimos juntar tipos diferentes
# ex
# nome = '' string
# categoria = '' string
# ativo = False boolean

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False 

# instanciando a classe / criando objeto

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()


restaurantes = [restaurante_praca, restaurante_pizza]


print(restaurantes)
# se printar diretamente vai mostrar a classe do objeto e o endereço de memoria
# [<__main__.Restaurante object at 0x783153bff4a0>, <__main__.Restaurante object at 0x783153bff4d0>]
