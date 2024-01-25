from pydantic import BaseModel
from typing import Optional, List


class ItemDesejo(BaseModel):
    id: Optional[str] = None
    nome: str
    descricao: Optional[str] = None
    prioridade: int
    preco: float
    adquirido: bool
    usuario_id: Optional[int]=None
    class Config:
        orm_mode=True

class Fatura(BaseModel):
    id: Optional[str] = None
    nomeInstituicao: str
    nomeFatura: str
    valor: float
    parcelas: int
    usuario_id: str
    class Config:
        orm_mode=True


class Usuario(BaseModel):
    id:  Optional[str] = None
    nome: str
    email: str
    senha: str
    ativo: Optional[bool] = True
    admin: Optional[bool] = False
    listaDeDesejos: Optional[List[ItemDesejo]] = None
    faturas: Optional[List[Fatura]] = None
    dia_fatura: Optional[int] = None
    class Config:
        orm_mode=True

class LoginData(BaseModel):
    senha: str
    email: str
    class Config:
        orm_mode=True

