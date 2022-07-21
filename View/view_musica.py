import tkinter as tk
from tkinter import ttk
from Controller.controller_musica import MusicaCt
from Controller.controller_artista import ArtistaCt
from Controller.controller_disco import DiscoCt


class MusicaVw:
    def __init__(self):
        self.controller_musica = MusicaCt()
        self.controller_artista = ArtistaCt()
        self.controller_disco = DiscoCt()
    
    def cadastroMusica(self):
        cadastro_musica_window = tk.Toplevel()
        cadastro_musica_window.title("Cadastro de Músicas")
        cadastro_musica_window.geometry("255x360")

        titulo_label = ttk.Label(master=cadastro_musica_window, text='Título da Música')
        titulo_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        titulo = tk.StringVar()
        titulo_entry = ttk.Entry(master=cadastro_musica_window, textvariable=titulo)
        titulo_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)
        
        interprete_label = ttk.Label(master=cadastro_musica_window, text='Intérprete')
        interprete_label.grid(row=2, column=0, padx=4, pady=4, columnspan=1)
        interprete = tk.StringVar()

        def trace_interprete_combo(*args):
            interprete.set(interprete_combo.get())

        interpretes = self.controller_artista.listaArtistas()  # lista com todos os artistas, ordem alfabética
        interprete_combo = ttk.Combobox(master=cadastro_musica_window, values=interpretes, state='readonly')
        interprete_combo.grid(row=2, column=1, padx=4, pady=4, columnspan=3)
        interprete_combo.bind('<<ComboboxSelected>>', trace_interprete_combo)

        def trace_interprete(*args):
            disco_combo.set('')
            _discos = self.controller_disco.ctBuscarPorArtista(interprete.get())
            disco_combo['values'] = _discos

        def get_disco_ID():
            str_id = disco_combo.get()
            id_disco = int(str_id.split("-", 1)[0])
            return id_disco

        def on_disco_change(*args):
            id_disco = get_disco_ID()
            musicas_lb.delete(0, 'end')
            lista = self.controller_musica.ct_musicas_from_disco(id_disco)
            for musica in lista:
                musicas_lb.insert('end', musica)

        disco_label = ttk.Label(master=cadastro_musica_window, text='Disco')
        disco_label.grid(row=3, column=0, padx=4, pady=4, columnspan=1)
        interprete.trace_add('write', trace_interprete)
        discos = self.controller_disco.ctBuscarPorArtista(lambda d: interprete.get())
        disco_combo = ttk.Combobox(master=cadastro_musica_window, values=discos, state='readonly')
        disco_combo.grid(row=3, column=1, padx=4, pady=4, columnspan=3)
        disco_combo.bind('<<ComboboxSelected>>', on_disco_change)
        
        compositor_label = ttk.Label(master=cadastro_musica_window, text='Compositor')
        compositor_label.grid(row=4, column=0, padx=4, pady=4, columnspan=1)
        
        compositor = tk.StringVar()
        compositor_entry = ttk.Entry(master=cadastro_musica_window, textvariable=compositor)
        compositor_entry.grid(row=4, column=1, padx=4, pady=4, columnspan=3)
        
        genero_label = ttk.Label(master=cadastro_musica_window, text='Gênero')
        genero_label.grid(row=5, column=0, padx=4, pady=4, columnspan=1)
        
        genero = tk.StringVar()
        genero_entry = ttk.Entry(master=cadastro_musica_window, textvariable=genero)
        genero_entry.grid(row=5, column=1, padx=4, pady=4, columnspan=3)
        
        lado_disco_label = ttk.Label(master=cadastro_musica_window, text='Lado do Disco')
        lado_disco_label.grid(row=6, column=0, padx=4, pady=4, columnspan=1)
        
        lado_disco = tk.StringVar()
        lado_disco_entry = ttk.Entry(master=cadastro_musica_window, textvariable=lado_disco)
        lado_disco_entry.grid(row=6, column=1, padx=4, pady=4, columnspan=3)

        def reset_form():
            titulo_entry.delete(0, 'end')
            compositor_entry.delete(0, 'end')
            genero_entry.delete(0, 'end')
            lado_disco_entry.delete(0, 'end')

        def adiciona_musica():
            artista_id = self.controller_artista.ctCapturaId(interprete_combo.get())
            musica = f"{titulo.get()}-{compositor.get()}-{genero.get()}-{lado_disco.get()}"
            musicas_lb.insert('end', musica)
            self.controller_musica.ctCadastrarMusica(titulo.get(), compositor.get(), genero.get(), lado_disco.get(),
                                                     artista_id)
            id_nova_musica = self.controller_musica.ct_nova_musica_id(titulo.get(), compositor.get(), genero.get(),
                                                                      lado_disco.get(), artista_id)
            id_disco = get_disco_ID()
            self.controller_musica.ct_musica_disco_insert(id_nova_musica, id_disco)
            reset_form()

        adicionar_button = tk.Button(master=cadastro_musica_window, text="Adicionar Música", command=adiciona_musica)
        adicionar_button.grid(row=7, column=0, padx=4, pady=4, columnspan=2)
        
        finalizar_button = tk.Button(master=cadastro_musica_window, text="Finalizar Cadastro",
                                     command=cadastro_musica_window.destroy)
        finalizar_button.grid(row=7, column=3, padx=4, pady=4, columnspan=2)
        
        musicas_lb = tk.Listbox(master=cadastro_musica_window, bg="#a7f5a4", width=100)
        musicas_lb.grid(row=8, column=0, padx=4, pady=4, columnspan=4)
    
    def alterarMusica(self):
        alterar_window = tk.Toplevel()
        alterar_window.title("Alterar Música")
        alterar_window.geometry("255x350")

        musica_label = ttk.Label(master=alterar_window, text='Nome da Música')
        musica_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        musica = tk.StringVar()
        musica_entry = ttk.Entry(master=alterar_window, textvariable=musica)
        musica_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)

        lista = tk.Listbox(master=alterar_window, selectmode="single", bg="#a7f5a4", width=40)
        lista.grid(row=3, column=0, padx=4, pady=4, columnspan=4)

        def alimentaLista(_musica):
            lista.delete(0, 'end')
            query = self.controller_musica.ctBuscarPorTitulo(_musica)
            for row in query:
                lista.insert('end', row)

        buscar_button = tk.Button(master=alterar_window, text="Buscar", width=30, height=1,
                                  command=lambda: alimentaLista(musica.get()))
        buscar_button.grid(row=2, column=0, padx=4, pady=4, columnspan=4)

        def get_ID():
            str_id = lista.get(lista.curselection())
            id_musica = int(str_id.split("-", 1)[0])
            return id_musica

        alterar_button = tk.Button(master=alterar_window, text="Alterar Música Selecionada", width=30, height=1,
                                   command=lambda: alterarMusicaForm(get_ID()))
        alterar_button.grid(row=4, column=0, padx=4, pady=4, columnspan=4)

        def alterarMusicaForm(alteracao_id):
            musica_window = tk.Toplevel()
            musica_window.title("Informações da Música")
            musica_window.geometry("230x150")
            
            titulo_label = ttk.Label(master=musica_window, text='Título da Música')
            titulo_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
            titulo = tk.StringVar()
            titulo_entry = ttk.Entry(master=musica_window, textvariable=titulo)
            titulo_entry.grid(row=1, column=1, padx=4, pady=4, columnspan=3)

            compositor_label = ttk.Label(master=musica_window, text='Compositor')
            compositor_label.grid(row=2, column=0, padx=4, pady=4, columnspan=1)
            
            compositor = tk.StringVar()
            compositor_entry = ttk.Entry(master=musica_window, textvariable=compositor)
            compositor_entry.grid(row=2, column=1, padx=4, pady=4, columnspan=3)
            
            genero_label = ttk.Label(master=musica_window, text='Gênero')
            genero_label.grid(row=3, column=0, padx=4, pady=4, columnspan=1)
            
            genero = tk.StringVar()
            genero_entry = ttk.Entry(master=musica_window, textvariable=genero)
            genero_entry.grid(row=3, column=1, padx=4, pady=4, columnspan=3)
            
            lado_disco_label = ttk.Label(master=musica_window, text='Lado do Disco')
            lado_disco_label.grid(row=4, column=0, padx=4, pady=4, columnspan=1)
            
            lado_disco = tk.StringVar()
            lado_disco_entry = ttk.Entry(master=musica_window, textvariable=lado_disco)
            lado_disco_entry.grid(row=4, column=1, padx=4, pady=4, columnspan=3)

            def salvarAlteracoes():
                self.controller_musica.ctAlterarMusica(alteracao_id, titulo.get(), compositor.get(),
                                                       genero.get(), lado_disco.get())
                musica_window.destroy()

            salvar_button = tk.Button(master=musica_window, text="Salvar", width=30, height=1,
                                      command=salvarAlteracoes)
            salvar_button.grid(row=10, column=0, padx=4, pady=4, columnspan=3)
            
    def pesquisaMusica(self):
        pesquisar_window = tk.Toplevel()
        pesquisar_window.title("Pesquisar Músicas")
        pesquisar_window.geometry("255x350")
        
        pesquisar_label = ttk.Label(master=pesquisar_window, text='Pesquisar Por:')
        pesquisar_label.grid(row=1, column=0, padx=4, pady=4, columnspan=1)
        
        tipo_pesquisa = tk.StringVar()
        interpreteRb = ttk.Radiobutton(master=pesquisar_window, text="Intérprete", variable=tipo_pesquisa,
                                       value="Intérprete")
        interpreteRb.grid(row=1, column=1)
        tituloRb = ttk.Radiobutton(master=pesquisar_window, text="Título", variable=tipo_pesquisa, value="Título")
        tituloRb.grid(row=1, column=2)

        lista = tk.Listbox(master=pesquisar_window, selectmode="single", bg="#a7f5a4", width=40)
        lista.grid(row=4, column=0, padx=4, pady=4, columnspan=4)
        
        pesquisa = tk.StringVar()
        pesquisa_entry = ttk.Entry(master=pesquisar_window, textvariable=pesquisa)
        pesquisa_entry.grid(row=2, column=0, padx=4, pady=4, columnspan=4)

        def alimentaLista(_tipo_pesquisa, _pesquisa):
            lista.delete(0, 'end')
            if _tipo_pesquisa == "Título":
                query = self.controller_musica.ctBuscarPorTitulo(_pesquisa)
            else:
                query = self.controller_musica.ctBuscarPorInterprete(_pesquisa)
            for musica in query:
                lista.insert('end', musica)
        
        pesquisar_button = tk.Button(master=pesquisar_window, text="Pesquisar", width=30, height=1,
                                     command=lambda: alimentaLista(tipo_pesquisa.get(), pesquisa.get()))
        pesquisar_button.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
    
    def excluirMusica(self):
        excluir_window = tk.Toplevel()
        excluir_window.title("Excluir Músicas")
        excluir_window.geometry("255x350")

        def alimentaLista(_criterio, _pesquisa):
            lista.delete(0, 'end')
            if _criterio == "Artista":
                query = self.controller_musica.ctBuscarPorInterprete(_pesquisa)
            else:
                query = self.controller_musica.ctBuscarPorTitulo(_pesquisa)
            for musica in query:
                lista.insert('end', musica)

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
        tituloRb = ttk.Radiobutton(master=excluir_window, text="Titulo", variable=criterio, value="Titulo")
        tituloRb.grid(row=1, column=2)

        lista = tk.Listbox(master=excluir_window, selectmode="multiple", bg="#a7f5a4", width=40)
        lista.grid(row=4, column=0, padx=4, pady=4, columnspan=4)

        def get_ID():
            str_id = lista.get(lista.curselection())
            id_musica = int(str_id.split("-", 1)[0])
            return id_musica

        def excluir(id_musica):
            self.controller_musica.ctExcluirMusica(id_musica)
            excluir_window.destroy()

        excluir_button = tk.Button(master=excluir_window, text="Excluir", width=30, height=1,
                                   command=lambda: excluir(get_ID()))
        excluir_button.grid(row=6, column=0, padx=4, pady=4, columnspan=4)
    