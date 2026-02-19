from avaliacao import Avalicao

class Restaurante:

    restaurantes = []

    def __init__(this, nome, categoria):
        this._nome = nome.title()
        this._categoria = categoria.upper()
        this._ativo = False
        this._avaliacao = []
        Restaurante.restaurantes.append(this)
   
    def __str__(this):
        return f'{this._nome} | {this._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante.ativo} | {restaurante.media_avaliacao}')

    def alternar_estado(this):
        this._ativo = not this._ativo

    def receber_avaliacao(this, cliente, nota):
        avaliacao = Avalicao(cliente, nota)
        
        this._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(this):
        if len(this._avaliacao) == 0:
            return 0
        total = sum(av._nota for av in this._avaliacao)
        return total / len(this._avaliacao)


    @property
    def ativo(this):
        return 'Verdadeiro' if this._ativo else 'Falso'




