class Disco():

    def __init__(self, titulo, artista, genero, ano, gravadora, musicas=None, numero_disco, qualidade, estado_capa, estado_midia):
        self.titulo = titulo
        self.artista = artista #não vai ser um atributo, vai ser um objeto Artista
        self.genero = genero
        self.ano = ano
        self.gravadora = gravadora
        self.numero_disco = numero_disco
        self.qualidade = qualidade
        self.estado_capa = estado_capa
        self.estado_midia = estado_midia

    def get_titulo(self):
        return self.titulo


    def get_artista(self):
        return self.artista


    def get_genero(self):
        return self.genero


    def get_ano(self):
        return self.ano


    def get_gravadora(self):
        return self.gravadora
    
    
    def get_numero_disco(self):
        return self.numero_disco
    
    
    def get_qualidade(self):
        return self.qualidade
    
    
    def get_estado_capa(self):
        return self.estado_capa
    
    
    def get_estado_midia(self):
        return self.estado_midia


    def set_titulo(self, value):
        self.titulo = value


    def set_artista(self, value):
        self.artista = value


    def set_genero(self, value):
        self.genero = value


    def set_ano(self, value):
        self.ano = value


    def set_gravadora(self, value):
        self.gravadora = value
        
        
    def set_numero_disco(self, value):
        self.numero_disco = value
        
    
    def set_qualidade(self, value):
        self.qualidade = value
        
    
    def set_estado_capa(self, value):
        self.estado_capa = value
    
    
    def set_estado_midia(self, value):
        self.estado_midia = value

