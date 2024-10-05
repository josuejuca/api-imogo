# crud.py
from sqlalchemy.orm import Session
import hashlib
import models  # Adicione esta linha
import schemas
from models import Usuario, Imoveis, CaracteristicasImovel, CaracteristicasCondominio
from schemas import (
    UsuarioCreate, 
    UsuarioUpdate, 
    ImovelCreate, 
    ImovelUpdate, 
    CaracteristicasImovelCreate, 
    CaracteristicasImovelUpdate, 
    CaracteristicasCondominioCreate, 
    CaracteristicasCondominioUpdate
)


# Função para gerar hash MD5 de uma senha
def get_md5_hash(senha: str) -> str:
    return hashlib.md5(senha.encode()).hexdigest()

# CRUD para Usuários
# Verifica se o e-mail já existe no banco de dados
def get_usuario_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

# CRUD para Usuários

def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Usuario).offset(skip).limit(limit).all()


def create_usuario(db: Session, usuario: UsuarioCreate):
    # Verifica se o e-mail já existe
    existing_user = get_usuario_by_email(db, usuario.email)
    if existing_user:
        return None, "E-mail já cadastrado."  # Retorna None e uma mensagem de erro
    
    hashed_senha = get_md5_hash(usuario.senha)  # Gera o hash MD5 da senha
    db_usuario = Usuario(
        nome_social=usuario.nome_social,
        telefone=usuario.telefone,
        email=usuario.email,
        senha=get_md5_hash(usuario.senha),
        origem=usuario.origem,
        foto_conta=usuario.foto_conta,
        status=1  # Status inicial
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario, None

def update_usuario(db: Session, usuario_id: int, usuario: UsuarioUpdate):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario is None:
        return None, "Usuário não encontrado."
    
    # Verifica se o e-mail já está sendo usado por outro usuário
    if usuario.email and usuario.email != db_usuario.email:
        existing_user = get_usuario_by_email(db, usuario.email)
        if existing_user:
            return None, "E-mail já em uso por outro usuário."
    
    if usuario.senha:
        usuario.senha = get_md5_hash(usuario.senha)  # Atualiza a senha com o hash MD5
    for key, value in usuario.dict(exclude_unset=True).items():
        setattr(db_usuario, key, value)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario, None

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario is None:
        return None, "Usuário não encontrado."
    db.delete(db_usuario)
    db.commit()
    return db_usuario, None


# CRUD para Imoveis
def get_imovel(db: Session, imovel_id: int):
    return db.query(Imoveis).filter(Imoveis.id == imovel_id).first()


def get_imoveis(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Imoveis).offset(skip).limit(limit).all()


def create_imovel(db: Session, imovel: ImovelCreate):
    # Verifica o usuário que está criando o imóvel
    db_usuario = db.query(Usuario).filter(Usuario.id == imovel.usuario_id).first()

    if not db_usuario:
        return None, "Usuário não encontrado."
    
    # Verifica se o status do usuário é 1 e o atualiza para 2 se for o caso
    if db_usuario.status == 1:
        db_usuario.status = 2
        db.commit()

    # Cria o imóvel normalmente
    db_imovel = Imoveis(**imovel.dict())
    db.add(db_imovel)
    db.commit()
    db.refresh(db_imovel)
    
    return db_imovel


def update_imovel(db: Session, imovel_id: int, imovel: ImovelUpdate):
    db_imovel = db.query(Imoveis).filter(Imoveis.id == imovel_id).first()
    if db_imovel is None:
        return None
    for key, value in imovel.dict(exclude_unset=True).items():
        setattr(db_imovel, key, value)
    db.commit()
    db.refresh(db_imovel)
    return db_imovel


def delete_imovel(db: Session, imovel_id: int):
    db_imovel = db.query(Imoveis).filter(Imoveis.id == imovel_id).first()
    if db_imovel is None:
        return None
    db.delete(db_imovel)
    db.commit()
    return db_imovel


# buscar imovel pelo user 

def get_imoveis_por_usuario(db: Session, usuario_id: int, skip: int = 0, limit: int = 10):
    return db.query(Imoveis).filter(Imoveis.usuario_id == usuario_id).offset(skip).limit(limit).all()

# login

# Verifica o login de um usuário
def authenticate_usuario(db: Session, email: str, senha: str):
    # Verifica se o e-mail existe no banco de dados
    db_usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if not db_usuario:
        return None, "E-mail não encontrado."
    
    # Verifica se a senha está correta
    hashed_senha = get_md5_hash(senha)
    if hashed_senha != db_usuario.senha:
        return None, "Senha incorreta."

    return db_usuario, None


# CRUD para Características de Imóvel
def get_caracteristicas_imovel(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.CaracteristicasImovel).offset(skip).limit(limit).all()

def create_caracteristicas_imovel(db: Session, caracteristicas: schemas.CaracteristicasImovelCreate):
    db_caracteristicas = models.CaracteristicasImovel(**caracteristicas.dict())
    db.add(db_caracteristicas)
    db.commit()
    db.refresh(db_caracteristicas)
    return db_caracteristicas

def update_caracteristicas_imovel(db: Session, id: int, caracteristicas: schemas.CaracteristicasImovelUpdate):
    db_caracteristicas = db.query(models.CaracteristicasImovel).filter(models.CaracteristicasImovel.id == id).first()
    if db_caracteristicas is None:
        return None
    for key, value in caracteristicas.dict(exclude_unset=True).items():
        setattr(db_caracteristicas, key, value)
    db.commit()
    db.refresh(db_caracteristicas)
    return db_caracteristicas

def delete_caracteristicas_imovel(db: Session, id: int):
    db_caracteristicas = db.query(models.CaracteristicasImovel).filter(models.CaracteristicasImovel.id == id).first()
    if db_caracteristicas is None:
        return None
    db.delete(db_caracteristicas)
    db.commit()
    return db_caracteristicas

# CRUD para Características de Condomínio
def get_caracteristicas_condominio(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.CaracteristicasCondominio).offset(skip).limit(limit).all()

def create_caracteristicas_condominio(db: Session, caracteristicas: schemas.CaracteristicasCondominioCreate):
    db_caracteristicas = models.CaracteristicasCondominio(**caracteristicas.dict())
    db.add(db_caracteristicas)
    db.commit()
    db.refresh(db_caracteristicas)
    return db_caracteristicas

def update_caracteristicas_condominio(db: Session, id: int, caracteristicas: schemas.CaracteristicasCondominioUpdate):
    db_caracteristicas = db.query(models.CaracteristicasCondominio).filter(models.CaracteristicasCondominio.id == id).first()
    if db_caracteristicas is None:
        return None
    for key, value in caracteristicas.dict(exclude_unset=True).items():
        setattr(db_caracteristicas, key, value)
    db.commit()
    db.refresh(db_caracteristicas)
    return db_caracteristicas

def delete_caracteristicas_condominio(db: Session, id: int):
    db_caracteristicas = db.query(models.CaracteristicasCondominio).filter(models.CaracteristicasCondominio.id == id).first()
    if db_caracteristicas is None:
        return None
    db.delete(db_caracteristicas)
    db.commit()
    return db_caracteristicas

# CRUD para Características de Condomínio
def get_caracteristicas_condominio(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.CaracteristicasCondominio).offset(skip).limit(limit).all()

def create_caracteristicas_condominio(db: Session, caracteristicas: schemas.CaracteristicasCondominioCreate):
    db_caracteristicas = models.CaracteristicasCondominio(**caracteristicas.dict())
    db.add(db_caracteristicas)
    db.commit()
    db.refresh(db_caracteristicas)
    return db_caracteristicas

def update_caracteristicas_condominio(db: Session, id: int, caracteristicas: schemas.CaracteristicasCondominioUpdate):
    db_caracteristicas = db.query(models.CaracteristicasCondominio).filter(models.CaracteristicasCondominio.id == id).first()
    if db_caracteristicas is None:
        return None
    for key, value in caracteristicas.dict(exclude_unset=True).items():
        setattr(db_caracteristicas, key, value)
    db.commit()
    db.refresh(db_caracteristicas)
    return db_caracteristicas

def delete_caracteristicas_condominio(db: Session, id: int):
    db_caracteristicas = db.query(models.CaracteristicasCondominio).filter(models.CaracteristicasCondominio.id == id).first()
    if db_caracteristicas is None:
        return None
    db.delete(db_caracteristicas)
    db.commit()
    return db_caracteristicas

def get_caracteristica_imovel_by_id(db: Session, id: int):
    return db.query(models.CaracteristicasImovel).filter(models.CaracteristicasImovel.id == id).first()

def get_caracteristica_condominio_by_id(db: Session, id: int):
    return db.query(models.CaracteristicasCondominio).filter(models.CaracteristicasCondominio.id == id).first()

