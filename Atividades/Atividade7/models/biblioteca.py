from livro import Livro

livro1 = Livro('O guia do mochileiro das galáxias', 'Douglas Adams', 1979)
livro2 = Livro('O restaurante no fim do universo', 'Douglas Adams', 1980)
livro3 = Livro('A vida, o universo e tudo mais', 'Douglas Adams', 1982)
livro4 = Livro('Até mais, e obrigado pelos peixes', 'Douglas Adams', 1984)
livro5 = Livro('Praticamente inofensiva', 'Douglas Adams', 1992)
livro6 = Livro('O nome do vento', 'Patrick Rothfuss', 2007)
livro7 = Livro('O temor do sábio', 'Patrick Rothfuss', 2011)

livro1.emprestar
print(livro1._disponivel)

print(Livro.verificar_disponibilidade(1979))