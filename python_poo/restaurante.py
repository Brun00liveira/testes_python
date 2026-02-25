from avaliacao import Avalicao
from cardapio.item_cardapio import ItemCardapio
from cardapio.bebida import Bebida
from cardapio.prato import Prato
class Restaurante:

    restaurantes = []

    def __init__(this, nome, categoria):
        this._nome = nome.title()
        this._categoria = categoria.upper()
        this._ativo = False
        this._avaliacao = []
        this._cardapio = []
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

    # def adicionar_bebida_no_cardapio(self, bebida):
    #     self._cardapio.append(bebida)

    # def adicionar_comida_no_cardapio(self, comida):
    #     self._cardapio.append(comida)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do {self._nome}:\n')

        for i, item in enumerate(self._cardapio, start=1):

            if isinstance(item, Prato):
                mensagem = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco:.2f} | Descrição: {item._descricao}'
            
            elif isinstance(item, Bebida):
                mensagem = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco:.2f} | Tamanho: {item._tamanho}'
            
            print(mensagem)