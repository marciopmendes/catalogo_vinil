import tkinter as tk
from tkinter import ttk

class cadastro_discoVw:
    
    def __init__(self):
        self.cadastroDisco()
    
    def cadastroDisco(self):
        cadastro_disco_window = tk.Toplevel()
        cadastro_disco_window.title("Cadastro de Discos")
        cadastro_disco_window.geometry("300x300")
        
        #Criação do formulário de cadastro
        titulo_label = ttk.Label(master=cadastro_disco_window, text='Título do Disco')
        titulo_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        titulo = tk.StringVar()
        titulo_entry = ttk.Entry(master=cadastro_disco_window, textvariable=titulo)
        titulo_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
        
        artista_label = ttk.Label(master=cadastro_disco_window, text='Artista')
        artista_label.grid(row=2, column=0, padx=4, pady=4, columnspan=1)
        """o campo abaixo vai ser uma ttk.combobox para escolher dentre os artistas cadastrados"""
        artista = "QUERY"       """"ESSA VARIÁVEL RECEBE A QUERY SELECT * FROM ARTISTAS_TBL"""
        artista_combo = ttk.Combobox(master=cadastro_disco_window, values=artista)
        artista_combo.grid(row=2, column=1, padx=4, pady=4, columnspan=3)
        
        genero_label = ttk.Label(master=cadastro_disco_window, text='Gênero')
        genero_label.grid(row=3, column=0, padx=4, pady=4, columnspan=1)
        
        genero = tk.StringVar()
        genero_entry = ttk.Entry(master=cadastro_disco_window, textvariable=genero)
        genero_entry.grid(row=3, column=1, padx=4, pady=4, columnspan=3)
        
        ano_label = ttk.Label(master=cadastro_disco_window, text='Ano')
        ano_label.grid(row=4, column=0, padx=4, pady=4, columnspan=1)
        
        ano = tk.IntVar()
        ano_entry = ttk.Entry(master=cadastro_disco_window, textvariable=ano)
        ano_entry.grid(row=4, column=1, padx=4, pady=4, columnspan=3)
        
        gravadora_label = ttk.Label(master=cadastro_disco_window, text='Gravadora')
        gravadora_label.grid(row=5, column=0, padx=4, pady=4, columnspan=1)
        
        gravadora = tk.StringVar()
        gravadora_entry = ttk.Entry(master=cadastro_disco_window, textvariable=gravadora)
        gravadora_entry.grid(row=5, column=1, padx=4, pady=4, columnspan=3)
        
        numero_disco_label = ttk.Label(master=cadastro_disco_window, text='Número do Disco')
        numero_disco_label.grid(row=6, column=0, padx=4, pady=4, columnspan=1)
        
        numero = tk.IntVar()
        numero_disco_entry = ttk.Entry(master=cadastro_disco_window, textvariable=numero)
        numero_disco_entry.grid(row=6, column=1, padx=4, pady=4, columnspan=3)
        
        qualidade_label = ttk.Label(master=cadastro_disco_window, text='Qualidade do Áudio')
        qualidade_label.grid(row=7, column=0, padx=4, pady=4, columnspan=1)
        
        qualidade = tk.StringVar()
        estereo = ttk.Radiobutton(master=cadastro_disco_window, text="Estéreo", variable=qualidade, value="Estéreo")
        estereo.grid(row=7, column=1)
        mono = ttk.Radiobutton(master=cadastro_disco_window, text="Mono", variable=qualidade, value="Mono")
        mono.grid(row=7, column=2)
        
        estado_capa_label = ttk.Label(master=cadastro_disco_window, text="Estado da Capa")
        estado_capa_label.grid(row=8, column=0, padx=4, pady=4, columnspan=1)
        estado_capa_combo = ttk.Combobox(master=cadastro_disco_window, values=["M", "NM", "VG+/E", "VG", "G/G+/VG-", "P/F", "SA/SS"])
        estado_capa_combo.grid(row=8, column=1, padx=4, pady=4, columnspan=3)
        
        estado_midia_label = ttk.Label(master=cadastro_disco_window, text="Estado da Mídia")
        estado_midia_label.grid(row=9, column=0, padx=4, pady=4, columnspan=1)
        estado_midia_combo = ttk.Combobox(master=cadastro_disco_window, values=["M", "NM", "VG+/E", "VG", "G/G+/VG-", "P/F", "SA/SS"])
        estado_midia_combo.grid(row=9, column=1, padx=4, pady=4, columnspan=3)
        
        salvar_button = tk.Button(master=cadastro_disco_window, text="Salvar", width=40, height=1)
        salvar_button.grid(row=10, column=0, padx=4, pady=4, columnspan=3)