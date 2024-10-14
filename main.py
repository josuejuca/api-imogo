# main.py

from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, models, schemas
from database import SessionLocal, engine

# Uploads 
from fastapi.responses import FileResponse
from models import Imoveis  # Certifique-se de importar o modelo 
import os
import uuid  # Para gerar nomes aleatórios

models.Base.metadata.create_all(bind=engine)
UPLOAD_DIRECTORY = "uploads"
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
@app.post("/api/v1/imoveis/", response_model=schemas.Imovel, tags=["IMÓVEIS - ETAPA 1"])
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

@app.post("/api/v1/imoveis/caracteristicas", response_model=schemas.Imovel)
def create_imovel_caracteristicas(imovel_data: schemas.ImovelCaracteristicasUpdate, db: Session = Depends(get_db)):
    imovel_create = schemas.ImovelCreate(**imovel_data.dict())  # Converte o dado de características para criação
    created_imovel = crud.create_imovel(db=db, imovel=imovel_create)
    
    if created_imovel is None:
        raise HTTPException(status_code=400, detail="Erro ao criar imóvel.")
    
    return created_imovel

@app.put("/api/v1/imoveis/{imovel_id}/endereco", response_model=schemas.Imovel, tags=["IMÓVEIS - ETAPA 2"])
def update_endereco_imovel(imovel_id: int, imovel_data: schemas.ImovelEnderecoUpdate, db: Session = Depends(get_db)):
    db_imovel = crud.get_imovel(db, imovel_id=imovel_id)
    if db_imovel is None:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")
    
    updated_imovel = crud.update_imovel(db, imovel_id=imovel_id, imovel=imovel_data)
    return updated_imovel

@app.put("/api/v1/imoveis/{imovel_id}/proprietario", response_model=schemas.Imovel, tags=["IMÓVEIS - ETAPA 3"])
def update_proprietario_imovel(imovel_id: int, imovel_data: schemas.ImovelProprietarioUpdate, db: Session = Depends(get_db)):
    db_imovel = crud.get_imovel(db, imovel_id=imovel_id)
    if db_imovel is None:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")
    
    updated_imovel = crud.update_imovel(db, imovel_id=imovel_id, imovel=imovel_data)
    return updated_imovel


# endpoitn caracteristicas imob

