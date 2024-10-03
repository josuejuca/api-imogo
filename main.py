# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints CRUD para Usuário
@app.post("/api/v1/usuarios/", response_model=schemas.Usuario, tags=["USUÁRIOS"])
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario, error = crud.create_usuario(db=db, usuario=usuario)
    if error:
        raise HTTPException(status_code=400, detail=error)  # Retorna erro se existir
    return db_usuario


@app.get("/api/v1/usuarios/", response_model=List[schemas.Usuario], tags=["USUÁRIOS"])
def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    usuarios = crud.get_usuarios(db, skip=skip, limit=limit)
    return usuarios


@app.get("/api/v1/usuarios/{usuario_id}", response_model=schemas.Usuario, tags=["USUÁRIOS"])
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_usuario


@app.put("/api/v1/usuarios/{usuario_id}", response_model=schemas.Usuario, tags=["USUÁRIOS"])
def update_usuario(usuario_id: int, usuario: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    db_usuario, error = crud.update_usuario(db, usuario_id=usuario_id, usuario=usuario)
    if error:
        raise HTTPException(status_code=400, detail=error)  # Retorna erro se existir
    return db_usuario


@app.delete("/api/v1/usuarios/{usuario_id}", response_model=schemas.Usuario, tags=["USUÁRIOS"])
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario, error = crud.delete_usuario(db, usuario_id=usuario_id)
    if error:
        raise HTTPException(status_code=404, detail=error)  # Retorna erro se existir
    return db_usuario


# Endpoints CRUD para Imóveis
@app.post("/api/v1/imoveis/", response_model=schemas.Imovel, tags=["IMÓVEIS"])
def create_imovel(imovel: schemas.ImovelCreate, db: Session = Depends(get_db)):
    return crud.create_imovel(db=db, imovel=imovel)


@app.get("/api/v1/imoveis/", response_model=List[schemas.Imovel], tags=["IMÓVEIS"])
def read_imoveis(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    imoveis = crud.get_imoveis(db, skip=skip, limit=limit)
    return imoveis


@app.get("/api/v1/imoveis/{imovel_id}", response_model=schemas.Imovel, tags=["IMÓVEIS"])
def read_imovel(imovel_id: int, db: Session = Depends(get_db)):
    db_imovel = crud.get_imovel(db, imovel_id=imovel_id)
    if db_imovel is None:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")
    return db_imovel


@app.put("/api/v1/imoveis/{imovel_id}", response_model=schemas.Imovel, tags=["IMÓVEIS"])
def update_imovel(imovel_id: int, imovel: schemas.ImovelUpdate, db: Session = Depends(get_db)):
    db_imovel = crud.update_imovel(db, imovel_id=imovel_id, imovel=imovel)
    if db_imovel is None:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")
    return db_imovel


@app.delete("/api/v1/imoveis/{imovel_id}", response_model=schemas.Imovel, tags=["IMÓVEIS"])
def delete_imovel(imovel_id: int, db: Session = Depends(get_db)):
    db_imovel = crud.delete_imovel(db, imovel_id=imovel_id)
    if db_imovel is None:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")
    return db_imovel


# buscar imovel pelo user 

@app.get("/api/v1/usuarios/{usuario_id}/imoveis", response_model=List[schemas.Imovel], tags=["USUÁRIOS"])
def read_imoveis_por_usuario(usuario_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    imoveis = crud.get_imoveis_por_usuario(db, usuario_id=usuario_id, skip=skip, limit=limit)
    return imoveis


# Login

# Rota de login
@app.post("/login")
def login(usuario: schemas.LoginSchema, db: Session = Depends(get_db)):
    db_usuario, error = crud.authenticate_usuario(db, usuario.email, usuario.senha)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return {"message": "Login bem-sucedido", "usuario_id": db_usuario.id}


# rota de criação de imoveis 

@app.post("/imoveis/caracteristicas", response_model=schemas.Imovel)
def create_imovel_caracteristicas(imovel_data: schemas.ImovelCaracteristicasUpdate, db: Session = Depends(get_db)):
    imovel_create = schemas.ImovelCreate(**imovel_data.dict())  # Converte o dado de características para criação
    created_imovel = crud.create_imovel(db=db, imovel=imovel_create)
    return created_imovel

@app.put("/imoveis/{imovel_id}/endereco", response_model=schemas.Imovel)
def update_endereco_imovel(imovel_id: int, imovel_data: schemas.ImovelEnderecoUpdate, db: Session = Depends(get_db)):
    db_imovel = crud.get_imovel(db, imovel_id=imovel_id)
    if db_imovel is None:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")
    
    updated_imovel = crud.update_imovel(db, imovel_id=imovel_id, imovel=imovel_data)
    return updated_imovel

@app.put("/imoveis/{imovel_id}/proprietario", response_model=schemas.Imovel)
def update_proprietario_imovel(imovel_id: int, imovel_data: schemas.ImovelProprietarioUpdate, db: Session = Depends(get_db)):
    db_imovel = crud.get_imovel(db, imovel_id=imovel_id)
    if db_imovel is None:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")
    
    updated_imovel = crud.update_imovel(db, imovel_id=imovel_id, imovel=imovel_data)
    return updated_imovel
