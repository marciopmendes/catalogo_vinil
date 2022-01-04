import tkinter as tk
from tkinter import ttk

class cadastro_artistaVw:
    
    def __init__(self):
        self.cadastroArtista()
    
    def cadastroArtista(self):
        cadastro_artista_window = tk.Toplevel()
        cadastro_artista_window.title("Cadastro de Artistas")
        cadastro_artista_window.geometry("250x70")
        
        #Criação do formulário de cadastro
        artista_label = ttk.Label(master=cadastro_artista_window, text='Nome do Artista')
        artista_label.grid(row=1, column=0, padx=4, pady=4)
        
        artista = tk.StringVar()
        artista_entry = ttk.Entry(master=cadastro_artista_window, textvariable=artista)
        artista_entry.grid(row=1, column=1, padx=4, pady=4)
        
        salvar_button = tk.Button(master=cadastro_artista_window, text="Salvar", width=33, height=1)
        salvar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=2)
        """esse botão executa a query pra salvar no banco"""