# 1 - Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. 
# Inicie o atributo ativo como False por padrão.


# 2 - Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o 
# titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

# 3 - Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. 
# Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

# 4 - Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. 
# Utilize propriedades, se necessário.

# 5 - Crie uma instância da classe e imprima o valor da propriedade titular.


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




# INSTANCIANDO
conta_1 = ContaBancaria('Jean Junior', 5000)
conta_2 = ContaBancaria('Kaique', 5000)


print(conta_1) # Titular: Jean Junior | Saldo: 5000
print(conta_2) # Titular: Kaique | Saldo: 5000

print(f"Antes de ativar: Conta ativa? {conta_1.ativo}") # Antes de ativar: Conta ativa? False
conta_1.ativar_conta()
print(f"Depois de ativar: Conta ativa? {conta_1.ativo}") # Depois de ativar: Conta ativa? True

# print diretamente com properties 

print(conta_1.titular) # Jean Junior
print(conta_1.saldo) # 5000
print(conta_1.ativo) # True

ContaBancaria.listar_contas()
# Titular         | Saldo           | Ativo
# Jean Junior     | 5000            | True
# Kaique          | 5000            | False


conta_3 = ContaBancaria("Fernanda", 1500)
print(f"Titular da conta 3: {conta_3.titular}") # Titular da conta 3: Fernanda



