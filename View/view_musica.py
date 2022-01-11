import tkinter as tk
from tkinter import ttk
from Controller.controller_musica import musicaCt

class musicaVw:
    def __init__(self):
        pass
    
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
        """o campo abaixo vai ser uma ttk.combobox para escolher dentre os artistas cadastrados"""
        interprete = "QUERY"  """ESSA VARIAVEL RECEBE A QUERY SELECT * FROM ARTISTAS_TBL"""
        interprete_combo = ttk.Combobox(master=cadastro_musica_window, values=interprete)
        interprete_combo.grid(row=2, column=1, padx=4, pady=4, columnspan=3)
        
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
            
    def pesquisaMusica(self):
        pesquisar_window = tk.Toplevel()
        pesquisar_window.title("Pesquisar Músicas")
        pesquisar_window.geometry("255x350")
        
        pesquisar_label = ttk.Label(master=pesquisar_window, text='Pesquisar Por:')
        pesquisar_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        tipo_pesquisa = tk.StringVar()
        interprete = ttk.Radiobutton(master=pesquisar_window, text="Intérprete", variable=tipo_pesquisa, value="Intérprete")
        interprete.grid(row=1, column=1)
        titulo = ttk.Radiobutton(master=pesquisar_window, text="Título", variable=tipo_pesquisa, value="Título")
        titulo.grid(row=1, column=2)
        
        pesquisa = tk.StringVar()
        pesquisa_entry = ttk.Entry(master=pesquisar_window, textvariable=pesquisa)
        pesquisa_entry.grid(row=2, column=0, padx=4, pady=4, columnspan=4)
        
        pesquisar_button = tk.Button(master=pesquisar_window, text="Pesquisar", width=30, height=1)
        pesquisar_button.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
        
        """O botão de buscar vai executar uma query. O resultado dessa query será usado para alimentar a listbox"""
        
        lista = tk.Listbox(master=pesquisar_window, selectmode="single", bg="#a7f5a4", width=40)#listvariable=LISTA_SQL
        lista.grid(row=4, column=0, padx=4, pady=4, columnspan=4)
        
        """for item in query:
               lista.insert(END,item)"""
    
    #PESQUISAR TODAS AS MUSICAS DO CANTOR X
    #PESQUISAR TODAS AS MUSICAS CUJO NOME SEJA Y, MOSTRAR NOME E INTREPRETE NUMA LISTA. A QUE FOR SELECIONADA NESSA LISTA ABRE TODAS AS INFORMAÇÕES
    #EM UM POPUP
    
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
        
    