import tkinter as tk
from tkinter import ttk

excluir_window = tk.Toplevel()
excluir_window.title("Excluir Discos")
excluir_window.geometry("230x150")

#Criação do formulário de exclusão
artista_label = ttk.Label(text='Nome do Artista')
artista_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)

artista = tk.StringVar()
artista_entry = ttk.Entry(textvariable=artista)
artista_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)

buscar_button = tk.Button(text="Buscar", width=30, height=1)
buscar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=4)

"""O botão de buscar vai executar uma query. O resultado dessa query será usado para alimentar a listbox"""

lista = tk.Listbox(selectmode="multiple", bg="#a7f5a4", width=40)#listvariable=LISTA_SQL
lista.grid(row=3, column=0, padx=4, pady=4, columnspan=4)

"""for item in query:
       lista.insert(END,item)
       
    Os itens selecionados vão popular algo tipo uma lista que vai alimentar a query de exclusão"""

excluir_button = tk.Button(text="Excluir Itens Selecionados", width=30, height=1)
excluir_button.grid(row=4, column=0, padx=4, pady=4, columnspan=4)


#PENDÊNCIAS
#View cadastro músicas
