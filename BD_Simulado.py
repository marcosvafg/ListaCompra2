# Importando classe
from Item_Compra import Item_Compra

# Classe BD_Simulado
class BD_Simulado():
    # Metodo construtor
    def __init__(self):
        # Atributos
        self.lista_compra = []
        self.carregar_lista_compra()

    # Metodo carregar lista de compra
    def carregar_lista_compra(self):
        # Colocar aqui código para abrir arquivo
        # Cada linha do arquivo separar nome e qtde split(';')
        # Cada linha do arquivo criar um objeto de Item_Compra
        # Inserir o objeto na lista de compra

        # Remover essa parte
        item1 = Item_Compra('tomate', 10)
        item2 = Item_Compra('banana', 5)
        item3 = Item_Compra('café', 1)

        self.lista_compra.append(item1)
        self.lista_compra.append(item2)
        self.lista_compra.append(item3)
        # Remover até aqui

    def gravar_lista_compra(self):
        # Abrir o arquivo para gravação (apagar o conteúdo)
        # Percorrer a lista
        # Para cada item da lista converter em string
        # salvar no arquivo

        # Remover essa parte
        for item in self.lista_compra:
            print(item.to_string())
        # Remover até aqui

    # Metodo para retornar um Item_Compra de acordo com seu nome
    def get_item_compra(self, nome):
        # Percorrer a lista
        for item in self.lista_compra:
            # Se nome for igual
            if (item.get_nome() == nome):
                return item

        # Se não encontrar
        return None

    # Metodo para retornar lista de compras
    def get_lista_compra(self):
        return self.lista_compra







