import tkinter as tk
from tkinter import ttk

#Criação da janela principal
main_window = tk.Tk()
main_window.title("Catálogo de Discos")
main_window.geometry("230x180")

#Criação dos botões na tela principal
cadastrar_disco_button = tk.Button(text="Cadastrar Novo Disco", width=30, height=1)
cadastrar_disco_button.grid(row=1, column=0, padx=4, pady=4, columnspan=3)

cadastrar_musica_button = tk.Button(text="Cadastrar Músicas", width=30, height=1)
cadastrar_musica_button.grid(row=2, column=0, padx=4, pady=4, columnspan=3)

pesquisar_disco_button = tk.Button(text="Pesquisar Disco", width=30, height=1)
pesquisar_disco_button.grid(row=3, column=0, padx=4, pady=4, columnspan=3)

excluir_disco_button = tk.Button(text="Excluir Disco", width=30, height=1)
excluir_disco_button.grid(row=4, column=0, padx=4, pady=4, columnspan=3)

sair_button = tk.Button(text="Sair", width=30, height=1, command=main_window.destroy)
sair_button.grid(row=5, column=0, padx=4, pady=4, columnspan=3)

#Instrução para rodar o código
if __name__ == '__main__':
    main_window.mainloop()