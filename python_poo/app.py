
from restaurante import Restaurante
from cardapio.prato import Prato
from cardapio.bebida import Bebida

restaurante1 = Restaurante("barbacoa", "Churrascaria")
bebida1 = Bebida("Coca-cola", 5.00, "500ml")
prato1 = Prato("Picanha", 50.00, "Picanha suculenta com tempero especial")

def main():
    print(bebida1)
    print(prato1)
if __name__ == "__main__":
    main()