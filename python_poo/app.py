
from restaurante import Restaurante
from cardapio.prato import Prato
from cardapio.bebida import Bebida

restaurante1 = Restaurante("barbacoa", "Churrascaria")
bebida1 = Bebida("Coca-cola", 5.00, "500ml")
bebida1.aplicar_desconto()
prato1 = Prato("Picanha", 50.00, "Picanha suculenta com tempero especial")
prato1.aplicar_desconto()
restaurante1.adicionar_no_cardapio(bebida1)
restaurante1.adicionar_no_cardapio(prato1)

def main():
    restaurante1.exibir_cardapio

if __name__ == "__main__":
    main()