import tkinter as tk
from tkinter import ttk

pesquisar_window = tk.Toplevel()
pesquisar_window.title("Pesquisar Discos")
pesquisar_window.geometry("230x150")

pesquisar_label = ttk.Label(text='Pesquisar Por:')
pesquisar_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)

tipo_pesquisa = tk.StringVar()
artista = ttk.Radiobutton(text="Artista", variable=tipo_pesquisa, value="Artista")
artista.grid(row=1, column=1)
titulo = ttk.Radiobutton(text="Título", variable=tipo_pesquisa, value="Título")
titulo.grid(row=1, column=2)

pesquisa = tk.StringVar()
pesquisa_entry = ttk.Entry(textvariable=pesquisa)
pesquisa_entry.grid(row=2, column=0, padx=4, pady=4, columnspan=4)

pesquisar_button = tk.Button(text="Pesquisar", width=30, height=1)
pesquisar_button.grid(row=3, column=0, padx=4, pady=4, columnspan=4)