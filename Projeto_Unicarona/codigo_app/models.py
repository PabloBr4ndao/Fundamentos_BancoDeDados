
# Este arquivo espelha a tabela CARONA que já existe no seu banco de dados. O SQLAlchemy vai usar isso para saber onde salvar as coisas.

from sqlalchemy import Column, Integer, String, Date, Time
from database import Base

class Carona(Base):
    __tablename__ = "carona" # O nome da tabela no PostgreSQL

    id_carona = Column(Integer, primary_key=True, index=True)
    cpf_motorista = Column(String(11), nullable=False)
    placa_veiculo = Column(String(7), nullable=False)
    id_origem = Column(Integer, nullable=False)
    id_destino = Column(Integer, nullable=False)
    data = Column(Date, nullable=False) 
    horario = Column(Time, nullable=False)
    vagas_disponiveis = Column(Integer, nullable=False)