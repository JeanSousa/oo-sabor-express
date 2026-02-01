# Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos. 
# Um objeto é uma instância específica de uma classe, e as classes são utilizadas para definir 
# o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.

# Por exemplo, uma classe Música poderia ter 3 atributos (que trazem as características ou propriedades de um objeto):
# nome
# artista
# duracao

# Agora é sua vez! Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo..


class Musica():
    nome = ''
    artista = ''
    duracao = ''


musica_1 = Musica()
musica_1.nome = 'Unmissible'
musica_1.artista = 'Gordon City'
musica_1.duracao = 5.45

musica_2 = Musica()
musica_2.nome = 'Bruce Lee'
musica_2.artista = 'Chris Brown'
musica_2.duracao = 4.35



musica_3 = Musica()
musica_3.nome = 'Now or Never'
musica_3.artista = 'Halsey'
musica_3.duracao = 5.20


print(dir(musica_1))

print(vars(musica_1))
print(vars(musica_2))
print(vars(musica_3))


