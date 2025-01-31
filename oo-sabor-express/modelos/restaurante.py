class Restaurante:
    nome = ""
    categoria = ""
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Italiana"
if restaurante_praca.ativo:
    print(f"O restauraurante {restaurante_praca.nome} está ativo.")
else:
    print(f"O restauraurante {restaurante_praca.nome} está Inativo.")
print(restaurante_praca)
print(restaurante_praca.nome)
restaurante_praca.nome = "Bistro"

restaurante_pizza = Restaurante()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"
if restaurante_pizza.categoria == "Fast Food":
    print(True)
else:
    print(False)
restaurante_pizza.ativo = True
print(f"Nome: {restaurante_praca.nome}\nCategoria: {restaurante_praca.categoria}")

restaurantes = [restaurante_praca, restaurante_pizza]


categoria = Restaurante.categoria
