class Restaurante:
    '''classe que representa um restaurante'''
    restaurantes = []
    def __init__(self, nome:str, categoria:str):
        '''método construtor da classe Restaurante'''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        '''método mágico que retorna uma representação em string do objeto'''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''o @classmethod é um decorator que transforma o método em um método de classe
        e não de instância, ou seja, ele não precisa de uma instância para ser chamado
        e sim da própria classe'''
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property 
    def ativo(self):
        '''transforma o método em uma propriedade
        necessário transformar o self.ativo em privado (colocando um _ no começo) 
        senão o método não funciona por causa do decorator @property 
        que não aceita atributos públicos'''
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        '''método que alterna o estado do restaurante entre ativo e inativo'''
        self._ativo = not self._ativo

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")

restaurante_praca.alternar_estado()

Restaurante.listar_restaurantes()