# AO IMPORTAR É CRIADO O PYCACHE, É UM CACHE DOS MODULOS IMPORTADOS
# DIRETORIO QUE O PYTHON CRIA QUE ARMAZENA OS ARQUIVOS COMPILADO EM BITECODE
# EXTENSAO pyc 
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato 



restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')
# restaurante_mexicano.alternar_estado()

# CRIANDO UMA AVALIAÇÃO 
# restaurante_praca.receber_avaliacao('Gui', 10)
# restaurante_praca.receber_avaliacao('Lais', 8)
# restaurante_praca.receber_avaliacao('Emy', 2)

# CRIANDO UMA BEBIDA 
bebida_suco = Bebida('Suco de melancia', 5.00, 'grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')



# 🔹 __name__ == "__main__"
# ➜ arquivo executado diretamente

# 🔹 __name__ != "__main__"
# ➜ arquivo importado

def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()


