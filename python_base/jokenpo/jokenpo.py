import os
import random

def jokenpo(): 
    computador = [
        {'name': 'Pedra', 'cod': 1},
        {'name': 'Papel', 'cod': 2},
        {'name': 'Tesoura', 'cod': 3}
    ]
    
    while True:
        entrada = input("Escolha (1-Pedra, 2-Papel, 3-Tesoura): ")

        if not entrada.isdigit():
            print("A resposta tem que ser um número")
            continue

        escolha = int(entrada)
        jogador = escolhaJogador(escolha)

        if jogador is None:
            continue

        pc = escolhaComputador(computador)
        print(f"Computador escolheu {pc['name']}")

        getVencedor(jogador, pc['cod'])
        break


def getVencedor(jogador, computador):
    if jogador == computador:
        print("Empate!")
    elif (
        (jogador == 1 and computador == 3) or
        (jogador == 3 and computador == 2) or
        (jogador == 2 and computador == 1)
    ):
        print("Você Ganhou!")
    else:
        print("Você Perdeu!")


def escolhaComputador(computador):
    return random.choice(computador)


def escolhaJogador(escolha):
    if escolha == 1:
        print("Você escolheu Pedra")
        return 1
    elif escolha == 2:
        print("Você escolheu Papel")
        return 2
    elif escolha == 3:
        print("Você escolheu Tesoura")
        return 3
    else:
        print("Opção não disponível")
        return None


def main():
    os.system('cls')
    jokenpo()

if __name__ == "__main__":
    main()
