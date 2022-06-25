import MySQLdb
from Model.dbconnect import db


class musicaMd(db):

    def __init__(self, nome="", compositor="", genero="", lado_disco="", artista_id=""):
        self.nome = nome
        self.compositor = compositor
        self.genero = genero
        self.lado_disco = lado_disco
        self.artista_id = artista_id

    def set_nome(self, value):
        self.nome = value

    def set_compositor(self, value):
        self.compositor = value

    def set_genero(self, value):
        self.genero = value

    def set_lado_disco(self, value):
        self.lado_disco = value
        
    def get_nome(self):
        return self.nome

    def get_compositor(self):
        return self.compositor
    
    def get_genero(self):
        return self.genero

    def get_lado_disco(self):
        return self.lado_disco

    def musicas_from_disco(self, idDisco):
        lista = []
        database = MySQLdb.connect(db.banco_host, db.banco_username, db.banco_password, db.banco_nome)
        cursor = database.cursor()
        sql = """SELECT m.musica_nome, m.musica_compositor, m.musica_genero, m.musica_lado_disco
                FROM musica_tbl m
                INNER JOIN musica_disco_tbl md
                ON m.musica_id = md.musica_tbl_musica_id
                INNER JOIN disco_tbl d
                ON d.disco_id = md.disco_tbl_disco_id
                WHERE d.disco_id = %s"""
        cursor.execute(sql, (idDisco,))
        result = cursor.fetchall()
        for tupla in result:
            lista.append(f"{tupla[0]}-{tupla[1]}-{tupla[2]}-{tupla[3]}")
        database.commit()
        database.close()
        return lista

    def musicas_id_from_disco(self, idDisco):
        lista = []
        database = MySQLdb.connect(db.banco_host, db.banco_username, db.banco_password, db.banco_nome)
        cursor = database.cursor()
        sql = """SELECT m.musica_id
                FROM musica_tbl m
                INNER JOIN musica_disco_tbl md
                ON m.musica_id = md.musica_tbl_musica_id
                INNER JOIN disco_tbl d
                ON d.disco_id = md.disco_tbl_disco_id
                WHERE d.disco_id = %s"""
        cursor.execute(sql, (idDisco,))
        result = cursor.fetchall()
        for tupla in result:
            lista.append(f"{tupla[0]}-{tupla[1]}-{tupla[2]}-{tupla[3]}")
        database.commit()
        database.close()
        return lista

    def cadastrarMusica(self, nome, compositor, genero, lado_disco, artista_id):
        musica = musicaMd(nome, compositor, genero, lado_disco, artista_id)
        database = MySQLdb.connect(db.banco_host, db.banco_username, db.banco_password, db.banco_nome)
        cursor = database.cursor()
        sql = f"""INSERT INTO musica_tbl (musica_nome, musica_compositor, musica_genero,
                musica_lado_disco, artista_id) VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(sql, (musica.get_nome(), musica.get_compositor(), musica.get_genero(), musica.get_lado_disco(), musica.artista_id))
        database.commit()
        database.close()

    def nova_musica_id(self, nome, compositor, genero, lado_disco, artista_id):
        database = MySQLdb.connect(db.banco_host, db.banco_username, db.banco_password, db.banco_nome)
        cursor = database.cursor()
        sql = """SELECT m.musica_id
                FROM musica_tbl m
                WHERE m.musica_nome = %s AND m.musica_compositor = %s AND m.musica_genero = %s
                 AND m.musica_lado_disco = %s AND m.artista_id = %s"""
        cursor.execute(sql, (nome, compositor, genero, lado_disco, artista_id))
        result = cursor.fetchone()
        database.commit()
        database.close()
        return result[0]

    def musica_disco_insert(self, id_nova_musica, id_disco):
        database = MySQLdb.connect(db.banco_host, db.banco_username, db.banco_password, db.banco_nome)
        cursor = database.cursor()
        sql = f"""INSERT INTO musica_disco_tbl (musica_tbl_musica_id, disco_tbl_disco_id) VALUES (%s,%s)"""
        cursor.execute(sql, (id_nova_musica, id_disco))
        database.commit()
        database.close()

    def buscarPorTitulo(self, titulo):
        lista = []
        database = MySQLdb.connect(db.banco_host, db.banco_username, db.banco_password, db.banco_nome)
        cursor = database.cursor()
        if titulo == "":
            sql = f"""SELECT musica_id, musica_nome, musica_compositor, musica_genero, musica_lado_disco, artista_nome FROM musica_tbl INNER JOIN artista_tbl
                                            ON musica_tbl.artista_id = artista_tbl.artista_id"""
        else:
            sql = f"""SELECT musica_id, musica_nome, musica_compositor, musica_genero, musica_lado_disco, artista_nome FROM musica_tbl INNER JOIN artista_tbl
                                            ON musica_tbl.artista_id = artista_tbl.artista_id WHERE musica_nome LIKE '%{titulo}%'"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for tupla in result:
            lista.append(f"{tupla[0]}-{tupla[1]}-{tupla[5]}-{tupla[2]}-{tupla[3]}-{tupla[4]}")
        database.commit()
        database.close()
        return lista

    def buscarPorInterprete(self, interprete):
        lista = []
        database = MySQLdb.connect(db.banco_host, db.banco_username, db.banco_password, db.banco_nome)
        cursor = database.cursor()
        if interprete == "":
            sql = f"""SELECT musica_id, musica_nome, musica_compositor, musica_genero, musica_lado_disco, artista_nome FROM musica_tbl INNER JOIN artista_tbl
                                                        ON musica_tbl.artista_id = artista_tbl.artista_id"""
        else:
            sql = f"""SELECT musica_id, musica_nome, musica_compositor, musica_genero, musica_lado_disco, artista_nome FROM musica_tbl INNER JOIN artista_tbl
                                                        ON musica_tbl.artista_id = artista_tbl.artista_id WHERE artista_nome LIKE '%{interprete}%'"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for tupla in result:
            lista.append(f"{tupla[0]}-{tupla[1]}-{tupla[5]}-{tupla[2]}-{tupla[3]}-{tupla[4]}")
        database.commit()
        database.close()
        return lista

    def AlterarMusica(self, alteracaoid, titulo, compositor, genero, lado_disco):
        database = MySQLdb.connect(db.banco_host, db.banco_username, db.banco_password, db.banco_nome)
        cursor = database.cursor()
        sql = f"""UPDATE musica_tbl SET musica_nome=%s, musica_compositor=%s, musica_genero=%s,
        musica_lado_disco=%s WHERE musica_id=%s"""
        cursor.execute(sql, [titulo, compositor, genero, lado_disco, alteracaoid])
        database.commit()
        database.close()

    def excluirMusica(self, idMusica):
        database = MySQLdb.connect(db.banco_host, db.banco_username, db.banco_password, db.banco_nome)
        cursor = database.cursor()
        sql = "DELETE FROM musica_disco_tbl WHERE musica_tbl_musica_id=%s"
        cursor.execute(sql, [idMusica])
        database.commit()
        sql = "DELETE FROM musica_tbl WHERE musica_id=%s"
        cursor.execute(sql, [idMusica])
        database.commit()
        database.close()
