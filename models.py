# models.py

from sqlalchemy import Column, Integer, String, Text, DECIMAL, Enum, JSON, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Integer, nullable=False)
    nome_social = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(32), nullable=False)
    origem = Column(String(50), nullable=False)
    data_criacao = Column(DateTime, default=func.now())
    foto_conta = Column(String(255), nullable=True)
    nome_completo = Column(String(150), nullable=True)
    data_nascimento = Column(DateTime, nullable=True)
    cpf = Column(String(14), nullable=True)
    estado_civil = Column(String(20), nullable=True)
    foto_cnh_url = Column(String(255), nullable=True)
    foto_qrcode_cnh_url = Column(String(255), nullable=True)
    pdf_cnh_url = Column(String(255), nullable=True)
    rg = Column(String(50), nullable=True)
    nome_mae = Column(String(100), nullable=True)
    nome_pai = Column(String(100), nullable=True)
    cnh = Column(String(20), nullable=True)
    tipo_documento = Column(String(255), nullable=True)
    foto_pessoal = Column(String(255), nullable=True)
    rg_frente = Column(String(255), nullable=True)
    rg_costa = Column(String(255), nullable=True)
    id_google = Column(Integer, nullable=True)

    imoveis = relationship("Imoveis", back_populates="usuario")  # Nome correto da tabela

class Imoveis(Base):
    __tablename__ = "Imoveis"  # Nome correto da tabela

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    status = Column(Integer, nullable=False)
    classificacao = Column(Enum("Comercial", "Residencial", "Outro"), nullable=True)
    tipo = Column(String(50), nullable=True)
    numero_quartos = Column(Integer, nullable=True)
    numero_suites = Column(Integer, nullable=True)
    numero_banheiros = Column(Integer, nullable=True)
    numero_garagem = Column(Integer, nullable=True)
    orientacao_sol = Column(Enum("Poente", "Nascente", "Perpendicular"), nullable=True) # '','',''
    area_total = Column(DECIMAL(10, 2), nullable=True)
    area_privativa = Column(DECIMAL(10, 2), nullable=True)
    descricao_complementar = Column(Text, nullable=True)
    valor_venda = Column(DECIMAL(15, 2), nullable=True)
    cep = Column(String(10), nullable=True)
    endereco = Column(String(150), nullable=True)
    situacao = Column(String(100), nullable=True)
    complemento = Column(String(100), nullable=True)
    bairro = Column(String(100), nullable=True)
    cidade = Column(String(100), nullable=True)
    uf = Column(String(2), nullable=True)
    detalhes_do_imovel = Column(JSON, nullable=True)
    detalhes_do_condominio = Column(JSON, nullable=True)
    formas_pagamento = Column(JSON, nullable=True)
    nome_completo_prop = Column(String(150), nullable=True)
    data_nascimento_prop = Column(DateTime, nullable=True)
    cpf_prop = Column(String(14), nullable=True)
    estado_civil_prop = Column(String(20), nullable=True)
    foto_cnh_url_prop = Column(String(255), nullable=True)
    foto_qrcode_cnh_url_prop = Column(String(255), nullable=True)
    pdf_cnh_url_prop = Column(String(255), nullable=True)
    rg_prop = Column(String(50), nullable=True)
    nome_mae_prop = Column(String(100), nullable=True)
    nome_pai_prop = Column(String(100), nullable=True)
    cnh_prop = Column(String(20), nullable=True)
    data_criacao_imovel = Column(DateTime, default=func.now())
    matricula_imovel = Column(String(50), nullable=True, unique=True)
    inscricao_iptu = Column(String(50), nullable=True, unique=True)
    cartorio_matricula = Column(String(100), nullable=True)
    porcentagem_corretagem = Column(DECIMAL(5, 2), nullable=True)
    saldo_devedor = Column(DECIMAL(15, 2), nullable=True)
    # Nova coluna foto_app_capa com valor padrão
    foto_app_capa = Column(String(255), nullable=False, default="https://cdn.imogo.com.br/img/banner_imovel.png")
    tipo_documento = Column(String(50), nullable=True)
    usuario_proprietario = Column(Boolean, default=False)
    foto_pessoal = Column(String(255), nullable=True)
    rg_frente = Column(String(255), nullable=True)
    rg_costa = Column(String(255), nullable=True)   
    valorCondominio = Column(DECIMAL(15, 2), nullable=True)
    usuario = relationship("Usuario", back_populates="imoveis")

# ALTER TABLE `Imoveis` ADD `foto_app_capa` VARCHAR(100) NOT NULL DEFAULT 'https://cdn.imogo.com.br/img/banner_imovel.png' AFTER `saldo_devedor`;


class CaracteristicasImovel(Base):
    __tablename__ = "caracteristicas_imovel"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    caracteristicas = Column(String(100), nullable=False)

class CaracteristicasCondominio(Base):
    __tablename__ = "caracteristicas_condominio"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    caracteristicas = Column(String(100), nullable=False)

    