@app.get("/api/v1/caracteristicas_imovel/", response_model=List[schemas.CaracteristicasImovel], tags=["caracteristicas"])
def read_caracteristicas_imovel(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_caracteristicas_imovel(db, skip=skip, limit=limit)

@app.post("/api/v1/caracteristicas_imovel/", response_model=schemas.CaracteristicasImovel, tags=["caracteristicas"])
def create_caracteristicas_imovel(caracteristicas: schemas.CaracteristicasImovelCreate, db: Session = Depends(get_db)):
    return crud.create_caracteristicas_imovel(db=db, caracteristicas=caracteristicas)

@app.put("/api/v1/caracteristicas_imovel/{id}", response_model=schemas.CaracteristicasImovel, tags=["caracteristicas"])
def update_caracteristicas_imovel(id: int, caracteristicas: schemas.CaracteristicasImovelUpdate, db: Session = Depends(get_db)):
    updated_caracteristicas = crud.update_caracteristicas_imovel(db=db, id=id, caracteristicas=caracteristicas)
    if updated_caracteristicas is None:
        raise HTTPException(status_code=404, detail="Características do imóvel não encontradas")
    return updated_caracteristicas

@app.delete("/api/v1/caracteristicas_imovel/{id}", response_model=schemas.CaracteristicasImovel, tags=["caracteristicas"])
def delete_caracteristicas_imovel(id: int, db: Session = Depends(get_db)):
    deleted_caracteristicas = crud.delete_caracteristicas_imovel(db=db, id=id)
    if deleted_caracteristicas is None:
        raise HTTPException(status_code=404, detail="Características do imóvel não encontradas")
    return deleted_caracteristicas

# endpoitn caracteristicas condominio

@app.get("/api/v1/caracteristicas_condominio/", response_model=List[schemas.CaracteristicasCondominio], tags=["caracteristicas"])
def read_caracteristicas_condominio(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_caracteristicas_condominio(db, skip=skip, limit=limit)

@app.post("/api/v1/caracteristicas_condominio/", response_model=schemas.CaracteristicasCondominio, tags=["caracteristicas"])
def create_caracteristicas_condominio(caracteristicas: schemas.CaracteristicasCondominioCreate, db: Session = Depends(get_db)):
    return crud.create_caracteristicas_condominio(db=db, caracteristicas=caracteristicas)

@app.put("/api/v1/caracteristicas_condominio/{id}", response_model=schemas.CaracteristicasCondominio, tags=["caracteristicas"])
def update_caracteristicas_condominio(id: int, caracteristicas: schemas.CaracteristicasCondominioUpdate, db: Session = Depends(get_db)):
    updated_caracteristicas = crud.update_caracteristicas_condominio(db=db, id=id, caracteristicas=caracteristicas)
    if updated_caracteristicas is None:
        raise HTTPException(status_code=404, detail="Características do condomínio não encontradas")
    return updated_caracteristicas

@app.delete("/api/v1/caracteristicas_condominio/{id}", response_model=schemas.CaracteristicasCondominio, tags=["caracteristicas"])
def delete_caracteristicas_condominio(id: int, db: Session = Depends(get_db)):
    deleted_caracteristicas = crud.delete_caracteristicas_condominio(db=db, id=id)
    if deleted_caracteristicas is None:
        raise HTTPException(status_code=404, detail="Características do condomínio não encontradas")
    return deleted_caracteristicas


@app.get("/api/v1/caracteristicas_imovel/{id}", response_model=schemas.CaracteristicasImovel, tags=["caracteristicas"])
def read_caracteristica_imovel(id: int, db: Session = Depends(get_db)):
    db_caracteristica = crud.get_caracteristica_imovel_by_id(db, id=id)
    if db_caracteristica is None:
        raise HTTPException(status_code=404, detail="Características do imóvel não encontradas")
    return db_caracteristica


# uploads de arquivos
# Função para salvar o arquivo no diretório
def save_file(file: UploadFile, file_type: str):
    # Gera um nome de arquivo aleatório com extensão baseada no nome original
    file_extension = file.filename.split(".")[-1]
    random_name = f"{file_type}_{uuid.uuid4().hex}.{file_extension}"

    # Define o caminho onde o arquivo será salvo
    file_location = f"uploads/{random_name}"

    # Cria o diretório se não existir
    os.makedirs(os.path.dirname(file_location), exist_ok=True)

    # Salva o arquivo
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    return file_location

# Rota para upload dos arquivos de CNH e QR Code
@app.post("/api/v1/imoveis/{imovel_id}/upload_cnh/", tags=["IMÓVEIS - ETAPA 4"])
async def upload_cnh_files(imovel_id: int, cnh_file: UploadFile = File(...), qr_cnh_file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Verificar se o imóvel existe
    db_imovel = db.query(models.Imoveis).filter(models.Imoveis.id == imovel_id).first()
    
    if not db_imovel:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado.")
    
    # Gerar nomes aleatórios para os arquivos
    cnh_filename = f"cnh_{uuid.uuid4().hex}{os.path.splitext(cnh_file.filename)[1]}"
    qr_cnh_filename = f"qr_cnh_{uuid.uuid4().hex}{os.path.splitext(qr_cnh_file.filename)[1]}"
    
    # Salvar arquivos no diretório (ou serviço de armazenamento)
    cnh_path = f"uploads/{cnh_filename}"
    qr_cnh_path = f"uploads/{qr_cnh_filename}"
    
    # Aqui você pode implementar a lógica para salvar os arquivos no sistema de arquivos ou serviço de armazenamento
    with open(cnh_path, "wb") as buffer:
        buffer.write(await cnh_file.read())
    
    with open(qr_cnh_path, "wb") as buffer:
        buffer.write(await qr_cnh_file.read())
    
    # Atualizar os campos de foto do imóvel no banco de dados
    db_imovel.foto_cnh_url_prop = cnh_path
    db_imovel.foto_qrcode_cnh_url_prop = qr_cnh_path
    
    # Atualizar o status do imóvel para 5
    db_imovel.status = 5
    
    db.commit()
    db.refresh(db_imovel)

    # Retornar os dados do imóvel atualizados
    return db_imovel

# Rota para upload dos arquivos de CNH
@app.post("/api/v1/imoveis/{imovel_id}/upload_pdf_cnh/", tags=["IMÓVEIS - ETAPA 4"])
async def upload_pdf_cnh(imovel_id: int, pdf_cnh_file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Verificar se o imóvel existe
    db_imovel = db.query(models.Imoveis).filter(models.Imoveis.id == imovel_id).first()
    
    if not db_imovel:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado.")
    
    # Gerar nome aleatório para o arquivo PDF
    pdf_cnh_filename = f"pdf_cnh_{uuid.uuid4().hex}{os.path.splitext(pdf_cnh_file.filename)[1]}"
    
    # Salvar o arquivo no diretório (ou serviço de armazenamento)
    pdf_cnh_path = f"uploads/{pdf_cnh_filename}"
    
    # Aqui você pode implementar a lógica para salvar o arquivo no sistema de arquivos ou serviço de armazenamento
    with open(pdf_cnh_path, "wb") as buffer:
        buffer.write(await pdf_cnh_file.read())
    
    # Atualizar o campo de PDF da CNH no banco de dados
    db_imovel.pdf_cnh_url_prop = pdf_cnh_path
    
    # Atualizar o status do imóvel para 5
    db_imovel.status = 5
    
    db.commit()
    db.refresh(db_imovel)

    # Retornar os dados do imóvel atualizados
    return db_imovel

# rota que recebe o RG 

@app.post("/api/v1/imoveis/{imovel_id}/upload_rg/", tags=["IMÓVEIS - ETAPA 4"])
async def upload_rg_files(imovel_id: int, rg_frente_file: UploadFile = File(...), rg_costa_file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Verificar se o imóvel existe
    db_imovel = db.query(models.Imoveis).filter(models.Imoveis.id == imovel_id).first()
    
    if not db_imovel:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado.")
    
    # Gerar nomes aleatórios para os arquivos
    rg_frente_filename = f"rg_frente_{uuid.uuid4().hex}{os.path.splitext(rg_frente_file.filename)[1]}"
    rg_costa_filename = f"rg_costa_{uuid.uuid4().hex}{os.path.splitext(rg_costa_file.filename)[1]}"
    
    # Salvar arquivos no diretório (ou serviço de armazenamento)
    rg_frente_path = f"uploads/{rg_frente_filename}"
    rg_costa_path = f"uploads/{rg_costa_filename}"
    
    # Aqui você pode implementar a lógica para salvar os arquivos no sistema de arquivos ou serviço de armazenamento
    with open(rg_frente_path, "wb") as buffer:
        buffer.write(await rg_frente_file.read())
    
    with open(rg_costa_path, "wb") as buffer:
        buffer.write(await rg_costa_file.read())
    
    # Atualizar os campos de foto do imóvel no banco de dados
    db_imovel.rg_frente = rg_frente_path
    db_imovel.rg_costa = rg_costa_path
    
    # Atualizar o status do imóvel para 5
    db_imovel.status = 5
    
    db.commit()
    db.refresh(db_imovel)

    # Retornar os dados do imóvel atualizados
    return db_imovel

# Rota que recebe a foto pessoal   

@app.post("/api/v1/imoveis/{imovel_id}/upload_foto_pessoal/", tags=["IMÓVEIS - ETAPA 5"])
async def upload_foto_pessoal(imovel_id: int, foto_pessoal_file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Verificar se o imóvel existe
    db_imovel = db.query(models.Imoveis).filter(models.Imoveis.id == imovel_id).first()
    
    if not db_imovel:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado.")
    
    # Gerar nome aleatório para o arquivo
    foto_pessoal_filename = f"foto_pessoal_{uuid.uuid4().hex}{os.path.splitext(foto_pessoal_file.filename)[1]}"
    
    # Salvar arquivo no diretório (ou serviço de armazenamento)
    foto_pessoal_path = f"uploads/{foto_pessoal_filename}"
    
    # Aqui você pode implementar a lógica para salvar o arquivo no sistema de arquivos ou serviço de armazenamento
    with open(foto_pessoal_path, "wb") as buffer:
        buffer.write(await foto_pessoal_file.read())

    # Atualizar o campo de foto pessoal no banco de dados
    db_imovel.foto_pessoal = foto_pessoal_path
    
    # Atualizar o status do imóvel para 10
    db_imovel.status = 10
    
    db.commit()
    db.refresh(db_imovel)

    # Retornar os dados do imóvel atualizados
    return db_imovel
 


# uploads 

@app.get("/files", tags=["files"])
async def list_uploads():
    """
    Lista todos os arquivos no diretório de uploads.
    """
    try:
        # Verifica se o diretório de uploads existe
        if not os.path.exists(UPLOAD_DIRECTORY):
            raise HTTPException(status_code=404, detail="Diretório de uploads não encontrado.")
        
        # Lista todos os arquivos no diretório
        files = os.listdir(UPLOAD_DIRECTORY)
        if not files:
            return {"message": "Nenhum arquivo encontrado no diretório de uploads."}
        
        return {"files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar os arquivos: {str(e)}")
    
@app.get("/files/{file_name}", tags=["files"])
async def get_upload(file_name: str):
    """
    Retorna um arquivo específico do diretório de uploads.
    """
    file_path = os.path.join(UPLOAD_DIRECTORY, file_name)

    # Verifica se o arquivo existe
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Arquivo não encontrado.")
    
    # Retorna o arquivo
    return FileResponse(file_path)