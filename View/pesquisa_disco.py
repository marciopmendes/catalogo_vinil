import tkinter as tk
from tkinter import ttk

class pesquisa_discoVw:
    
    def __init__(self):
        self.pesquisaDisco()
    
    def pesquisaDisco(self):
        pesquisar_window = tk.Toplevel()
        pesquisar_window.title("Pesquisar Discos")
        pesquisar_window.geometry("255x320")
        
        pesquisar_label = ttk.Label(master=pesquisar_window, text='Pesquisar Por:')
        pesquisar_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        tipo_pesquisa = tk.StringVar()
        artista = ttk.Radiobutton(master=pesquisar_window, text="Artista", variable=tipo_pesquisa, value="Artista")
        artista.grid(row=1, column=1)
        titulo = ttk.Radiobutton(master=pesquisar_window, text="Título", variable=tipo_pesquisa, value="Título")
        titulo.grid(row=1, column=2)
        
        pesquisa = tk.StringVar()
        pesquisa_entry = ttk.Entry(master=pesquisar_window, textvariable=pesquisa)
        pesquisa_entry.grid(row=2, column=0, padx=4, pady=4, columnspan=4)
        
        pesquisar_button = tk.Button(master=pesquisar_window, text="Pesquisar", width=30, height=1)
        pesquisar_button.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
        """Esse botão pesquisar vai executar a query por artista ou titulo, conforme a escolha do radio button"""
        
        lista = tk.Listbox(master=pesquisar_window, selectmode="single", bg="#a7f5a4", width=40)#listvariable=LISTA_SQL
        lista.grid(row=4, column=0, padx=4, pady=4, columnspan=4)
        
        """for item in query:
               lista.insert(END,item)"""
    
    #PESQUISAR TODAS AS MUSICAS DO CANTOR X
    #PESQUISAR TODAS AS MUSICAS CUJO NOME SEJA Y, MOSTRAR NOME E INTREPRETE NUMA LISTA. A QUE FOR SELECIONADA NESSA LISTA ABRE TODAS AS INFORMAÇÕES
    #EM UM POPUP