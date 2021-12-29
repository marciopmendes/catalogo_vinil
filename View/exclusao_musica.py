import tkinter as tk
from tkinter import ttk

class excluir_musicaVw:
    
    def __init__(self):
        self.excluirMusica()
    
    def excluirMusica(self):
        excluir_window = tk.Toplevel()
        excluir_window.title("Excluir Músicas")
        excluir_window.geometry("255x350")
        
        #Criação do formulário de exclusão
        musica_label = ttk.Label(master=excluir_window, text='Nome da Música')
        musica_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        musica = tk.StringVar()
        musica_entry = ttk.Entry(master=excluir_window, textvariable=musica)
        musica_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
        
        buscar_button = tk.Button(master=excluir_window, text="Buscar", width=30, height=1)
        buscar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=4)
        
        """O botão de buscar vai executar uma query. O resultado dessa query será usado para alimentar a listbox"""
        
        lista = tk.Listbox(master=excluir_window, selectmode="multiple", bg="#a7f5a4", width=40)#listvariable=LISTA_SQL
        lista.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
        
        """for item in query:
               lista.insert(END,item)
               
            Os itens selecionados vão popular algo tipo uma lista que vai alimentar a query de exclusão"""
        
        excluir_button = tk.Button(master=excluir_window, text="Excluir Itens Selecionados", width=30, height=1)
        excluir_button.grid(row=4, column=0, padx=4, pady=4, columnspan=4)