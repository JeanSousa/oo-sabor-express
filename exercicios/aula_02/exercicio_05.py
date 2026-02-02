# 5 - Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta 
# classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome, email, telefone, cidade):
        self.nome = nome 
        self.email = email 
        self.telefone = telefone 
        self.cidade = cidade 

    def __str__(self):
        return str(vars(self))
    

cliente_01 = Cliente('jean', 'jean@gmail.com', '(16) 99955-5588', 'Franca-SP')
print(cliente_01) # {'nome': 'jean', 'email': 'jean@gmail.com', 'telefone': '(16) 99955-5588', 'cidade': 'Franca-SP'}

cliente_02 = Cliente('nick', 'nick@gmail.com', '(16) 99955-5589', 'Franca-SP')
print(cliente_02) # {'nome': 'nick', 'email': 'nick@gmail.com', 'telefone': '(16) 99955-5589', 'cidade': 'Franca-SP'}