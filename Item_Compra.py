# Classe Item_Compra
class Item_Compra():
    # Metodo construtor
    def __init__(self, nome, qtde):
        # Atributos
        self.nome = nome
        self.qtde = qtde

    # Metodo que converte a classe em texto
    def to_string(self):
        return self.nome + ';' + str(self.qtde)

    # Metodo para retornar o nome
    def get_nome(self):
        return self.nome

    # Metodo para retornar a qtde
    def get_qtde(self):
        return self.qtde