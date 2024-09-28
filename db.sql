CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status TINYINT NOT NULL,
    nome_social VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,  
    senha VARCHAR(32) NOT NULL,  
    origem VARCHAR(50) NOT NULL,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    foto_conta VARCHAR(255),  
    nome_completo VARCHAR(150) DEFAULT NULL,
    data_nascimento DATE DEFAULT NULL,
    cpf VARCHAR(14) DEFAULT NULL,  
    estado_civil VARCHAR(20) DEFAULT NULL,
    foto_cnh_url VARCHAR(255) DEFAULT NULL,
    foto_qrcode_cnh_url VARCHAR(255) DEFAULT NULL,
    pdf_cnh_url VARCHAR(255) DEFAULT NULL,
    rg VARCHAR(50) DEFAULT NULL,
    nome_mae VARCHAR(100) DEFAULT NULL,
    nome_pai VARCHAR(100) DEFAULT NULL,
    cnh VARCHAR(20) DEFAULT NULL,
    CONSTRAINT unique_email_cpf UNIQUE (email, cpf)  
);

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status TINYINT NOT NULL,
    nome_social VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(32) NOT NULL,
    origem VARCHAR(50) NOT NULL,
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    foto_conta VARCHAR(255),
    nome_completo VARCHAR(150) DEFAULT NULL,
    data_nascimento DATE DEFAULT NULL,
    cpf VARCHAR(14) DEFAULT NULL,
    estado_civil VARCHAR(20) DEFAULT NULL,
    foto_cnh_url VARCHAR(255) DEFAULT NULL,
    foto_qrcode_cnh_url VARCHAR(255) DEFAULT NULL,
    pdf_cnh_url VARCHAR(255) DEFAULT NULL,
    rg VARCHAR(50) DEFAULT NULL,
    nome_mae VARCHAR(100) DEFAULT NULL,
    nome_pai VARCHAR(100) DEFAULT NULL,
    cnh VARCHAR(20) DEFAULT NULL,
    CONSTRAINT unique_email_cpf UNIQUE (email, cpf)
);


├── main.py
├── models.py
├── schemas.py
├── crud.py
└── database.py