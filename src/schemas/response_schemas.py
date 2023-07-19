from schemas.schemas import Usuario
from pydantic import BaseModel



class LoginSucesso(BaseModel):
    usuario: Usuario
    access_token: str
