import tkinter as tk
from tkinter import ttk

cadastro_window = tk.Toplevel()
cadastro_window.title("Cadastro de Discos")
cadastro_window.geometry("230x150")

#Criação do formulário de cadastro
titulo_label = ttk.Label(text='Título do Disco')
titulo_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)

titulo = tk.StringVar()
titulo_entry = ttk.Entry(textvariable=titulo)
titulo_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)

artista_label = ttk.Label(text='Artista')
artista_label.grid(row=2, column=0, padx=4, pady=4, columnspan=1)

artista = tk.StringVar()
artista_entry = ttk.Entry(textvariable=artista)
artista_entry.grid(row=2, column=1, padx=4, pady=4, columnspan=3)

genero_label = ttk.Label(text='Gênero')
genero_label.grid(row=3, column=0, padx=4, pady=4, columnspan=1)

genero = tk.StringVar()
genero_entry = ttk.Entry(textvariable=genero)
genero_entry.grid(row=3, column=1, padx=4, pady=4, columnspan=3)

ano_label = ttk.Label(text='Ano')
ano_label.grid(row=4, column=0, padx=4, pady=4, columnspan=1)

ano = tk.IntVar()
ano_entry = ttk.Entry(textvariable=ano)
ano_entry.grid(row=4, column=1, padx=4, pady=4, columnspan=3)

gravadora_label = ttk.Label(text='Gravadora')
gravadora_label.grid(row=5, column=0, padx=4, pady=4, columnspan=1)

gravadora = tk.StringVar()
gravadora_entry = ttk.Entry(textvariable=gravadora)
gravadora_entry.grid(row=5, column=1, padx=4, pady=4, columnspan=3)

numero_disco_label = ttk.Label(text='Número do Disco')
numero_disco_label.grid(row=6, column=0, padx=4, pady=4, columnspan=1)

numero = tk.IntVar()
numero_disco_entry = ttk.Entry(textvariable=numero)
numero_disco_entry.grid(row=6, column=1, padx=4, pady=4, columnspan=3)

qualidade_label = ttk.Label(text='Qualidade do Áudio')
qualidade_label.grid(row=7, column=0, padx=4, pady=4, columnspan=1)

qualidade = tk.StringVar()
estereo = ttk.Radiobutton(text="Estéreo", variable=qualidade, value="Estéreo")
estereo.grid(row=7, column=1)
mono = ttk.Radiobutton(text="Mono", variable=qualidade, value="Mono")
mono.grid(row=7, column=2)

estado_capa_label = ttk.Label(text="Estado da Capa")
estado_capa_label.grid(row=8, column=0, padx=4, pady=4, columnspan=1)
estado_capa_combo = ttk.Combobox(values=["M", "NM", "VG+/E", "VG", "G/G+/VG-", "P/F", "SA/SS"])
estado_capa_combo.grid(row=8, column=1, padx=4, pady=4, columnspan=3)

estado_midia_label = ttk.Label(text="Estado da Mídia")
estado_midia_label.grid(row=9, column=0, padx=4, pady=4, columnspan=1)
estado_midia_combo = ttk.Combobox(values=["M", "NM", "VG+/E", "VG", "G/G+/VG-", "P/F", "SA/SS"])
estado_midia_combo.grid(row=9, column=1, padx=4, pady=4, columnspan=3)


salvar_button = tk.Button(text="Salvar", width=30, height=1)
salvar_button.grid(row=10, column=0, padx=4, pady=4, columnspan=3)