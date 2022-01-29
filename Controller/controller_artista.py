from Model.artista import artistaMd

class artistaCt:
    
    artista_model = artistaMd()
    
    def __init__(self):
        pass
    
    def ctCadastrarArtista(self, nome):
        self.artista_model.cadastrarArtista(nome)
        
    def ctBuscarArtista(self, nome):
        lista = self.artista_model.buscarArtista(nome)
        return lista
    
    def ctCapturaId(self, nome):
        artistaId = self.artista_model.capturaId(nome)
        return artistaId
    
    def ctExcluirArtistas(self, listaIds):
        self.artista_model.excluirArtistas(listaIds)
    
    def ctAlterarArtista(self, artistaId, artistaNome):
        self.artista_model.alterarArtista(artistaId, artistaNome)

    def listaArtistas(self):
        lista = self.artista_model.listaArtistas()
        return lista