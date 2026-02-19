class Usuario:

    def __init__(self, nome):
        self.nome = nome
        self.status = False

    def __str__(self):
        return f'Usuário {self.nome} | {"Ativo" if self.status else "Inativo"}'
    
    def alterar_status(self):
        self.status = not self.status

usuario = Usuario("Ana")
print(usuario)

usuario.alterar_status()
print(usuario)
