from Model.artista import ArtistaMd


class ArtistaCt:
    
    artista_model = ArtistaMd()
    
    def __init__(self):
        pass
    
    def ctCadastrarArtista(self, nome):
        self.artista_model.cadastrarArtista(nome)
        
    def ctBuscarArtista(self, nome):
        lista = self.artista_model.buscarArtista(nome)
        return lista
    
    def ctCapturaId(self, nome):
        artista_id = self.artista_model.capturaId(nome)
        return artista_id
    
    def ctExcluirArtistas(self, lista_ids):
        self.artista_model.excluirArtistas(lista_ids)
    
    def ctAlterarArtista(self, artista_id, artista_nome):
        self.artista_model.alterarArtista(artista_id, artista_nome)

    def listaArtistas(self):
        lista = self.artista_model.listaArtistas()
        return lista
