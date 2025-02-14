class Restaurante:
    restaurantes = []
    
    def __init__(self, nome:str, categoria:str):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property #transforma o método em uma propriedade
    #necessário transformar o self.ativo em privado (colocando um _ no começo) 
    #senão o método não funciona por causa do decorator @property 
    # que não aceita atributos públicos
    def ativo(self):
        return '⌧' if self._ativo else '☐'

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")

Restaurante.listar_restaurantes()