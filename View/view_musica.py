import tkinter as tk
from tkinter import ttk
from Controller.controller_musica import musicaCt
from Controller.controller_artista import artistaCt
from Controller.controller_disco import discoCt

class musicaVw:
    def __init__(self):
        self.controller_musica = musicaCt()
        self.controller_artista = artistaCt()
        self.controller_disco = discoCt()
    
    def cadastroMusica(self):
        cadastro_musica_window = tk.Toplevel()
        cadastro_musica_window.title("Cadastro de Músicas")
        cadastro_musica_window.geometry("255x360")
        
        # lista_musicas = []
        
        #Criação do formulário de cadastro
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
            discos = self.controller_disco.ctBuscarPorArtista(interprete.get())
            disco_combo['values'] = discos

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
        discos = self.controller_disco.ctBuscarPorArtista(lambda d: interprete.get())  # pegar os discos baseado no interprete selecionado
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
        
        finalizar_button = tk.Button(master=cadastro_musica_window, text="Finalizar Cadastro", command=cadastro_musica_window.destroy)
        finalizar_button.grid(row=7, column=3, padx=4, pady=4, columnspan=2)
        
        musicas_lb = tk.Listbox(master=cadastro_musica_window, bg="#a7f5a4", width=100)
        musicas_lb.grid(row=8, column=0, padx=4, pady=4, columnspan=4)
    
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
        interpreteRb = ttk.Radiobutton(master=pesquisar_window, text="Intérprete", variable=tipo_pesquisa, value="Intérprete")
        interpreteRb.grid(row=1, column=1)
        tituloRb = ttk.Radiobutton(master=pesquisar_window, text="Título", variable=tipo_pesquisa, value="Título")
        tituloRb.grid(row=1, column=2)

        lista = tk.Listbox(master=pesquisar_window, selectmode="single", bg="#a7f5a4", width=40)
        lista.grid(row=4, column=0, padx=4, pady=4, columnspan=4)
        
        pesquisa = tk.StringVar()
        pesquisa_entry = ttk.Entry(master=pesquisar_window, textvariable=pesquisa)
        pesquisa_entry.grid(row=2, column=0, padx=4, pady=4, columnspan=4)

        def alimentaLista(tipo_pesquisa, pesquisa):
            lista.delete(0, 'end')
            if tipo_pesquisa == "Título":
                query = self.controller_musica.ctBuscarPorTitulo(pesquisa)
            else:
                query = self.controller_musica.ctBuscarPorInterprete(pesquisa)
            for musica in query:
                lista.insert('end', musica)
        
        pesquisar_button = tk.Button(master=pesquisar_window, text="Pesquisar", width=30, height=1,
                                     command=lambda: alimentaLista(tipo_pesquisa.get(),pesquisa.get()))
        pesquisar_button.grid(row=3, column=0, padx=4, pady=4, columnspan=4)
    
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
        
    