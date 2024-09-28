# schemas.py

from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome_social: str
    telefone: str
    email: str
    origem: str
    foto_conta: Optional[str] = None
    nome_completo: Optional[str] = None
    data_nascimento: Optional[datetime] = None
    cpf: Optional[str] = None
    estado_civil: Optional[str] = None
    foto_cnh_url: Optional[str] = None
    foto_qrcode_cnh_url: Optional[str] = None
    pdf_cnh_url: Optional[str] = None
    rg: Optional[str] = None
    nome_mae: Optional[str] = None
    nome_pai: Optional[str] = None
    cnh: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioUpdate(UsuarioBase):
    senha: Optional[str] = None

class Usuario(UsuarioBase):
    id: int
    status: int
    data_criacao: datetime

    class Config:
        from_attributes = True  # Para Pydantic V2
        
# imovel

class ImovelBase(BaseModel):
    usuario_id: int
    status: int
    classificacao: Optional[str] = None
    tipo: Optional[str] = None
    numero_quartos: Optional[int] = None
    numero_suites: Optional[int] = None
    numero_banheiros: Optional[int] = None
    numero_garagem: Optional[int] = None
    orientacao_sol: Optional[str] = None
    area_total: Optional[float] = None
    area_privativa: Optional[float] = None
    descricao_complementar: Optional[str] = None
    valor_venda: Optional[float] = None
    cep: Optional[str] = None
    endereco: Optional[str] = None
    situacao_imovel: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    detalhes_do_imovel: Optional[List[str]] = None
    detalhes_do_condominio: Optional[List[str]] = None
    formas_pagamento: Optional[List[str]] = None


class ImovelCreate(ImovelBase):
    pass


class ImovelUpdate(ImovelBase):
    pass


class Imovel(ImovelBase):
    id: int
    data_criacao_imovel: datetime

    class Config:
        from_attributes = True
        



