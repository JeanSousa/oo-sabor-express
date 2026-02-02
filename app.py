# AO IMPORTAR É CRIADO O PYCACHE, É UM CACHE DOS MODULOS IMPORTADOS
# DIRETORIO QUE O PYTHON CRIA QUE ARMAZENA OS ARQUIVOS COMPILADO EM BITECODE
# EXTENSAO pyc 
from modelos.restaurante import Restaurante



restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()





# 🔹 __name__ == "__main__"
# ➜ arquivo executado diretamente

# 🔹 __name__ != "__main__"
# ➜ arquivo importado

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()


