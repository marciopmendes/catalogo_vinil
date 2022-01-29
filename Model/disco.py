import MySQLdb
from Model.dbconnect import db

class discoMd(db):

    def __init__(self, titulo="", artistaId=0, genero="", ano=0, gravadora="", numero_disco=0, qualidade="", estado_capa="", estado_midia=""):
        self.titulo = titulo
        self.artistaId = artistaId #não vai ser um atributo, vai ser um ID
        self.genero = genero
        self.ano = ano
        self.gravadora = gravadora
        self.numero_disco = numero_disco
        self.qualidade = qualidade
        self.estado_capa = estado_capa
        self.estado_midia = estado_midia

    def get_titulo(self):
        return self.titulo


    def get_artistaId(self):
        return self.artistaId


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


    def set_artistaId(self, value):
        self.artistaId = value


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

    def cadastrarDisco(self, titulo, artistaId, genero, ano, gravadora, numero, qualidade, capa, midia):
        disco = discoMd(titulo, artistaId, genero, ano, gravadora, numero, qualidade, capa, midia)
        database = MySQLdb.connect(db.banco_host, db.banco_username, db.banco_password, db.banco_nome)
        cursor = database.cursor()
        sql = f"""INSERT INTO disco_tbl (disco_titulo, artista_id, disco_genero, disco_ano, disco_gravadora, disco_numero, disco_qualidade,
                                        disco_estado_capa, disco_estado_midia) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql, [disco.get_titulo(), disco.get_artistaId(), disco.get_genero(), disco.get_ano(), disco.get_gravadora(), disco.get_numero_disco(), disco.get_qualidade(), disco.get_estado_capa(), disco.get_estado_midia()])
        database.commit()
        database.close()

    def buscarPorTitulo(self, titulo):
        lista = []
        database = MySQLdb.connect(db.banco_host, db.banco_username, db.banco_password, db.banco_nome)
        cursor = database.cursor()
        sql = f"""SELECT disco_titulo, disco_ano, disco_numero, artista_nome FROM disco_tbl INNER JOIN artista_tbl
                ON disco_tbl.artista_id = artista_tbl.artista_id WHERE disco_titulo LIKE '%{titulo}%'"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for tupla in result:
            lista.append(f"Título: {tupla[0]}, Artista: {tupla[3]}, Ano: {tupla[1]}, Número do disco: {tupla[2]}")
        database.commit()
        database.close()
        return lista

    def buscarPorArtista(self, artista):
        lista = []
        database = MySQLdb.connect(db.banco_host, db.banco_username, db.banco_password, db.banco_nome)
        cursor = database.cursor()
        sql = f"""SELECT disco_titulo, disco_ano, disco_numero, artista_nome FROM disco_tbl INNER JOIN artista_tbl
                ON disco_tbl.artista_id = artista_tbl.artista_id WHERE artista_nome LIKE '%{artista}%'"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for tupla in result:
            lista.append(f"Título: {tupla[0]}, Artista: {tupla[3]}, Ano: {tupla[1]}, Número do disco: {tupla[2]}")
        database.commit()
        database.close()
        return lista