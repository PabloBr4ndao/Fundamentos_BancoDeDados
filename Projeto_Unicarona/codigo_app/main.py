from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, get_db

# Isso garante que o SQLAlchemy se conecte e valide as tabelas
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API UniCarona - CRUD de Caronas")

# Rota para INSERIR (POST)
@app.post("/caronas/", response_model=schemas.CaronaResponse)
def criar_carona(carona: schemas.CaronaCreate, db: Session = Depends(get_db)):
    # Verifica se a carona já existe
    db_carona = crud.get_carona(db, carona_id=carona.id_carona)
    if db_carona:
        raise HTTPException(status_code=400, detail="ID de carona já cadastrado!")
    return crud.create_carona(db=db, carona=carona)

# Rota para LISTAR TODAS (GET)
@app.get("/caronas/", response_model=list[schemas.CaronaResponse])
def listar_caronas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_caronas(db, skip=skip, limit=limit)

# Rota para BUSCAR UMA SÓ (GET)
@app.get("/caronas/{carona_id}", response_model=schemas.CaronaResponse)
def buscar_carona(carona_id: int, db: Session = Depends(get_db)):
    db_carona = crud.get_carona(db, carona_id=carona_id)
    if db_carona is None:
        raise HTTPException(status_code=404, detail="Carona não encontrada")
    return db_carona

# Rota para ATUALIZAR (PUT)
@app.put("/caronas/{carona_id}", response_model=schemas.CaronaResponse)
def atualizar_carona(carona_id: int, vagas: schemas.CaronaUpdate, db: Session = Depends(get_db)):
    db_carona = crud.update_vagas(db, carona_id=carona_id, novas_vagas=vagas.vagas_disponiveis)
    if db_carona is None:
        raise HTTPException(status_code=404, detail="Carona não encontrada")
    return db_carona

# Rota para DELETAR (DELETE)
@app.delete("/caronas/{carona_id}")
def deletar_carona(carona_id: int, db: Session = Depends(get_db)):
    db_carona = crud.delete_carona(db, carona_id=carona_id)
    if db_carona is None:
        raise HTTPException(status_code=404, detail="Carona não encontrada")
    return {"mensagem": "Carona cancelada/deletada com sucesso"}