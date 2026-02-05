import os

# 1 - Cadastrar novo restaurante
# 2 - Criar Restaurante

# Status 1 = ativo
# Status 2 = inativo

# troca para testar dicionários (Json)

# restaurantes = ['Fogo de Chão', 'Felippi']

restaurantes = [{'id': 1 , 'cod': 'S001' ,'nome':'Ja paguei', 'categoria':'Sushi', 'ativo':False}, 
                    {'id': 2 , 'cod': 'PM001' ,'nome':'Mama Mia', 'categoria':'Pizzas e Massas', 'ativo':True},
                    {'id': 3 , 'cod': 'I001','nome':'Uga Uga', 'categoria':'Indigena', 'ativo':False}]

def finalizar_app():
    print("Finalizando o APP")

def voltar_menu_inicial():
    input('\nDigite uma tecla para voltar nas opções iniciais: ')
    main()

def exibir_titulo(request):
    os.system('cls')
    print(request)

def opcao_invalida():
    print("Opção invalida!")
    voltar_menu_inicial()

def exibir_subtitulo(texto):
    print

def verificar_cod(nome_do_restaurante):
    while True:
        cod = input(f'Digite o código do restaurante {nome_do_restaurante}: ')

        for restaurante in restaurantes:
            if cod == restaurante['cod']:
                print("Esse código já foi registrado! Tente novamente.\n")
                break
        else:
            return cod
        
def cadastrar_id():
    if len(restaurantes) == 0:
        return 1
    else:
        return restaurantes[-1]['id'] + 1

def cadastrar_novo_restaurantes():
    exibir_titulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que você deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    cod = verificar_cod(nome_do_restaurante)
    id = cadastrar_id()
    dados_do_restaurante = {'id': id,'cod':cod, 'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    restaurantes.append(dados_do_restaurante)

    voltar_menu_inicial()

def listar_restaurantes():
    exibir_titulo('Listando os restaurantes\n')

    print(f"{'ID':5} | {'Nome':20} | {'Categoria':20} | {'Status':10} | Cod")
    print('-' * 80)

    for restaurante in restaurantes:
        status = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(
            f"{restaurante['id']:<5} | "
            f"{restaurante['nome']:20} | "
            f"{restaurante['categoria']:20} | "
            f"{status:10} | "
            f"{restaurante['cod']}"
        )

    voltar_menu_inicial()


def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            message = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(message)
    if not restaurante_encontrado: 
        print("O restaurante não foi encontrado")

    voltar_menu_inicial()
   
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurantes()
        elif opcao_escolhida == 2:
           listar_restaurantes()
        elif(opcao_escolhida == 3):
            alternar_estado_restaurante()
        elif(opcao_escolhida == 4):
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    escolher_opcao()

if __name__ == '__main__':
    main()