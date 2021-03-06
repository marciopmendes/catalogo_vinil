from Model.musica import MusicaMd


class MusicaCt:
    musica_model = MusicaMd()

    def __init__(self):
        pass

    def ct_musicas_from_disco(self, id_disco):
        lista = self.musica_model.musicas_from_disco(id_disco)
        return lista

    def ctCadastrarMusica(self, nome, compositor, genero, lado_disco, artista_id):
        self.musica_model.cadastrarMusica(nome, compositor, genero, lado_disco, artista_id)

    def ct_nova_musica_id(self, nome, compositor, genero, lado_disco, artista_id):
        return self.musica_model.nova_musica_id(nome, compositor, genero, lado_disco, artista_id)

    def ct_musica_disco_insert(self, id_nova_musica, id_disco):
        self.musica_model.musica_disco_insert(id_nova_musica, id_disco)

    def ctBuscarPorTitulo(self, titulo):
        lista = self.musica_model.buscarPorTitulo(titulo)
        return lista

    def ctBuscarPorInterprete(self, interprete):
        lista = self.musica_model.buscarPorInterprete(interprete)
        return lista

    def ctAlterarMusica(self, alteracaoid, titulo, compositor, genero, lado_disco):
        self.musica_model.AlterarMusica(alteracaoid, titulo, compositor, genero, lado_disco)

    def ctExcluirMusica(self, id_musica):
        self.musica_model.excluirMusica(id_musica)
