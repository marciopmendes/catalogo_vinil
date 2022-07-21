import MySQLdb
from Model.dbconnect import DatabaseMd


class ArtistaMd(DatabaseMd):
    
    def __init__(self, nome=""):
        self.nome = nome
        
    def get_nome(self):
        return self.nome
    
    def set_nome(self, value):
        self.nome = value
    
    def cadastrarArtista(self, nome):
        artista = ArtistaMd(nome)
        database = MySQLdb.connect(DatabaseMd.banco_host, DatabaseMd.banco_username, DatabaseMd.banco_password,
                                   DatabaseMd.banco_nome)
        cursor = database.cursor()
        sql = f"INSERT INTO artista_tbl (artista_nome) VALUES (%s)"
        cursor.execute(sql, [artista.get_nome()])
        database.commit()
        database.close()
        
    def buscarArtista(self, nome):
        lista = []
        database = MySQLdb.connect(DatabaseMd.banco_host, DatabaseMd.banco_username, DatabaseMd.banco_password,
                                   DatabaseMd.banco_nome)
        cursor = database.cursor()
        if nome == "":
            sql = f"SELECT artista_nome FROM artista_tbl"
        else:
            sql = f"SELECT artista_nome FROM artista_tbl WHERE artista_nome LIKE '%{nome}%'"
        cursor.execute(sql)
        result = cursor.fetchall()
        for tupla in result:
            lista.append(tupla[0])
        database.commit()
        database.close()
        return lista
    
    def capturaId(self, nome):
        artista = ArtistaMd(nome)
        database = MySQLdb.connect(DatabaseMd.banco_host, DatabaseMd.banco_username, DatabaseMd.banco_password,
                                   DatabaseMd.banco_nome)
        cursor = database.cursor()
        sql = f"SELECT artista_id FROM artista_tbl WHERE artista_nome=%s"
        cursor.execute(sql, [artista.get_nome()])
        result = cursor.fetchone()
        database.commit()
        database.close()
        artistaId = result[0]
        return artistaId
    
    def alterarArtista(self, artista_id, artista_nome):
        artista = ArtistaMd(artista_nome)
        database = MySQLdb.connect(DatabaseMd.banco_host, DatabaseMd.banco_username, DatabaseMd.banco_password,
                                   DatabaseMd.banco_nome)
        cursor = database.cursor()
        sql = f"UPDATE artista_tbl SET artista_nome=%s WHERE artista_id=%s"
        cursor.execute(sql, [artista.get_nome(), artista_id])
        database.commit()
        database.close()
        
    def excluirArtistas(self, lista_ids):
        database = MySQLdb.connect(DatabaseMd.banco_host, DatabaseMd.banco_username, DatabaseMd.banco_password,
                                   DatabaseMd.banco_nome)
        for artista_id in lista_ids:
            cursor = database.cursor()
            sql = f"DELETE FROM artista_tbl WHERE artista_id=%s"
            cursor.execute(sql, [artista_id])
            database.commit()
        database.close()

    def listaArtistas(self):
        lista = []
        database = MySQLdb.connect(DatabaseMd.banco_host, DatabaseMd.banco_username, DatabaseMd.banco_password,
                                   DatabaseMd.banco_nome)
        cursor = database.cursor()
        sql = "SELECT artista_nome FROM artista_tbl ORDER BY artista_nome ASC"
        cursor.execute(sql)
        result = cursor.fetchall()
        database.commit()
        database.close()
        for tupla in result:
            lista.append(tupla[0])
        return lista
