import os

def validate_cpf(): 
    while True:
        cpf = input("Digite o seu CPF: ")

        if not cpf.isdigit():
            print("Erro: Digite somente números.\n")
            continue
        if len(cpf) != 11:
            print("Erro: O CPF deve ter exatamente 11 dígitos.\n")
            continue
        print("CPF válido.")
        break

def main():
    os.system('cls')
    validate_cpf()

if __name__ == "__main__":
    main()
