from Model.disco import DiscoMd
from Controller.controller_artista import ArtistaCt


class DiscoCt:

    disco_model = DiscoMd()
    artista_controller = ArtistaCt()

    def __init__(self):
        pass    

    def listaArtistas(self):
        lista = self.artista_controller.listaArtistas()
        return lista

    def getArtistaById(self, nome):
        artistaId = self.artista_controller.ctCapturaId(nome)
        return artistaId

    def ctCadastrarDisco(self, titulo, artista_id, genero, ano, gravadora, numero, qualidade, capa, midia):
        self.disco_model.cadastrarDisco(titulo, artista_id, genero, ano, gravadora, numero, qualidade, capa, midia)

    def ctBuscarPorTitulo(self, titulo):
        lista = self.disco_model.buscarPorTitulo(titulo)
        return lista

    def ctBuscarPorArtista(self, artista):
        lista = self.disco_model.buscarPorArtista(artista)
        return lista

    def ctAlterarDisco(self, id_do_disco, titulo, artista_id, genero, ano, gravadora, numero, qualidade, estado_capa,
                       estado_midia):
        self.disco_model.alterarDisco(id_do_disco, titulo, artista_id, genero, ano, gravadora, numero, qualidade,
                                      estado_capa, estado_midia)

    def ctExcluirDisco(self, id_disco):
        self.disco_model.excluirDisco(id_disco)
