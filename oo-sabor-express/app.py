from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_mexicano = Restaurante('mexican fodd', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'japonês')

def main():
    Restaurante.listar_restaurantes()
    restaurante_mexicano.alternar_estado()
    
if __name__ == '__main__':
    main()