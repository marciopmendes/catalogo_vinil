import tkinter as tk
from tkinter import ttk

class alterar_artistaVw:
    def __init__(self):
        self.alterarArtista()
        
    def alterarArtista(self):
        alterar_window = tk.Toplevel()
        alterar_window.title("Alterar Artista")
        alterar_window.geometry("255x350")
        
        #Criação do formulário de alteração
        artista_label = ttk.Label(master=alterar_window, text='Nome do Artista')
        artista_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        artista = tk.StringVar()
        artista_entry = ttk.Entry(master=alterar_window, textvariable=artista)
        artista_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
        
        buscar_button = tk.Button(master=alterar_window, text="Buscar", width=30, height=1)
        buscar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=4)
        
        """O botão de buscar vai executar uma query. O resultado dessa query será usado para alimentar a listbox"""
        
        lista = tk.Listbox(master=alterar_window, selectmode="single", bg="#a7f5a4", width=40)#listvariable=LISTA_SQL
        lista.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
        
        """for item in query:
               lista.insert(END,item)
               
            Os itens selecionados vão popular algo tipo uma lista que vai alimentar a query de alterar"""
        
        alterar_button = tk.Button(master=alterar_window, text="Alterar Artista Selecionado", width=30, height=1)
        alterar_button.grid(row=4, column=0, padx=4, pady=4, columnspan=4)
        
        """o botão alterar acima vai executar uma função chamando o formulário abaixo"""
        
        def alterarArtistaForm(self):
            artista_window = tk.Toplevel()
            artista_window.title("Informações do Artista")
            artista_window.geometry("230x150")
            
            artista_label = ttk.Label(text='Artista')
            artista_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
            
            artista = tk.StringVar()
            artista_entry = ttk.Entry(textvariable=artista)
            artista_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
                       
            salvar_button = tk.Button(text="Salvar", width=30, height=1)
            salvar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=3)
            """Esse botão vai executar uma query alterando o artista selecionado na listbox"""