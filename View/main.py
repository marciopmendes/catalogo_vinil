import sys
sys.path.append("./")
import tkinter as tk
from View.view_disco import DiscoVw
from View.view_musica import MusicaVw
from View.view_artista import ArtistaVw
from View.view_db import DatabaseVw


class MainVw:
    
    def __init__(self):
        self.view_artista = ArtistaVw()
        self.view_disco = DiscoVw()
        self.view_musica = MusicaVw()
        self.main_window = tk.Tk()
        self.main_window.title("Catálogo de Discos")
        self.main_window.geometry("240x530")
        self.database = DatabaseVw()
        self.artista_labelFrame = tk.LabelFrame(master=self.main_window, text='Artista')
        self.disco_labelFrame = tk.LabelFrame(master=self.main_window, text='Disco')
        self.musica_labelFrame = tk.LabelFrame(master=self.main_window, text='Musica')
        self.artista_labelFrame.grid(row=0, column=0, padx=4, pady=4)
        self.disco_labelFrame.grid(row=1, column=0, padx=4, pady=4)
        self.musica_labelFrame.grid(row=2, column=0, padx=4, pady=4)
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

    def cadastrarArtistaButton(self):
        cadastrar_artista_button = tk.Button(master=self.artista_labelFrame, text="Cadastrar Novo Artista", width=30,
                                             height=1, command=self.view_artista.cadastroArtista)
        cadastrar_artista_button.grid(row=1, column=0, padx=4, pady=4)
    
    def pesquisarArtistaButton(self):
        pesquisar_disco_button = tk.Button(master=self.artista_labelFrame, text="Pesquisar Artista", width=30, height=1,
                                           command=self.view_artista.pesquisaArtista)
        pesquisar_disco_button.grid(row=2, column=0, padx=4, pady=4)
        
    def alterarArtistaButton(self):
        alterar_artista_button = tk.Button(master=self.artista_labelFrame, text="Alterar Cadastro do Artista", width=30,
                                           height=1, command=self.view_artista.alterarArtista)
        alterar_artista_button.grid(row=3, column=0, padx=4, pady=4)
    
    def excluirArtistaButton(self):
        excluir_artista_button = tk.Button(master=self.artista_labelFrame, text="Excluir Artista", width=30, height=1,
                                           command=self.view_artista.excluirArtista)
        excluir_artista_button.grid(row=4, column=0, padx=4, pady=4, columnspan=3)
    
    def cadastrarDiscoButton(self):
        cadastrar_disco_button = tk.Button(master=self.disco_labelFrame, text="Cadastrar Novo Disco", width=30,
                                           height=1, command=self.view_disco.cadastroDisco)
        cadastrar_disco_button.grid(row=5, column=0, padx=4, pady=4)
    
    def pesquisarDiscoButton(self):
        pesquisar_disco_button = tk.Button(master=self.disco_labelFrame, text="Pesquisar Disco", width=30, height=1,
                                           command=self.view_disco.pesquisaDisco)
        pesquisar_disco_button.grid(row=6, column=0, padx=4, pady=4)
        
    def alterarDiscoButton(self):
        alterar_disco_button = tk.Button(master=self.disco_labelFrame, text="Alterar Cadastro do Disco", width=30,
                                         height=1, command=self.view_disco.alterarDisco)
        alterar_disco_button.grid(row=7, column=0, padx=4, pady=4)
    
    def excluirDiscoButton(self):
        excluir_disco_button = tk.Button(master=self.disco_labelFrame, text="Excluir Disco", width=30, height=1,
                                         command=self.view_disco.excluirDisco)
        excluir_disco_button.grid(row=8, column=0, padx=4, pady=4, columnspan=3)
        
    def cadastrarMusicaButton(self):
        cadastrar_musica_button = tk.Button(master=self.musica_labelFrame, text="Cadastrar Músicas", width=30, height=1,
                                            command=self.view_musica.cadastroMusica)
        cadastrar_musica_button.grid(row=9, column=0, padx=4, pady=4, columnspan=3)
        
    def pesquisarMusicaButton(self):
        pesquisar_musica_button = tk.Button(master=self.musica_labelFrame, text="Pesquisar Música", width=30, height=1,
                                            command=self.view_musica.pesquisaMusica)
        pesquisar_musica_button.grid(row=10, column=0, padx=4, pady=4)
        
    def alterarMusicaButton(self):
        alterar_musica_button = tk.Button(master=self.musica_labelFrame, text="Alterar Cadastro da Música", width=30,
                                          height=1, command=self.view_musica.alterarMusica)
        alterar_musica_button.grid(row=11, column=0, padx=4, pady=4)
    
    def excluirMusicaButton(self):
        excluir_musica_button = tk.Button(master=self.musica_labelFrame, text="Excluir Música", width=30, height=1,
                                          command=self.view_musica.excluirMusica)
        excluir_musica_button.grid(row=12, column=0, padx=4, pady=4, columnspan=3)
    
    def sairButton(self):
        sair_button = tk.Button(master=self.main_window, text="Sair", width=30, height=1,
                                command=self.main_window.destroy, bg="red")
        sair_button.grid(row=13, column=0, padx=4, pady=4, columnspan=3)


if __name__ == '__main__':
    app = MainVw()
    app.main_window.mainloop()
