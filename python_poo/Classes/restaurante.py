class Restaurante:

    restaurantes = []

    def __init__(this, nome, categoria):
        this._nome = nome.title()
        this._categoria = categoria.upper()
        this._ativo = False
        Restaurante.restaurantes.append(this)
   
    def __str__(this):
        return f'{this._nome} | {this._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante.ativo}')

    def alternar_estado(this):
        this._ativo = not this._ativo


    @property
    def ativo(this):
        return 'Verdadeiro' if this._ativo else 'Falso'

restaurante1 = Restaurante("barbacoa", "Churrascaria")
restaurante1.alternar_estado()
restaurante2 = Restaurante("pizza 1", "Pizzaria")

Restaurante.listar_restaurantes()