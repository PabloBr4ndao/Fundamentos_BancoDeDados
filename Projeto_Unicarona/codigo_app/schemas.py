from pydantic import BaseModel
from datetime import date, time

class CaronaBase(BaseModel):
    cpf_motorista: str
    placa_veiculo: str
    id_origem: int
    id_destino: int
    data: date
    horario: time
    vagas_disponiveis: int

# Esquema para quando o usuário for INSERIR uma carona (precisa passar o ID)
class CaronaCreate(CaronaBase):
    id_carona: int

# Esquema para quando formos ATUALIZAR as vagas
class CaronaUpdate(BaseModel):
    vagas_disponiveis: int

# Esquema de RESPOSTA (o que a API devolve para o usuário)
class CaronaResponse(CaronaBase):
    id_carona: int

    class Config:
        from_attributes = True