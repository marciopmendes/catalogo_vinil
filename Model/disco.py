import MySQLdb
from Model.dbconnect import DatabaseMd


class DiscoMd(DatabaseMd):

    def __init__(self, titulo="", artista_id=0, genero="", ano=0, gravadora="", numero_disco=0, qualidade="",
                 estado_capa="", estado_midia=""):
        self.titulo = titulo
        self.artistaId = artista_id
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

    def cadastrarDisco(self, titulo, artista_id, genero, ano, gravadora, numero, qualidade, capa, midia):
        disco = DiscoMd(titulo, artista_id, genero, ano, gravadora, numero, qualidade, capa, midia)
        database = MySQLdb.connect(DatabaseMd.banco_host, DatabaseMd.banco_username, DatabaseMd.banco_password,
                                   DatabaseMd.banco_nome)
        cursor = database.cursor()
        sql = f"""INSERT INTO disco_tbl (disco_titulo, artista_id, disco_genero, disco_ano, disco_gravadora,
         disco_numero, disco_qualidade, disco_estado_capa, disco_estado_midia) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql, [disco.get_titulo(), disco.get_artistaId(), disco.get_genero(), disco.get_ano(),
                             disco.get_gravadora(), disco.get_numero_disco(), disco.get_qualidade(),
                             disco.get_estado_capa(), disco.get_estado_midia()])
        database.commit()
        database.close()

    def buscarPorTitulo(self, titulo):
        lista = []
        database = MySQLdb.connect(DatabaseMd.banco_host, DatabaseMd.banco_username, DatabaseMd.banco_password,
                                   DatabaseMd.banco_nome)
        cursor = database.cursor()
        if titulo == "":
            sql = f"""SELECT disco_id, disco_titulo, disco_ano, disco_numero, artista_nome FROM disco_tbl INNER JOIN
             artista_tbl ON disco_tbl.artista_id = artista_tbl.artista_id"""
        else:
            sql = f"""SELECT disco_id, disco_titulo, disco_ano, disco_numero, artista_nome FROM disco_tbl INNER JOIN
             artista_tbl ON disco_tbl.artista_id = artista_tbl.artista_id WHERE disco_titulo LIKE '%{titulo}%'"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for tupla in result:
            lista.append(f"{tupla[0]}-{tupla[1]}-{tupla[4]}-{tupla[2]}-{tupla[3]}")
        database.commit()
        database.close()
        return lista

    def buscarPorArtista(self, artista):
        lista = []
        database = MySQLdb.connect(DatabaseMd.banco_host, DatabaseMd.banco_username, DatabaseMd.banco_password,
                                   DatabaseMd.banco_nome)
        cursor = database.cursor()
        if artista == "":
            sql = f"""SELECT disco_id, disco_titulo, disco_ano, disco_numero, artista_nome FROM disco_tbl INNER JOIN
             artista_tbl ON disco_tbl.artista_id = artista_tbl.artista_id"""
        else:
            sql = f"""SELECT disco_id, disco_titulo, disco_ano, disco_numero, artista_nome FROM disco_tbl INNER JOIN
             artista_tbl ON disco_tbl.artista_id = artista_tbl.artista_id WHERE artista_nome LIKE '%{artista}%'"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for tupla in result:
            lista.append(f"{tupla[0]}-{tupla[1]}-{tupla[4]}-{tupla[2]}-{tupla[3]}")
        database.commit()
        database.close()
        return lista

    def alterarDisco(self, id_do_disco, titulo, artista_id, genero, ano, gravadora, numero, qualidade, estado_capa,
                     estado_midia):
        database = MySQLdb.connect(DatabaseMd.banco_host, DatabaseMd.banco_username, DatabaseMd.banco_password,
                                   DatabaseMd.banco_nome)
        cursor = database.cursor()
        sql = f"""UPDATE disco_tbl SET disco_titulo=%s, artista_id=%s, disco_genero=%s, disco_ano=%s,
              disco_gravadora=%s, disco_numero=%s, disco_qualidade=%s, disco_estado_capa=%s, disco_estado_midia=%s
               WHERE disco_id=%s"""
        cursor.execute(sql, [titulo, artista_id, genero, ano, gravadora, numero, qualidade, estado_capa, estado_midia,
                             id_do_disco])
        database.commit()
        database.close()

    def excluirDisco(self, id_disco):
        database = MySQLdb.connect(DatabaseMd.banco_host, DatabaseMd.banco_username, DatabaseMd.banco_password,
                                   DatabaseMd.banco_nome)
        cursor = database.cursor()
        sql = "DELETE FROM musica_disco_tbl WHERE disco_tbl_disco_id=%s"
        cursor.execute(sql, [id_disco])
        database.commit()
        sql = "DELETE FROM disco_tbl WHERE disco_id=%s"
        cursor.execute(sql, [id_disco])
        database.commit()
        database.close()
