import os

def validate_cpf(): 
    vogais = "aeiouAEIOU"
    texto = input("Digite o seu texto: ")

    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    print(f"Quantidade de vogais: {contador}")

def main():
    os.system('cls')
    validate_cpf()

if __name__ == "__main__":
    main()
