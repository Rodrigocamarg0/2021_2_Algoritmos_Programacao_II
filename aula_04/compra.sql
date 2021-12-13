CREATE TABLE IF NOT EXISTS compra (
    id_compra_li INT PRIMARY KEY,
    produtos VARCHAR(1000) NOT NULL,
    valor_toral DECIMAL(15,2) NOT NULL,
    data DATE NOT NULL,
    pontos DECIMAL(15,2) NOT NULL,
    id_cliente_li INT,
    FOREIGN KEY (id_cliente_li) REFERENCES cliente(id_cliente_li)
)  ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS parceiro (
    nome VARCHAR(255) NOT NULL,
    descricao VARCHAR(1000),
    endereco VARCHAR(255),
    imagem VARCHAR(255),
    link VARCHAR(255),
    id_parceiro int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id_parceiro)
)  ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS beneficio (
    nome VARCHAR(255) NOT NULL,
    descricao VARCHAR(1000),
    cupom VARCHAR(255),
    imagem VARCHAR(255),
    nivel INT,
    id_beneficio int NOT NULL AUTO_INCREMENT,
    id_parceiro INT,
    FOREIGN KEY (id_parceiro) REFERENCES parceiro(id_parceiro),
    PRIMARY KEY (id_beneficio)
)  ENGINE=INNODB;