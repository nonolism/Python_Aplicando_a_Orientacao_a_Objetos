class Musica:
    def __init__(self, nome:str, artista:str, duracao:int):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        
        
musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)