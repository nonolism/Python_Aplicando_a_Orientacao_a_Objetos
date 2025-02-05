class Carro:
    def __init__(self, modelo:str, cor:str, ano:int):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        

meu_carro = Carro('Fiat Uno', 'Prata', 2004)

class Restaurante:
    def __init__(self, nome:str, categoria:str,prato_casa:str, hora_fechamento:int, ativo:bool=False ):
        self.nome = nome
        self.categoria = categoria
        self.prato_casa = prato_casa
        self.hora_fechamento = hora_fechamento
        self.ativo = ativo
        
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

        
meu_restaurante = Restaurante('Cuximi', 'Comida japonesa', True, 'Sashimi', 20)

print(meu_restaurante)

class Cliente:
    def __init__(self, nome:str, idade:int, empregado:bool = False, formado:bool = False):
        self.nome = nome
        self.idade = int
        self.empregado = empregado
        self.formado = formado
        
cliente1 = Cliente('Ruan', 20, True, False)
cliente2 = Cliente('Renato', 40, True, True)
cliente3 = Cliente('Adriano', 24, True, True)