import sys
sys.path.append("./")
import tkinter as tk
from tkinter import ttk
from Controller.controller_disco import DiscoCt
from Controller.controller_artista import ArtistaCt


class DiscoVw:
    def __init__(self):
        self.controller_disco = DiscoCt()
        self.controller_artista = ArtistaCt()
        
    def cadastroDisco(self):
        cadastro_disco_window = tk.Toplevel()
        cadastro_disco_window.title("Cadastro de Discos")
        cadastro_disco_window.geometry("300x300")

        titulo_label = ttk.Label(master=cadastro_disco_window, text='Título do Disco')
        titulo_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        titulo = tk.StringVar()
        titulo_entry = ttk.Entry(master=cadastro_disco_window, textvariable=titulo)
        titulo_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
        
        artista_label = ttk.Label(master=cadastro_disco_window, text='Artista')
        artista_label.grid(row=2, column=0, padx=4, pady=4, columnspan=1)
        lista_artistas = self.controller_disco.listaArtistas()
        artista = tk.StringVar()
        artista_combo = ttk.Combobox(master=cadastro_disco_window, values=lista_artistas, textvariable=artista,
                                     state="readonly")
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
        estado_capa = tk.StringVar()
        estado_capa_combo = ttk.Combobox(master=cadastro_disco_window,
                                         values=["M", "NM", "VG+/E", "VG", "G/G+/VG-", "P/F", "SA/SS"],
                                         textvariable=estado_capa, state="readonly")
        estado_capa_combo.grid(row=8, column=1, padx=4, pady=4, columnspan=3)
        
        estado_midia_label = ttk.Label(master=cadastro_disco_window, text="Estado da Mídia")
        estado_midia_label.grid(row=9, column=0, padx=4, pady=4, columnspan=1)
        estado_midia = tk.StringVar()
        estado_midia_combo = ttk.Combobox(master=cadastro_disco_window,
                                          values=["M", "NM", "VG+/E", "VG", "G/G+/VG-", "P/F", "SA/SS"],
                                          textvariable=estado_midia, state="readonly")
        estado_midia_combo.grid(row=9, column=1, padx=4, pady=4, columnspan=3)

        def saveDisco(_titulo, _artista, _genero, _ano, _gravadora, _numero, _qualidade, _capa, _midia):
            id_artista = self.controller_disco.getArtistaById(_artista)
            self.controller_disco.ctCadastrarDisco(_titulo, id_artista, _genero, _ano, _gravadora, _numero, _qualidade,
                                                   _capa, _midia)
            cadastro_disco_window.destroy()
        
        salvar_button = tk.Button(master=cadastro_disco_window, text="Salvar", width=40, height=1,
                                  command=lambda: saveDisco(titulo.get(), artista.get(), genero.get(), ano.get(),
                                                            gravadora.get(), numero.get(),
                                                            qualidade.get(), estado_capa.get(), estado_midia.get()))
        salvar_button.grid(row=10, column=0, padx=4, pady=4, columnspan=3)
        
    def alterarDisco(self):
        alterar_window = tk.Toplevel()
        alterar_window.title("Alterar Disco")
        alterar_window.geometry("255x350")

        pesquisa_label = ttk.Label(master=alterar_window, text='Buscar por: ')
        pesquisa_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)

        pesquisa = tk.StringVar()
        pesquisa_entry = ttk.Entry(master=alterar_window, textvariable=pesquisa)
        pesquisa_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=2)

        criterio = tk.StringVar()
        artistaRb = ttk.Radiobutton(master=alterar_window, text="Artista", variable=criterio, value="Artista")
        artistaRb.grid(row=1, column=3, columnspan=1)
        discoRb = ttk.Radiobutton(master=alterar_window, text="Disco", variable=criterio, value="Disco")
        discoRb.grid(row=1, column=4, columnspan=1)

        lista_discos = tk.Listbox(master=alterar_window, selectmode="single", bg="#a7f5a4", width=100)
        lista_discos.grid(row=3, column=0, padx=4, pady=4, columnspan=5)
        
        def alimentaLista(_criterio, _pesquisa):
            lista_discos.delete(0, 'end')
            lista_discos.insert('end', "ID-Titulo-Artista-Ano-Numero do Disco")
            if _criterio == "Disco":
                query = self.controller_disco.ctBuscarPorTitulo(_pesquisa)
            else:
                query = self.controller_disco.ctBuscarPorArtista(_pesquisa)
            for disco in query:
                lista_discos.insert('end', disco)

        buscar_button = tk.Button(master=alterar_window, text="Buscar", width=30, height=1,
                                  command=lambda: alimentaLista(criterio.get(), pesquisa.get()))
        buscar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=4)

        def get_ID():
            str_id = lista_discos.get(lista_discos.curselection())
            id_disco = int(str_id.split("-", 1)[0])
            return id_disco
     
        alterar_button = tk.Button(master=alterar_window, text="Alterar Disco Selecionado", width=30, height=1,
                                   command=lambda: alterarDiscoForm(get_ID()))
        alterar_button.grid(row=5, column=0, padx=4, pady=4, columnspan=4)

        def alterarDiscoForm(id_do_disco):
            disco_window = tk.Toplevel()
            disco_window.title("Informações do Disco")
            disco_window.geometry("230x150")
            
            titulo_label = ttk.Label(master=disco_window, text='Título do Disco')
            titulo_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
            
            titulo = tk.StringVar()
            titulo_entry = ttk.Entry(master=disco_window, textvariable=titulo)
            titulo_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
            
            artista_label = ttk.Label(master=disco_window, text='Artista')
            artista_label.grid(row=2, column=0, padx=4, pady=4, columnspan=1)
            
            artista = tk.StringVar()
            artista_entry = ttk.Entry(master=disco_window, textvariable=artista)
            artista_entry.grid(row=2, column=1, padx=4, pady=4, columnspan=3)
            
            genero_label = ttk.Label(master=disco_window, text='Gênero')
            genero_label.grid(row=3, column=0, padx=4, pady=4, columnspan=1)
            
            genero = tk.StringVar()
            genero_entry = ttk.Entry(master=disco_window, textvariable=genero)
            genero_entry.grid(row=3, column=1, padx=4, pady=4, columnspan=3)
            
            ano_label = ttk.Label(master=disco_window, text='Ano')
            ano_label.grid(row=4, column=0, padx=4, pady=4, columnspan=1)
            
            ano = tk.IntVar()
            ano_entry = ttk.Entry(master=disco_window, textvariable=ano)
            ano_entry.grid(row=4, column=1, padx=4, pady=4, columnspan=3)
            
            gravadora_label = ttk.Label(master=disco_window, text='Gravadora')
            gravadora_label.grid(row=5, column=0, padx=4, pady=4, columnspan=1)
            
            gravadora = tk.StringVar()
            gravadora_entry = ttk.Entry(master=disco_window, textvariable=gravadora)
            gravadora_entry.grid(row=5, column=1, padx=4, pady=4, columnspan=3)
            
            numero_disco_label = ttk.Label(master=disco_window, text='Número do Disco')
            numero_disco_label.grid(row=6, column=0, padx=4, pady=4, columnspan=1)
            
            numero = tk.IntVar()
            numero_disco_entry = ttk.Entry(master=disco_window, textvariable=numero)
            numero_disco_entry.grid(row=6, column=1, padx=4, pady=4, columnspan=3)
            
            qualidade_label = ttk.Label(master=disco_window, text='Qualidade do Áudio')
            qualidade_label.grid(row=7, column=0, padx=4, pady=4, columnspan=1)
            
            qualidade = tk.StringVar()
            estereo = ttk.Radiobutton(master=disco_window, text="Estéreo", variable=qualidade, value="Estéreo")
            estereo.grid(row=7, column=1)
            mono = ttk.Radiobutton(master=disco_window, text="Mono", variable=qualidade, value="Mono")
            mono.grid(row=7, column=2)
            
            estado_capa = tk.StringVar()
            estado_capa_label = ttk.Label(master=disco_window, text="Estado da Capa")
            estado_capa_label.grid(row=8, column=0, padx=4, pady=4, columnspan=1)
            estado_capa_combo = ttk.Combobox(master=disco_window,
                                             values=["M", "NM", "VG+/E", "VG", "G/G+/VG-", "P/F", "SA/SS"],
                                             textvariable=estado_capa, state="readonly")
            estado_capa_combo.grid(row=8, column=1, padx=4, pady=4, columnspan=3)
            
            estado_midia = tk.StringVar()
            estado_midia_label = ttk.Label(master=disco_window, text="Estado da Mídia")
            estado_midia_label.grid(row=9, column=0, padx=4, pady=4, columnspan=1)
            estado_midia_combo = ttk.Combobox(master=disco_window,
                                              values=["M", "NM", "VG+/E", "VG", "G/G+/VG-", "P/F", "SA/SS"],
                                              textvariable=estado_midia, state="readonly")
            estado_midia_combo.grid(row=9, column=1, padx=4, pady=4, columnspan=3)

            def salvarAlteracoes():
                artistaId = self.controller_artista.ctCapturaId(artista.get())
                self.controller_disco.ctAlterarDisco(id_do_disco, titulo.get(), artistaId, genero.get(), ano.get(),
                                                     gravadora.get(), numero.get(), qualidade.get(),
                                                     estado_capa.get(), estado_midia.get())
                disco_window.destroy()
            
            salvar_button = tk.Button(master=disco_window, text="Salvar", width=30, height=1, command=salvarAlteracoes)
            salvar_button.grid(row=10, column=0, padx=4, pady=4, columnspan=3)
            
    def pesquisaDisco(self):
        pesquisar_window = tk.Toplevel()
        pesquisar_window.title("Pesquisar Discos")
        pesquisar_window.geometry("320x250")
        
        pesquisa_label = ttk.Label(master=pesquisar_window, text='Buscar por: ')
        pesquisa_label.grid(row=1, column=0, padx=4, pady=4, sticky='W')

        pesquisa = tk.StringVar()
        pesquisa_entry = ttk.Entry(master=pesquisar_window, textvariable=pesquisa)
        pesquisa_entry.grid(row=2, column=0, padx=4, pady=4)

        criterio = tk.StringVar()
        artistaRb = ttk.Radiobutton(master=pesquisar_window, text="Artista", variable=criterio, value="Artista")
        artistaRb.grid(row=1, column=1, columnspan=2)
        discoRb = ttk.Radiobutton(master=pesquisar_window, text="Disco", variable=criterio, value="Disco")
        discoRb.grid(row=1, column=3, columnspan=2)

        lista_discos = tk.Listbox(master=pesquisar_window, selectmode="single", bg="#a7f5a4", width=40)
        lista_discos.grid(row=4, column=0, padx=4, pady=4)
        
        def alimentaLista(_criterio, _pesquisa):
            lista_discos.delete(0, 'end')
            if _criterio == "Disco":
                query = self.controller_disco.ctBuscarPorTitulo(_pesquisa)
            else:
                query = self.controller_disco.ctBuscarPorArtista(_pesquisa)
            for disco in query:
                lista_discos.insert('end', disco)

        buscar_button = tk.Button(master=pesquisar_window, text="Buscar", width=30, height=1,
                                  command=lambda: alimentaLista(criterio.get(), pesquisa.get()))
        buscar_button.grid(row=3, column=0, padx=4, pady=4)
    
    def excluirDisco(self):
        excluir_window = tk.Toplevel()
        excluir_window.title("Excluir Discos")
        excluir_window.geometry("255x320")

        def alimentaLista(_criterio, _pesquisa):
            lista.delete(0, 'end')
            if _criterio == "Disco":
                query = self.controller_disco.ctBuscarPorTitulo(_pesquisa)
            else:
                query = self.controller_disco.ctBuscarPorArtista(_pesquisa)
            for disco in query:
                lista.insert('end', disco)

        pesquisa_label = ttk.Label(master=excluir_window, text='Buscar por: ')
        pesquisa_label.grid(row=1, column=0, padx=4, pady=4)
        
        pesquisa = tk.StringVar()
        pesquisa_entry = ttk.Entry(master=excluir_window, textvariable=pesquisa)
        pesquisa_entry.grid(row=2, column=0, padx=4, pady=4, columnspan=4)
        
        buscar_button = tk.Button(master=excluir_window, text="Buscar", width=30, height=1,
                                  command=lambda: alimentaLista(criterio.get(), pesquisa.get()))
        buscar_button.grid(row=3, column=0, padx=4, pady=4, columnspan=4)

        criterio = tk.StringVar()
        artistaRb = ttk.Radiobutton(master=excluir_window, text="Artista", variable=criterio, value="Artista")
        artistaRb.grid(row=1, column=1)
        discoRb = ttk.Radiobutton(master=excluir_window, text="Disco", variable=criterio, value="Disco")
        discoRb.grid(row=1, column=2)
        
        lista = tk.Listbox(master=excluir_window, selectmode="multiple", bg="#a7f5a4", width=40)
        lista.grid(row=4, column=0, padx=4, pady=4, columnspan=4)

        def get_ID():
            str_id = lista.get(lista.curselection())
            id_disco = int(str_id.split("-", 1)[0])
            return id_disco
        
        def excluir(id_disco):
            self.controller_disco.ctExcluirDisco(id_disco)
            excluir_window.destroy()

        excluir_button = tk.Button(master=excluir_window, text="Excluir", width=30, height=1,
                                   command=lambda: excluir(get_ID()))
        excluir_button.grid(row=6, column=0, padx=4, pady=4, columnspan=4)
