import tkinter as tk
from tkinter import ttk
from Controller.controller_disco import discoCt

class discoVw:
    def __init__(self):
        self.controller_disco = discoCt()
        
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
        
    def alterarDisco(self):
        alterar_window = tk.Toplevel()
        alterar_window.title("Alterar Disco")
        alterar_window.geometry("255x350")
        
        #Criação do formulário de alteração
        artista_label = ttk.Label(master=alterar_window, text='Nome do Artista')
        artista_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        artista = tk.StringVar()
        artista_entry = ttk.Entry(master=alterar_window, textvariable=artista)
        artista_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
        
        buscar_button = tk.Button(master=alterar_window, text="Buscar", width=30, height=1)
        buscar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=4)
        
        """O botão de buscar vai executar uma query. O resultado dessa query será usado para alimentar a listbox"""
        
        lista = tk.Listbox(master=alterar_window, selectmode="single", bg="#a7f5a4", width=40)#listvariable=LISTA_SQL
        lista.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
        
        """for item in query:
               lista.insert(END,item)
               
            Os itens selecionados vão popular algo tipo uma lista que vai alimentar a query de alterar"""
        
        alterar_button = tk.Button(master=alterar_window, text="Alterar Disco Selecionado", width=30, height=1)
        alterar_button.grid(row=4, column=0, padx=4, pady=4, columnspan=4)
        
        """o botão alterar acima vai executar uma função chamando o formulário abaixo"""
        def alterarDiscoForm(self):
            disco_window = tk.Toplevel()
            disco_window.title("Informações do Disco")
            disco_window.geometry("230x150")
            
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
            """Esse botão vai executar uma query alterando o disco selecionado na listbox"""
            
    def pesquisaDisco(self):
        pesquisar_window = tk.Toplevel()
        pesquisar_window.title("Pesquisar Discos")
        pesquisar_window.geometry("255x320")
        
        pesquisar_label = ttk.Label(master=pesquisar_window, text='Pesquisar Por:')
        pesquisar_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        tipo_pesquisa = tk.StringVar()
        artista = ttk.Radiobutton(master=pesquisar_window, text="Artista", variable=tipo_pesquisa, value="Artista")
        artista.grid(row=1, column=1)
        titulo = ttk.Radiobutton(master=pesquisar_window, text="Título", variable=tipo_pesquisa, value="Título")
        titulo.grid(row=1, column=2)
        
        pesquisa = tk.StringVar()
        pesquisa_entry = ttk.Entry(master=pesquisar_window, textvariable=pesquisa)
        pesquisa_entry.grid(row=2, column=0, padx=4, pady=4, columnspan=4)
        
        pesquisar_button = tk.Button(master=pesquisar_window, text="Pesquisar", width=30, height=1)
        pesquisar_button.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
        """Esse botão pesquisar vai executar a query por artista ou titulo, conforme a escolha do radio button"""
        
        lista = tk.Listbox(master=pesquisar_window, selectmode="single", bg="#a7f5a4", width=40)#listvariable=LISTA_SQL
        lista.grid(row=4, column=0, padx=4, pady=4, columnspan=4)
        
        """for item in query:
               lista.insert(END,item)"""
    
    #PESQUISAR TODAS AS MUSICAS DO CANTOR X
    #PESQUISAR TODAS AS MUSICAS CUJO NOME SEJA Y, MOSTRAR NOME E INTREPRETE NUMA LISTA. A QUE FOR SELECIONADA NESSA LISTA ABRE TODAS AS INFORMAÇÕES
    #EM UM POPUP
    
    def excluirDisco(self):
        excluir_window = tk.Toplevel()
        excluir_window.title("Excluir Discos")
        excluir_window.geometry("255x320")
        
        #Criação do formulário de exclusão
        artista_label = ttk.Label(master=excluir_window, text='Nome do Artista')
        artista_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        artista = tk.StringVar()
        artista_entry = ttk.Entry(master=excluir_window, textvariable=artista)
        artista_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
        
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