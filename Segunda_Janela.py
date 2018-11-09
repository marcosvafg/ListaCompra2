# Importacao das bibliotecas
from tkinter import *
from tkinter import messagebox

# Classe Segunda_Janela
class Segunda_Janela(Toplevel):
    # Metodo construtor
    def __init__(self, parent):
        # Chamar o init da classe mae
        super().__init__(parent)
        self.geometry('200x200+200+200')
        self.title('Segunda Janela')
        self.transient(parent)
        self.grab_set()

        # Widgets
        self.btn_close = Button(self, width=10,
                                text='Sair',
                                command=self.destroy)

        # Posicionando os widgets
        self.btn_close.place(x=10, y=150)

    # Metodo para fechar a janela
    def destroy(self):
        # Janela de confirmacao
        if messagebox.askokcancel('Confirmação',
                                  'Deseja sair?'):
            super().destroy()