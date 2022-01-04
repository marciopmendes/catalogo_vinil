import tkinter as tk
from tkinter import ttk

class pesquisa_artistaVw:
    
    def __init__(self):
        self.pesquisaArtista()
    
    def pesquisaArtista(self):
        pesquisar_window = tk.Toplevel()
        pesquisar_window.title("Pesquisar Artistas")
        pesquisar_window.geometry("255x320")
        
        pesquisar_label = ttk.Label(master=pesquisar_window, text='Nome do Artista:')
        pesquisar_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        artista = tk.StringVar()
        artista_entry = tk.Entry(master=pesquisar_window, textvariable=artista)
        artista_entry.grid(row=1, column=1)
        
        pesquisar_button = tk.Button(master=pesquisar_window, text="Pesquisar", width=30, height=1)
        pesquisar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=4)
        """Esse botão pesquisar vai executar a query buscando todos os artistas pelo nome"""
        
        lista = tk.Listbox(master=pesquisar_window, selectmode="single", bg="#a7f5a4", width=40)#listvariable=LISTA_SQL
        lista.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
        
        """for item in query:
               lista.insert(END,item)"""