import os

def conta():
    valor_conta = float(input("Digite o valor da conta: R$ "))
    
    valor_gorjeta = valor_conta * 0.10
    valor_total = valor_conta + valor_gorjeta

    print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
    print(f"Total a pagar: R$ {valor_total:.2f}")

def main():
    os.system('cls')
    conta()

if __name__ == "__main__":
    main()
