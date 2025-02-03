class Restaurante:
    def __init__(self, nome:str, categoria:str):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")

restaurantes = []

print(restaurante_pizza)
print(restaurante_praca)