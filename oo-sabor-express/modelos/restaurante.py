from modelos.avaliacao import Avaliacao

class Restaurante:
    '''classe que representa um restaurante'''
    restaurantes = []
    def __init__(self, nome:str, categoria:str):
        '''método construtor da classe Restaurante'''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
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
        
    def receber_avaliacao(self, cliente:str, nota:int):
        '''método que recebe uma avaliação de um cliente'''
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        '''método que calcula a média das avaliações do restaurante'''
        if not self._avaliacao:
            return 0
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        
        return media
        