class Musica:
    # atributo de classe para cadastrar todas as musicas em uma unica lista
    # atributo de classe é compartilhado entre as instanicas
    musicas = []

    # utilizo o self pois os atributos são da atual instancia 
    def __init__(self, nome, artista, duracao):
        # atributos com encapsulamento publico, podendo ser acessados sem passar por metodos dessa classe
        self.nome = nome 
        self.artista = artista 
        self.duracao = duracao 
        # acesso o atributo de classe diretamente por ela
        # e insiro um novo objeto na lista
        Musica.musicas.append(self)

    def __str__(self):
        # vars retorna os atributos da atual instancia como dict
        # e depois faço o casting para string
        return str(vars(self))
    
    # aqui não uso o self pois é um metodo que não se aplica a uma única instancia
    # é um metodo que usa um atributo de classe
    def listar_musicas():
        for musica in Musica.musicas:
            print(f"{musica.nome} | {musica.artista} | {musica.duracao}")
        


musica_1 = Musica("forever", "Chris Brown", 3.45)
# esse print utiliza um DUNDER METHODS método com duplo underscore
# por default ele guarda o endereço da variavel que foi atribuida a instancia
# mas podemos fazer o override de como representar a classe em string
print(musica_1) # {'nome': 'forever', 'artista': 'Chris Brown', 'duracao': 3.45}


musica_2 = Musica("in Bloom", "Metalica", 4.05)

Musica.listar_musicas()
# forever | Chris Brown | 3.45
# in Bloom | Metalica | 4.05


    


    





