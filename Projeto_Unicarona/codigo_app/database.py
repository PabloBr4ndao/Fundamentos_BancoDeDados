
# Este arquivo faz a conexão com o PostgreSQL usando as credenciais do administrador.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# String de conexão usando o usuário admin que vocês criaram
SQLALCHEMY_DATABASE_URL = "postgresql://unicarona_admin:admin_unicarona_2026@localhost:5432/unicarona"

# Para testar o bloqueio de acesso depois, comente a linha acima e descomente a linha abaixo:
# SQLALCHEMY_DATABASE_URL = "postgresql://unicarona_leitura:leitura_unicarona_2026@localhost:5432/unicarona"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()