# Importando as bibliotecas
from tkinter import *
from tkinter import messagebox
from Segunda_Janela import Segunda_Janela

# Classe Janela_Principal
class Janela_Principal(Tk):
    # Metodo construtor
    def __init__(self, controle):
        # Atributos
        self.controle = controle
        # Executar o metodo da classe mae
        super().__init__()
        # Ajustar tamanho
        self.geometry('300x300+200+200')
        # Colocar um titulo na janela
        self.title('Janela Principal')

        # Widgets da tela
        self.btn_close = Button(self, width=10,
                                text='Sair',
                                command=self.destroy)
        self.btn_ok = Button(self, width=10,
                             text='Ok',
                             command=self.btn_ok_click)
        self.lbl_ok = Label(self, text='Teste')
        self.txt_ok = Entry(self)

        # Posicionando os widgets
        self.btn_close.place(x=10, y=250)
        self.btn_ok.place(x=140, y=250)
        self.lbl_ok.place(x=140, y=200)
        self.txt_ok.place(x=140, y=150)

        # == Menu ==
        # Criando um menu
        self.menu = Menu(self)
        #Criando um item de menu e subtitens
        self.menu_principal = Menu(self.menu, tearoff=0)
        self.menu_principal.add_command(label='Segunda Janela',
                                        command=self.criar_segunda_janela)
        self.menu_principal.add_command(label='Comando 2',
                                        command=self.menu_click)
        self.menu_principal.add_command(label='Comando 3',
                                        command=self.menu_click)
        self.menu_principal.add_separator()
        self.menu_principal.add_command(label='Sair',
                                        command=self.destroy)
        self.menu.add_cascade(label='Principal',
                              menu=self.menu_principal)
        # Mostrando o menu
        self.config(menu=self.menu)


    # Metodo para fechar a janela
    def destroy(self):
        # Janela de confirmacao
        if messagebox.askokcancel('Confirmação',
                                  'Deseja sair?'):
            super().destroy()

    # Metodo para o btn_ok
    def btn_ok_click(self):
        # Recuperar a lista de compra
        lista_compra = self.controle.get_lista_compra()
        # Percorrer a lista
        for item in lista_compra:
            messagebox.showinfo('Item', item.to_string())

    # Metodo para click no item de menu
    def menu_click(self):
        messagebox.showinfo('Menu',
                            'Clicou no item de menu!')


    # Metodo para criar a segunda janela
    def criar_segunda_janela(self):
        Segunda_Janela(self)
