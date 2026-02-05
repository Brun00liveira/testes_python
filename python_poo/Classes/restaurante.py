class Restaurante:

    restaurantes = []

    def __init__(this, nome, categoria):
        this.nome = nome
        this.categoria = categoria
        this.ativo = False
        Restaurante.restaurantes.append(this)
   
    def __str__(this):
        return f'{this.nome} | {this.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante1 = Restaurante("Barbacoa", "Churrascaria")
restaurante2 = Restaurante("Pizza 1", "Pizzaria")

Restaurante.listar_restaurantes()