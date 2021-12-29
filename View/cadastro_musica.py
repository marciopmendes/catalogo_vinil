import tkinter as tk
from tkinter import ttk


class cadastro_musicaVw:
    
    def __init__(self):
        self.cadastroMusica()
    
    def cadastroMusica(self):
        cadastro_musica_window = tk.Toplevel()
        cadastro_musica_window.title("Cadastro de Músicas")
        cadastro_musica_window.geometry("255x360")
        
        lista_musicas = list()
        
        #Criação do formulário de cadastro
        titulo_label = ttk.Label(master=cadastro_musica_window, text='Título da Música')
        titulo_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        titulo = tk.StringVar()
        titulo_entry = ttk.Entry(master=cadastro_musica_window, textvariable=titulo)
        titulo_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
        
        interprete_label = ttk.Label(master=cadastro_musica_window, text='Intérprete')
        interprete_label.grid(row=2, column=0, padx=4, pady=4, columnspan=1)
        
        interprete = tk.StringVar()
        interprete_entry = ttk.Entry(master=cadastro_musica_window, textvariable=interprete)
        interprete_entry.grid(row=2, column=1, padx=4, pady=4, columnspan=3)
        
        compositor_label = ttk.Label(master=cadastro_musica_window, text='Compositor')
        compositor_label.grid(row=3, column=0, padx=4, pady=4, columnspan=1)
        
        compositor = tk.StringVar()
        compositor_entry = ttk.Entry(master=cadastro_musica_window, textvariable=compositor)
        compositor_entry.grid(row=3, column=1, padx=4, pady=4, columnspan=3)
        
        genero_label = ttk.Label(master=cadastro_musica_window, text='Gênero')
        genero_label.grid(row=4, column=0, padx=4, pady=4, columnspan=1)
        
        genero = tk.StringVar()
        genero_entry = ttk.Entry(master=cadastro_musica_window, textvariable=genero)
        genero_entry.grid(row=4, column=1, padx=4, pady=4, columnspan=3)
        
        lado_disco_label = ttk.Label(master=cadastro_musica_window, text='Lado do Disco')
        lado_disco_label.grid(row=5, column=0, padx=4, pady=4, columnspan=1)
        
        lado_disco = tk.StringVar()
        lado_disco_entry = ttk.Entry(master=cadastro_musica_window, textvariable=lado_disco)
        lado_disco_entry.grid(row=5, column=1, padx=4, pady=4, columnspan=3)
        
        adicionar_button = tk.Button(master=cadastro_musica_window, text="Adicionar Música")
        adicionar_button.grid(row=6, column=0, padx=4, pady=4, columnspan=2)
        """clicar no botão adicionar, faz um append na lista. essa lista alimenta uma listbox que aparece pro usuário
        saber qual ele já cadastrou"""
        
        finalizar_button = tk.Button(master=cadastro_musica_window, text="Finalizar Cadastro")
        finalizar_button.grid(row=6, column=3, padx=4, pady=4, columnspan=2)
        """clicar no botão finalizar cadastro executa a query que linka as músicas com o disco"""
        
        musicas_lb = tk.Listbox(master=cadastro_musica_window, bg="#a7f5a4", width=40, listvariable=lista_musicas)
        musicas_lb.grid(row=7, column=0, padx=4, pady=4, columnspan=4)