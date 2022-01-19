import tkinter as tk
from tkinter import ttk
from Controller.controller_artista import artistaCt

class artistaVw:
    
    def __init__(self):
        self.controller_artista = artistaCt()
    
    def cadastroArtista(self):
        cadastro_artista_window = tk.Toplevel()
        cadastro_artista_window.title("Cadastro de Artistas")
        cadastro_artista_window.geometry("250x70")
        
        def saveArtista(nome):
            self.controller_artista.ctCadastrarArtista(nome)
            artista_entry.delete(0, 'end')
        
        artista_label = ttk.Label(master=cadastro_artista_window, text='Nome do Artista')
        artista_label.grid(row=1, column=0, padx=4, pady=4)
        
        artista = tk.StringVar()
        artista_entry = ttk.Entry(master=cadastro_artista_window, textvariable=artista)
        artista_entry.grid(row=1, column=1, padx=4, pady=4)
        
        salvar_button = tk.Button(master=cadastro_artista_window, text="Salvar", width=33, height=1, command=lambda:saveArtista(artista.get()))
        salvar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=2)
        
    def alterarArtista(self):
        alterar_window = tk.Toplevel()
        alterar_window.title("Alterar Artista")
        alterar_window.geometry("255x280")
        
        artista_label = ttk.Label(master=alterar_window, text='Nome do Artista')
        artista_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        artista = tk.StringVar()
        artista_entry = ttk.Entry(master=alterar_window, textvariable=artista)
        artista_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
        
        def getIdByName():
            id_artista = self.controller_artista.ctCapturaId(lista_artistas.get(lista_artistas.curselection()))
            return id_artista

        lista_artistas = tk.Listbox(master=alterar_window, selectmode="single", bg="#a7f5a4", width=40)
        lista_artistas.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
        
        def alimentaLista(nome):
            lista_artistas.delete(0, 'end')
            query = self.controller_artista.ctBuscarArtista(nome)
            for artista in query:
                lista_artistas.insert('end', artista)
                
        buscar_button = tk.Button(master=alterar_window, text="Buscar", width=30, height=1, command=lambda:alimentaLista(artista.get()))
        buscar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=4)
        
        def alterarArtistaForm(id_artista):
            print(id_artista)
            artista_window = tk.Toplevel()
            artista_window.title("Informações do Artista")
            artista_window.geometry("230x80")
            
            artista_label = ttk.Label(master=artista_window, text='Artista')
            artista_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
            
            novo_artista = tk.StringVar()
            novo_artista_entry = ttk.Entry(master=artista_window, textvariable=novo_artista)
            novo_artista_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
                       
            salvar_button = tk.Button(master=artista_window, text="Salvar", width=30, height=1, command=lambda:self.controller_artista.ctAlterarArtista(id_artista, novo_artista.get()))
            salvar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=3)
        
        alterar_button = tk.Button(master=alterar_window, text="Alterar Artista Selecionado", width=30, height=1, command=lambda:alterarArtistaForm(getIdByName()))
        alterar_button.grid(row=4, column=0, padx=4, pady=4, columnspan=4)

    def pesquisaArtista(self):
        pesquisar_window = tk.Toplevel()
        pesquisar_window.title("Pesquisar Artistas")
        pesquisar_window.geometry("255x250")
        
        pesquisar_label = ttk.Label(master=pesquisar_window, text='Nome do Artista:')
        pesquisar_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        artista = tk.StringVar()
        artista_entry = tk.Entry(master=pesquisar_window, textvariable=artista)
        artista_entry.grid(row=1, column=1)
        
        lista = tk.Listbox(master=pesquisar_window, selectmode="single", bg="#a7f5a4", width=40)
        lista.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
        
        def alimentaLista(nome):
            lista.delete(0, 'end')
            query = self.controller_artista.ctBuscarArtista(nome)
            for artista in query:
                lista.insert('end', artista)
            artista_entry.delete(0, 'end')
                
        pesquisar_button = tk.Button(master=pesquisar_window, text="Pesquisar", width=30, height=1, command=lambda:alimentaLista(artista.get()))
        pesquisar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=4)  
     
    def excluirArtista(self):
        excluir_window = tk.Toplevel()
        excluir_window.title("Excluir Artistas")
        excluir_window.geometry("255x320")
        
        artista_label = ttk.Label(master=excluir_window, text='Nome do Artista')
        artista_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        artista = tk.StringVar()
        artista_entry = ttk.Entry(master=excluir_window, textvariable=artista)
        artista_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
        
        lista = tk.Listbox(master=excluir_window, selectmode="multiple", bg="#a7f5a4", width=40)
        lista.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
        
        def alimentaLista(nome):
            lista.delete(0, 'end')
            query = self.controller_artista.ctBuscarArtista(nome)
            for artista in query:
                lista.insert('end', artista)
                
        buscar_button = tk.Button(master=excluir_window, text="Buscar", width=30, height=1, command=lambda:alimentaLista(artista.get()))
        buscar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=4)
        
        def getIdsToDelete():
            tupla = lista.curselection()
            lista_ids = []
            for idt in tupla:
                id_artista = self.controller_artista.ctCapturaId(lista.get(idt))
                lista_ids.append(id_artista) 
            return lista_ids
          
        excluir_button = tk.Button(master=excluir_window, text="Excluir Artistas Selecionados", width=30, height=1, command=lambda:self.controller_artista.ctExcluirArtistas(getIdsToDelete()))
        excluir_button.grid(row=4, column=0, padx=4, pady=4, columnspan=4)