class Musica():

    def __init__(self, nome, interprete, compositor, genero, lado_disco):
        self.nome = nome
        self.interprete = interprete
        self.compositor = compositor
        self.genero = genero
        self.lado_disco = lado_disco
        
    
    def set_nome(self, value):
        self.nome = value
    
    
    def set_interprete(self, value):
        self.interprete = value
            
    
    def set_compositor(self, value):
        self.compositor = value
        
        
    def set_genero(self, value):
        self.genero = value
        
        
    def set_lado_disco(self, value):
        self.lado_disco = value
        
        
    def get_nome(self):
        return self.nome
    
    
    def get_interprete(self):
        return self.interprete
    
    
    def get_compositor(self):
        return self.compositor
    
    
    def get_genero(self):
        return self.genero
    
    
    def get_lado_disco(self):
        return self.lado_disco