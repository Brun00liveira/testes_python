class Pagina:

    contador_global  = 0

    def __init__(this, nome):
        this.nome = nome
        this.numero_visita = 0
    
    def visitar(this):
        this.numero_visita += 1
        this.__class__.contador_global  += 1

    def __str__(this):
        return f'{this.nome} | {this.numero_visita}'
    
    @classmethod
    def mostrar_visitas(cls):
        return f'total de visitas {cls.contador_global}'
    
p1 = Pagina("Home")
p2 = Pagina("Sobre")

p1.visitar()
p1.visitar()
p2.visitar()

print(p1)
print(p2)
print(Pagina.mostrar_visitas())