from sqlalchemy.orm import Session
import models, schemas

# 1. READ ALL (Buscar todas as caronas)
def get_caronas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Carona).offset(skip).limit(limit).all()

# 1.1 READ ONE (Buscar carona específica por ID)
def get_carona(db: Session, carona_id: int):
    return db.query(models.Carona).filter(models.Carona.id_carona == carona_id).first()

# 2. CREATE (Inserir carona)
def create_carona(db: Session, carona: schemas.CaronaCreate):
    # Converte os dados do Pydantic para o modelo do SQLAlchemy
    db_carona = models.Carona(**carona.model_dump())
    db.add(db_carona)
    db.commit()
    db.refresh(db_carona)
    return db_carona

# 3. UPDATE (Atualizar a quantidade de vagas)
def update_vagas(db: Session, carona_id: int, novas_vagas: int):
    db_carona = get_carona(db, carona_id)
    if db_carona:
        db_carona.vagas_disponiveis = novas_vagas
        db.commit()
        db.refresh(db_carona)
    return db_carona

# 4. DELETE (Deletar a carona)
def delete_carona(db: Session, carona_id: int):
    db_carona = get_carona(db, carona_id)
    if db_carona:
        db.delete(db_carona)
        db.commit()
    return db_carona