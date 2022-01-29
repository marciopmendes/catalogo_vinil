from Model.disco import discoMd
from Controller.controller_artista import artistaCt


class discoCt:

    disco_model = discoMd()
    artista_controller = artistaCt()

    def __init__(self):
        pass    

    def listaArtistas(self):
        lista = self.artista_controller.listaArtistas()
        return lista

    def getArtistaById(self, nome):
        artistaId = self.artista_controller.ctCapturaId(nome)
        return artistaId

    def ctCadastrarDisco(self, titulo, artistaId, genero, ano, gravadora, numero, qualidade, capa, midia):
        self.disco_model.cadastrarDisco(titulo, artistaId, genero, ano, gravadora, numero, qualidade, capa, midia)

    def ctBuscarPorTitulo(self, titulo):
        lista = self.disco_model.buscarPorTitulo(titulo)
        return lista

    def ctBuscarPorArtista(self, artista):
        lista = self.disco_model.buscarPorArtista(artista)
        return lista