import MySQLdb

class db:
    banco_host = "localhost"
    banco_username = "root"
    banco_password = "rkv83wwv"
    banco_nome = "mydb"
    
    def __init__(self):
        pass
    
    def getHost(self):
        return self.banco_host
    
    def getUsername(self):
        return self.banco_username

    def getPassword(self):
        return self.banco_password

    def getNome(self):
        return self.banco_nome

    def setHost(self, host):
        self.banco_host = host
    
    def setUsername(self, username):
        self.banco_username = username

    def setPassword(self, password):
        self.banco_password = password

    def setNome(self, nome):
        self.banco_nome = nome
        
    def dbConnect(self):
        db = MySQLdb.connect(self.banco_host, self.banco_username, self.banco_password, self.banco_nome)
        cursor = db.cursor()
        sql = f"""
        SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
        SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
        SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
        
        -- -----------------------------------------------------
        -- Schema {self.banco_nome}
        -- -----------------------------------------------------
        
        -- -----------------------------------------------------
        -- Schema {self.banco_nome}
        -- -----------------------------------------------------
        CREATE SCHEMA IF NOT EXISTS `{self.banco_nome}` DEFAULT CHARACTER SET utf8 ;
        USE `{self.banco_nome}` ;
        
        -- -----------------------------------------------------
        -- Table `{self.banco_nome}`.`artista_tbl`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `{self.banco_nome}`.`artista_tbl` (
          `artista_id` INT NOT NULL AUTO_INCREMENT,
          `artista_nome` VARCHAR(100) NOT NULL,
          PRIMARY KEY (`artista_id`),
          UNIQUE INDEX `idartista_UNIQUE` (`artista_id` ASC) VISIBLE)
        ENGINE = InnoDB;
        
        
        -- -----------------------------------------------------
        -- Table `{self.banco_nome}`.`disco_tbl`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `{self.banco_nome}`.`disco_tbl` (
          `disco_id` INT NOT NULL AUTO_INCREMENT,
          `disco_titulo` VARCHAR(80) NOT NULL,
          `disco_genero` VARCHAR(30) NOT NULL,
          `disco_ano` INT(4) NOT NULL,
          `disco_gravadora` VARCHAR(50) NOT NULL,
          `disco_numero` INT(1) NOT NULL COMMENT 'Padrão = 1. Em caso de discos duplos ou triplos, 2, 3 ...',
          `disco_qualidade` VARCHAR(10) NOT NULL COMMENT 'Estéreo ou Mono',
          `disco_estado_capa` VARCHAR(8) NOT NULL,
          `disco_estado_midia` VARCHAR(8) NOT NULL,
          `artista_id` INT NOT NULL,
          PRIMARY KEY (`disco_id`, `artista_id`),
          UNIQUE INDEX `disco_id_UNIQUE` (`disco_id` ASC) VISIBLE,
          INDEX `fk_disco_tbl_artista1_idx` (`artista_id` ASC) VISIBLE,
          CONSTRAINT `fk_disco_tbl_artista1`
            FOREIGN KEY (`artista_id`)
            REFERENCES `{self.banco_nome}`.`artista_tbl` (`artista_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
        ENGINE = InnoDB;
        
        
        -- -----------------------------------------------------
        -- Table `{self.banco_nome}`.`musica_tbl`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `{self.banco_nome}`.`musica_tbl` (
          `musica_id` INT NOT NULL AUTO_INCREMENT,
          `musica_nome` VARCHAR(80) NOT NULL,
          `musica_compositor` VARCHAR(100) NOT NULL,
          `musica_genero` VARCHAR(30) NOT NULL,
          `musica_lado_disco` VARCHAR(5) NOT NULL,
          `artista_id` INT NOT NULL,
          PRIMARY KEY (`musica_id`, `artista_id`),
          UNIQUE INDEX `musica_id_UNIQUE` (`musica_id` ASC) VISIBLE,
          INDEX `fk_musica_tbl_artista1_idx` (`artista_id` ASC) VISIBLE,
          CONSTRAINT `fk_musica_tbl_artista1`
            FOREIGN KEY (`artista_id`)
            REFERENCES `{self.banco_nome}`.`artista_tbl` (`artista_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
        ENGINE = InnoDB;
        
        
        -- -----------------------------------------------------
        -- Table `{self.banco_nome}`.`musica_disco_tbl`
        -- -----------------------------------------------------
        CREATE TABLE IF NOT EXISTS `{self.banco_nome}`.`musica_disco_tbl` (
          `disco_tbl_disco_id` INT NOT NULL,
          `musica_tbl_musica_id` INT NOT NULL,
          PRIMARY KEY (`disco_tbl_disco_id`, `musica_tbl_musica_id`),
          INDEX `fk_disco_tbl_has_musica_tbl_musica_tbl1_idx` (`musica_tbl_musica_id` ASC) VISIBLE,
          INDEX `fk_disco_tbl_has_musica_tbl_disco_tbl_idx` (`disco_tbl_disco_id` ASC) VISIBLE,
          CONSTRAINT `fk_disco_tbl_has_musica_tbl_disco_tbl`
            FOREIGN KEY (`disco_tbl_disco_id`)
            REFERENCES `{self.banco_nome}`.`disco_tbl` (`disco_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
          CONSTRAINT `fk_disco_tbl_has_musica_tbl_musica_tbl1`
            FOREIGN KEY (`musica_tbl_musica_id`)
            REFERENCES `{self.banco_nome}`.`musica_tbl` (`musica_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
        ENGINE = InnoDB;
        
        
        SET SQL_MODE=@OLD_SQL_MODE;
        SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
        SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;"""
        
        cursor.execute(sql)
        db.close()
