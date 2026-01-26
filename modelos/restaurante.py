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
# definindo atributos do restaurante
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'


# dir traz os métodos e atributos e como uma classe funciona
print(dir(restaurante_praca))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
#  '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ativo', 'categoria', 'nome']

# Essa função mostra um dicionario dos atributos e metodos
print(vars(restaurante_praca)) # {'nome': 'Praça', 'categoria': 'Gourmet'} aqui ele não lista o valor de ativo

print(restaurante_praca.ativo) # aqui ele lista mostrando que está armazenado mas não foi mostrado em vars

