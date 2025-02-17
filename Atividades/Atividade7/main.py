from models.livro import Livro

def main():
    '''Função principal'''
    livro1 = Livro('O Senhor dos Anéis', 'J. R. R. Tolkien', 1954)
    livro2 = Livro('Harry Potter e a Pedra Filosofal', 'J. K. Rowling', 1997)
    print(livro1)
    print(livro2)
    
    livro3 = Livro('O Hobbit', 'J. R. R. Tolkien', 1937)
    livro3.emprestar
    print(livro3._disponivel)
    
    print(Livro.verificar_disponibilidade(1954))
    
if __name__ == '__main__':
    main()