import tkinter as tk
from tkinter import ttk

cadastro_window = tk.Toplevel()
cadastro_window.title("Cadastro de Músicas")
cadastro_window.geometry("230x150")

lista_musicas = list()

#Criação do formulário de cadastro
titulo_label = ttk.Label(text='Título da Música')
titulo_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)

titulo = tk.StringVar()
titulo_entry = ttk.Entry(textvariable=titulo)
titulo_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)

interprete_label = ttk.Label(text='Intérprete')
interprete_label.grid(row=2, column=0, padx=4, pady=4, columnspan=1)

interprete = tk.StringVar()
interprete_entry = ttk.Entry(textvariable=interprete)
interprete_entry.grid(row=2, column=1, padx=4, pady=4, columnspan=3)

compositor_label = ttk.Label(text='Compositor')
compositor_label.grid(row=3, column=0, padx=4, pady=4, columnspan=1)

compositor = tk.StringVar()
compositor_entry = ttk.Entry(textvariable=compositor)
compositor_entry.grid(row=3, column=1, padx=4, pady=4, columnspan=3)

genero_label = ttk.Label(text='Gênero')
genero_label.grid(row=4, column=0, padx=4, pady=4, columnspan=1)

genero = tk.StringVar()
genero_entry = ttk.Entry(textvariable=genero)
genero_entry.grid(row=4, column=1, padx=4, pady=4, columnspan=3)

lado_disco_label = ttk.Label(text='Lado do Disco')
lado_disco_label.grid(row=5, column=0, padx=4, pady=4, columnspan=1)

lado_disco = tk.StringVar()
lado_disco_entry = ttk.Entry(textvariable=genero)
lado_disco_entry.grid(row=5, column=1, padx=4, pady=4, columnspan=3)

adicionar_button = tk.Button(text="Adicionar Música")
adicionar_button.grid(row=6, column=0, padx=4, pady=4, columnspan=2)
"""clicar no botão adicionar, faz um append na lista. essa lista alimenta uma listbox que aparece pro usuário
saber qual ele já cadastrou"""

finalizar_button = tk.Button(text="Finalizar Cadastro")
finalizar_button.grid(row=6, column=3, padx=4, pady=4, columnspan=2)
"""clicar no botão finalizar cadastro executa a query que linka as músicas com o disco"""

musicas_lb = tk.Listbox(bg="#a7f5a4", width=40, listvariable=lista_musicas)
musicas_lb.grid(row=7, column=0, padx=4, pady=4, columnspan=4)


cadastro_window.mainloop()