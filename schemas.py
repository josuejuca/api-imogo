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
    valorCondominio: Optional[float] = None
    cep: Optional[str] = None
    endereco: Optional[str] = None
    situacao: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    detalhes_do_imovel: Optional[List[str]] = None
    detalhes_do_condominio: Optional[List[str]] = None
    formas_pagamento: Optional[List[str]] = None
    foto_app_capa: Optional[str] = "https://cdn.imogo.com.br/img/banner_imovel.png"
    tipo_documento: Optional[str] = None
    nome_completo_prop: Optional[str] = None
    data_nascimento_prop: Optional[datetime] = None
    cpf_prop: Optional[str] = None
    estado_civil_prop: Optional[str] = None
    foto_cnh_url_prop: Optional[str] = None
    foto_qrcode_cnh_url_prop: Optional[str] = None
    pdf_cnh_url_prop: Optional[str] = None
    rg_prop: Optional[str] = None
    nome_mae_prop: Optional[str] = None
    nome_pai_prop: Optional[str] = None
    cnh_prop: Optional[str] = None
    matricula_imovel: Optional[str] = None
    inscricao_iptu: Optional[str] = None
    cartorio_matricula: Optional[str] = None
    porcentagem_corretagem: Optional[float] = None
    saldo_devedor: Optional[float] = None
    usuario_proprietario: Optional[bool] = False   
    foto_pessoal: Optional[str] = None
    rg_frente: Optional[str] = None
    rg_costa: Optional[str] = None 
    

class ImovelCreate(ImovelBase):
    pass


class ImovelUpdate(ImovelBase):
    pass


class Imovel(ImovelBase):
    id: int
    data_criacao_imovel: datetime

    class Config:
        from_attributes = True
        
class LoginSchema(BaseModel):
    email: str
    senha: str


# Criação dos imoveis 
# Parte 1
class ImovelCaracteristicasUpdate(BaseModel):
    classificacao: Optional[str] = None
    tipo: Optional[str] = None
    usuario_id: int
    status: int
   
    numero_quartos: Optional[int] = None
    numero_suites: Optional[int] = None
    numero_banheiros: Optional[int] = None
    numero_garagem: Optional[int] = None
    orientacao_sol: Optional[str] = None
    area_privativa: Optional[float] = None
    area_total: Optional[float] = None
    detalhes_do_imovel: Optional[List[str]] = None
    detalhes_do_condominio: Optional[List[str]] = None
    descricao_complementar: Optional[str] = None
    situacao_imovel: Optional[str] = None
    formas_pagamento: Optional[List[str]] = None
    valor_venda: Optional[float] = None

# parte 2  

class ImovelEnderecoUpdate(BaseModel):
    cep: Optional[str] = None
    endereco: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    status: Optional[int] = 3
# parte 3 

class ImovelProprietarioUpdate(BaseModel):
    nome_completo_prop: Optional[str] = None
    cpf_prop: Optional[str] = None
    estado_civil_prop: Optional[str] = None
    status: Optional[int] = 4
    tipo_documento: Optional[str] = None
    usuario_proprietario: Optional[bool] = None
    
    
    
    
# Esquemas para Características de Imóvel
class CaracteristicasImovelBase(BaseModel):
    caracteristicas: str

class CaracteristicasImovelCreate(CaracteristicasImovelBase):
    pass

class CaracteristicasImovelUpdate(CaracteristicasImovelBase):
    pass

class CaracteristicasImovel(CaracteristicasImovelBase):
    id: int

    class Config:
        from_attributes = True


# Esquemas para Características de Condomínio
class CaracteristicasCondominioBase(BaseModel):
    caracteristicas: str

class CaracteristicasCondominioCreate(CaracteristicasCondominioBase):
    pass

class CaracteristicasCondominioUpdate(CaracteristicasCondominioBase):
    pass

class CaracteristicasCondominio(CaracteristicasCondominioBase):
    id: int

    class Config:
        from_attributes = True
