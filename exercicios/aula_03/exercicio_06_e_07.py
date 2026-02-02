# 6 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. 
# Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

class ContaBancaria:
    contas = []

    def __init__(self, titular, saldo):
        self._titular = titular 
        self._saldo = saldo 
        self._ativo = False 
        ContaBancaria.contas.append(self)

    
    def __str__(self):
        return f"Titular: {self._titular} | Saldo: {self._saldo}"
    

    # DEFININDO PROPERTIES QUE É UMA FORMA DE APRESENTAR OS ATRIBUTOS
    @property
    def titular(self):
        return self._titular 
    
    @property
    def saldo(self):
        return self._saldo 
    
    @property 
    def ativo(self):
        return self._ativo
    
    @classmethod
    def listar_contas(cls):
        print(f"{'Titular'.ljust(15)} | {'Saldo'.ljust(15)} | {'Ativo'}")
        for conta in cls.contas:
            print(f'{conta.titular.ljust(15)} | {str(conta.saldo).ljust(15)} | {conta.ativo}')
    
    
    def ativar_conta(self):
        self._ativo = True 


# 6 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. 
# Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, nome, idade, telefone, cpf, profissao):
        self._nome = nome 
        self._idade = idade 
        self._telefone = telefone 
        self._cpf = cpf 
        self._profissao = profissao 


        # 7) Crie um método de classe para a conta `ClienteBanco`.
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaria(titular, saldo_inicial)
        return conta

cliente1 = ClienteBanco("Ana", 30, "16995588855", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "16995588855", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "16995588855", "111.222.333-44", "Frontend")

# Exemplo de uso do metodo de classe
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")
# Conta de Ana criada com saldo inicial de R$2000