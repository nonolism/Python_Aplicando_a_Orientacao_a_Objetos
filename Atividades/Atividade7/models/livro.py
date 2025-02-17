class Livro:
    _livros = []
    '''Classe que representa um livro'''
    def __init__(self, titulo:str, autor:str, ano_publicacao:int):
        '''Construtor da classe'''
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro._livros.append(self)
        
    def __str__(self):
        '''Retorna uma representação em string do objeto'''
        return f"{self._titulo} - {self._autor} ({self._ano_publicacao})"
    
    @property
    def emprestar(self):
        '''Método que empresta o livro'''
        self._disponivel = False
        
    @classmethod
    def verificar_disponibilidade(cls, ano:int):
        '''Método que verifica a disponibilidade de livros de um determinado ano'''
        livros_disponiveis = []
        for livro in cls._livros:
            if livro._ano_publicacao == ano:
                livros_disponiveis.append(livro._titulo)
        return livros_disponiveis   
