import tkinter as tk
from tkinter import ttk

class pesquisa_musicaVw:
    def __init__(self):
        pass
    
    def pesquisaMusica(self):
        pesquisar_window = tk.Toplevel()
        pesquisar_window.title("Pesquisar Músicas")
        pesquisar_window.geometry("230x150")
        
        pesquisar_label = ttk.Label(master=pesquisar_window, text='Pesquisar Por:')
        pesquisar_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        tipo_pesquisa = tk.StringVar()
        interprete = ttk.Radiobutton(master=pesquisar_window, text="Intérprete", variable=tipo_pesquisa, value="Intérprete")
        interprete.grid(row=1, column=1)
        titulo = ttk.Radiobutton(master=pesquisar_window, text="Título", variable=tipo_pesquisa, value="Título")
        titulo.grid(row=1, column=2)
        
        pesquisa = tk.StringVar()
        pesquisa_entry = ttk.Entry(master=pesquisar_window, textvariable=pesquisa)
        pesquisa_entry.grid(row=2, column=0, padx=4, pady=4, columnspan=4)
        
        pesquisar_button = tk.Button(master=pesquisar_window, text="Pesquisar", width=30, height=1)
        pesquisar_button.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
        
        """O botão de buscar vai executar uma query. O resultado dessa query será usado para alimentar a listbox"""
        
        lista = tk.Listbox(master=pesquisar_window, selectmode="single", bg="#a7f5a4", width=40)#listvariable=LISTA_SQL
        lista.grid(row=4, column=0, padx=4, pady=4, columnspan=4)
        
        """for item in query:
               lista.insert(END,item)"""
    
    #PESQUISAR TODAS AS MUSICAS DO CANTOR X
    #PESQUISAR TODAS AS MUSICAS CUJO NOME SEJA Y, MOSTRAR NOME E INTREPRETE NUMA LISTA. A QUE FOR SELECIONADA NESSA LISTA ABRE TODAS AS INFORMAÇÕES
    #EM UM POPUP