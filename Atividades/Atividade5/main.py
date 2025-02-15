class Pessoa:
    def __init__(self, nome:str='', idade:int=0, profissao:str=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        
    def __str__(self):
        return f'{self.nome} Tem {self.idade} anos de idade e sua profissão é {self.profissao}'
    
    def aniversario(self):
        self.idade += 1
    
    @property
    def saudacao(self):
        if self.profissao:
            print(f'Olá, meu nome é {self.nome} e sou {self.profissao}')
        else:
            print(f'Olá, meu nome é {self.nome}')

pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa3.aniversario()

print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)