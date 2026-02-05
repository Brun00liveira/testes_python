import os

def gerador_senha(): 
   
    while True:
        senha = input("Quantas caracteres: ")
        caractere_especial = "!@#$%&*_-=+"
        if not any(char.isdigit() for char in senha):
            print("A senha precisa ter pelo menos um número. ")
            continue
        if not any(char.isupper() for char in senha):
            print("A senha precisa ter pelo menos um maiúscula. ")
            continue
        if not any(char.islower() for char in senha):
            print("A senha precisa ter pelo menos um minúscula. ")
            continue
        if not any(char in caractere_especial for char in senha):
            print("A senha precisa ter pelo menos um caractere especial. ")
            continue
        else:
            print(f"Sua senha é: {senha}")

def main():
    os.system('cls')
    gerador_senha()

if __name__ == "__main__":
    main()
