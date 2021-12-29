import tkinter as tk
from tkinter import ttk

class altera_musicaVw:
    
    def __init__(self):
        self.alterarMusica()
    
    def alterarMusica(self):
        alterar_window = tk.Toplevel()
        alterar_window.title("Alterar Música")
        alterar_window.geometry("255x350")
        
        #Criação do formulário de alteração
        musica_label = ttk.Label(master=alterar_window, text='Nome da Música')
        musica_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        musica = tk.StringVar()
        musica_entry = ttk.Entry(master=alterar_window, textvariable=musica)
        musica_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
        
        buscar_button = tk.Button(master=alterar_window, text="Buscar", width=30, height=1)
        buscar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=4)
        
        """O botão de buscar vai executar uma query. O resultado dessa query será usado para alimentar a listbox"""
        
        lista = tk.Listbox(master=alterar_window, selectmode="single", bg="#a7f5a4", width=40)#listvariable=LISTA_SQL
        lista.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
        
        """for item in query:
               lista.insert(END,item)
               
            Os itens selecionados vão popular algo tipo uma lista que vai alimentar a query de alterar"""
        
        alterar_button = tk.Button(master=alterar_window, text="Alterar Música Selecionada", width=30, height=1)
        alterar_button.grid(row=4, column=0, padx=4, pady=4, columnspan=4)
        
        """o botão alterar acima vai executar uma função chamando o formulário abaixo"""
        def alterarMusicaForm(self):
            musica_window = tk.Toplevel()
            musica_window.title("Informações da Música")
            musica_window.geometry("230x150")
            
            titulo_label = ttk.Label(master=musica_window, text='Título da Música')
            titulo_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
            titulo = tk.StringVar()
            titulo_entry = ttk.Entry(master=musica_window, textvariable=titulo)
            titulo_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
            
            interprete_label = ttk.Label(master=musica_window, text='Intérprete')
            interprete_label.grid(row=2, column=0, padx=4, pady=4, columnspan=1)
            
            interprete = tk.StringVar()
            interprete_entry = ttk.Entry(master=musica_window, textvariable=interprete)
            interprete_entry.grid(row=2, column=1, padx=4, pady=4, columnspan=3)
            
            compositor_label = ttk.Label(master=musica_window, text='Compositor')
            compositor_label.grid(row=3, column=0, padx=4, pady=4, columnspan=1)
            
            compositor = tk.StringVar()
            compositor_entry = ttk.Entry(master=musica_window, textvariable=compositor)
            compositor_entry.grid(row=3, column=1, padx=4, pady=4, columnspan=3)
            
            genero_label = ttk.Label(master=musica_window, text='Gênero')
            genero_label.grid(row=4, column=0, padx=4, pady=4, columnspan=1)
            
            genero = tk.StringVar()
            genero_entry = ttk.Entry(master=musica_window, textvariable=genero)
            genero_entry.grid(row=4, column=1, padx=4, pady=4, columnspan=3)
            
            lado_disco_label = ttk.Label(master=musica_window, text='Lado do Disco')
            lado_disco_label.grid(row=5, column=0, padx=4, pady=4, columnspan=1)
            
            lado_disco = tk.StringVar()
            lado_disco_entry = ttk.Entry(master=musica_window, textvariable=lado_disco)
            lado_disco_entry.grid(row=5, column=1, padx=4, pady=4, columnspan=3)
                
            salvar_button = tk.Button(master=musica_window, text="Salvar", width=30, height=1)
            salvar_button.grid(row=10, column=0, padx=4, pady=4, columnspan=3)
            """Esse botão vai executar uma query alterando a música selecionada na listbox"""