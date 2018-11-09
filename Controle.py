# Importando classe
from Janela_Principal import Janela_Principal
from BD_Simulado import BD_Simulado

# Classe Controle
class Controle():
    # Metodo construtor
    def __init__(self):
        # Atributos
        self.bd = BD_Simulado()
        self.jnl = Janela_Principal(self)
        self.jnl.mainloop()

    # Metodo para retornar a lista de compra
    def get_lista_compra(self):
        return self.bd.get_lista_compra()