class ContaBancaria:
    '''Classe que representa uma conta bancária'''
    def __init__(self, titular:str, saldo:float):
        '''Construtor da classe ContaBancaria'''
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        
    def __str__(self):
        '''Método mágico que retorna uma representação em string do objeto'''
        return f"Titular: {self.titular.ljust(25)} | Saldo: {self.saldo}"
    
    @classmethod
    def ativar_conta(cls, conta):
        '''Método de classe que ativa a conta'''
        conta._ativo = True
    
#     Getters    

    @property
    def titular(self):
        '''getter do atributo titular'''
        return self._titular

    @property
    def saldo(self):
        '''getter do atributo saldo'''
        return self._saldo
    
    @property
    def ativo(self):
        '''getter do atributo ativo'''
        return self._ativo
    
    
conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 2000)

print(conta1)
print(conta2)

conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")

conta4 = ContaBancaria("Ana", 500)
print(f'O titular da conta 4 é: {conta4.titular}')

class ClienteBanco:
    '''Classe que representa um cliente de banco'''
    def __init__(self, nome:str, idade:int, endereco:str, cpf:str, profissao:str):
        '''Construtor da classe ClienteBanco'''
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._cpf = cpf
        self._profissao = profissao

    @classmethod
    def criar_conta(cls, titular:str, saldo:float):
        '''Método de classe que cria uma conta bancária para o cliente'''
        conta = ContaBancaria(titular, saldo)
        return conta
        

#     Getters

    @property
    def nome(self):
        '''getter do atributo nome'''
        return self._nome

    @property
    def idade(self):
        '''getter do atributo idade'''
        return self._idade

    @property
    def endereco(self):
        '''getter do atributo endereco'''
        return self._endereco

    @property
    def cpf(self):
        '''getter do atributo cpf'''
        return self._cpf

    @property
    def profissao(self):
        '''getter do atributo profissao'''
        return self._profissao
    
cliente1 = ClienteBanco("João", 30, "Rua A, 123", "123.456.789-00", "Engenheiro")
cliente2 = ClienteBanco("Maria", 25, "Rua B, 456", "987.654.321-00", "Médica")
cliente3 = ClienteBanco("Carlos", 40, "Rua C, 789", "456.789.123-00", "Professor")

conta_cliente1 = ClienteBanco.criar_conta(cliente1.nome, 1000)
print(f'Conta de {cliente1.nome} criada com saldo inicial de R$ {conta_cliente1.saldo}')