import tkinter as tk
from View.cadastro_disco import cadastro_discoVw
from View.pesquisa_disco import pesquisa_discoVw
from View.alterar_disco import alterar_discoVw
from View.exclusao_disco import excluir_discoVw
from View.cadastro_musica import cadastro_musicaVw
from View.pesquisa_musica import pesquisa_musicaVw
from View.alterar_musica import altera_musicaVw
from View.exclusao_musica import excluir_musicaVw
from View.cadastro_artista import cadastro_artistaVw
from View.pesquisa_artista import pesquisa_artistaVw
from View.alterar_artista import alterar_artistaVw
from View.exclusao_artista import excluir_artistaVw

class mainVw:
    
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Catálogo de Discos")
        self.main_window.geometry("230x450")
        self.cadastrarArtistaButton()
        self.pesquisarArtistaButton()
        self.alterarArtistaButton()
        self.excluirArtistaButton()
        self.cadastrarDiscoButton()
        self.pesquisarDiscoButton()
        self.alterarDiscoButton()
        self.excluirDiscoButton()
        self.cadastrarMusicaButton()
        self.pesquisarMusicaButton()
        self.alterarMusicaButton()
        self.excluirMusicaButton()
        self.sairButton()

#Criação dos botões na tela principal
    def cadastrarArtistaButton(self):
        cadastrar_artista_button = tk.Button(master=self.main_window, text="Cadastrar Novo Artista", width=30, height=1, command=cadastro_artistaVw)
        cadastrar_artista_button.grid(row=1, column=0, padx=4, pady=4)
    
    def pesquisarArtistaButton(self):
        pesquisar_disco_button = tk.Button(master=self.main_window, text="Pesquisar Artista", width=30, height=1, command=pesquisa_artistaVw)
        pesquisar_disco_button.grid(row=2, column=0, padx=4, pady=4)
        
    def alterarArtistaButton(self):
        alterar_artista_button = tk.Button(master=self.main_window, text="Alterar Cadastro do Artista", width=30, height=1, command=alterar_artistaVw)
        alterar_artista_button.grid(row=3, column=0, padx=4, pady=4)
    
    def excluirArtistaButton(self):
        excluir_artista_button = tk.Button(master=self.main_window, text="Excluir Artista", width=30, height=1, command=excluir_artistaVw)
        excluir_artista_button.grid(row=4, column=0, padx=4, pady=4, columnspan=3)
    
    def cadastrarDiscoButton(self):
        cadastrar_disco_button = tk.Button(master=self.main_window, text="Cadastrar Novo Disco", width=30, height=1, command=cadastro_discoVw)
        cadastrar_disco_button.grid(row=5, column=0, padx=4, pady=4)
    
    def pesquisarDiscoButton(self):
        pesquisar_disco_button = tk.Button(master=self.main_window, text="Pesquisar Disco", width=30, height=1, command=pesquisa_discoVw)
        pesquisar_disco_button.grid(row=6, column=0, padx=4, pady=4)
        
    def alterarDiscoButton(self):
        alterar_disco_button = tk.Button(master=self.main_window, text="Alterar Cadastro do Disco", width=30, height=1, command=alterar_discoVw)
        alterar_disco_button.grid(row=7, column=0, padx=4, pady=4)
    
    def excluirDiscoButton(self):
        excluir_disco_button = tk.Button(master=self.main_window, text="Excluir Disco", width=30, height=1, command=excluir_discoVw)
        excluir_disco_button.grid(row=8, column=0, padx=4, pady=4, columnspan=3)
        
    def cadastrarMusicaButton(self):
        cadastrar_musica_button = tk.Button(master=self.main_window, text="Cadastrar Músicas", width=30, height=1, command=cadastro_musicaVw)
        cadastrar_musica_button.grid(row=9, column=0, padx=4, pady=4, columnspan=3)
        
    def pesquisarMusicaButton(self):
        pesquisar_musica_button = tk.Button(master=self.main_window, text="Pesquisar Música", width=30, height=1, command=pesquisa_musicaVw)
        pesquisar_musica_button.grid(row=10, column=0, padx=4, pady=4)
        
    def alterarMusicaButton(self):
        alterar_musica_button = tk.Button(master=self.main_window, text="Alterar Cadastro da Música", width=30, height=1, command=altera_musicaVw)
        alterar_musica_button.grid(row=11, column=0, padx=4, pady=4)
    
    def excluirMusicaButton(self):
        excluir_musica_button = tk.Button(master=self.main_window, text="Excluir Música", width=30, height=1, command=excluir_musicaVw)
        excluir_musica_button.grid(row=12, column=0, padx=4, pady=4, columnspan=3)
    
    def sairButton(self):
        sair_button = tk.Button(master=self.main_window, text="Sair", width=30, height=1, command=self.main_window.destroy)
        sair_button.grid(row=13, column=0, padx=4, pady=4, columnspan=3)

#Instrução para rodar o código
if __name__ == '__main__':
    app = mainVw()
    app.main_window.mainloop()