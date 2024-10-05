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


-- Script do imovel 

CREATE TABLE Imoveis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,  -- Referência ao usuário (proprietário do imóvel)
    status INT NOT NULL,  -- Status numérico para indicar o estágio no fluxo
    classificacao ENUM('Comercial', 'Residencial', 'Outros') DEFAULT NULL,
    tipo VARCHAR(50) DEFAULT NULL,  -- Ex: Casa, Prédio, Kit, Lote, Sala Comercial...
    numero_quartos TINYINT DEFAULT NULL,
    numero_suites TINYINT DEFAULT NULL,
    numero_banheiros TINYINT DEFAULT NULL,
    numero_garagem TINYINT DEFAULT NULL,
    orientacao_sol ENUM('Poente', 'Nascente', 'Perpendicular') DEFAULT NULL,
    area_total DECIMAL(10, 2) DEFAULT NULL,  -- Área total em m²
    area_privativa DECIMAL(10, 2) DEFAULT NULL,  -- Área privativa em m²
    descricao_complementar TEXT DEFAULT NULL,  -- Texto adicional sobre o imóvel
    valor_venda DECIMAL(15, 2) DEFAULT NULL,  -- Valor de venda do imóvel
    cep VARCHAR(10) DEFAULT NULL,
    endereco VARCHAR(150) DEFAULT NULL,
    situacao_imovel ENUM('Vago', 'Ocupado', 'Alugado', 'Ocupado pelo Proprietário', 'Em Construção') DEFAULT NULL,
    complemento VARCHAR(100) DEFAULT NULL,
    bairro VARCHAR(100) DEFAULT NULL,
    cidade VARCHAR(100) DEFAULT NULL,
    uf CHAR(2) DEFAULT NULL,  -- Unidade Federativa, ex: DF, SP
    detalhes_do_imovel JSON DEFAULT NULL,  -- Lista de características do imóvel (JSON)
    detalhes_do_condominio JSON DEFAULT NULL,  -- Lista de características do condomínio (JSON)
    formas_pagamento JSON DEFAULT NULL,  -- Lista de formas de pagamento (JSON)
    nome_completo_prop VARCHAR(150) DEFAULT NULL,
    data_nascimento_prop DATE DEFAULT NULL,
    cpf_prop VARCHAR(14) DEFAULT NULL,  -- CPF do proprietário
    estado_civil_prop VARCHAR(20) DEFAULT NULL,
    foto_cnh_url_prop VARCHAR(255) DEFAULT NULL,
    foto_qrcode_cnh_url_prop VARCHAR(255) DEFAULT NULL,
    pdf_cnh_url_prop VARCHAR(255) DEFAULT NULL,
    rg_prop VARCHAR(50) DEFAULT NULL,  -- Ex: 4040430 SSP DF
    nome_mae_prop VARCHAR(100) DEFAULT NULL,
    nome_pai_prop VARCHAR(100) DEFAULT NULL,
    cnh_prop VARCHAR(20) DEFAULT NULL,
    data_criacao_imovel DATETIME DEFAULT CURRENT_TIMESTAMP,
    matricula_imovel VARCHAR(50) UNIQUE DEFAULT NULL,  -- Matrícula do imóvel
    inscricao_iptu VARCHAR(50) UNIQUE DEFAULT NULL,  -- Inscrição do IPTU
    cartorio_matricula VARCHAR(100) DEFAULT NULL,  -- Cartório da matrícula
    porcentagem_corretagem DECIMAL(5, 2) DEFAULT NULL,  -- Porcentagem de corretagem
    saldo_devedor DECIMAL(15, 2) DEFAULT NULL,  -- Saldo devedor do imóvel
    FOREIGN KEY (usuario_id) REFERENCES usuario(id) ON DELETE CASCADE  -- Associação com a tabela de usuários
);


-- Script do usuario

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

-- script das caracteristicas 

CREATE TABLE `quadr767_imogo_juca`.`caracteristicas_imovel` (
  `id` INT NOT NULL,
  `caracteristicas` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `quadr767_imogo_juca`.`caracteristicas_condominio` (
  `id` INT NOT NULL,
  `caracteristicas` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`));

