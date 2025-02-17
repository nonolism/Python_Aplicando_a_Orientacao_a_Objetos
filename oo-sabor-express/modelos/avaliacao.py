class Avaliacao:
    '''classe que representa uma avaliação de um restaurante'''
    def __init__(self, cliente: str, nota: float):
        '''método construtor da classe Avaliacao'''
        self._cliente = cliente
        self._nota = nota