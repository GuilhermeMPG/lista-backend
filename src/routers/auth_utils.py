from fastapi.security import  OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_db
from infra.providers import token_provaider
from jose import JWTError
from infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def obter_usuario_logado(token: str = Depends(oauth2_schema), session: Session = Depends(get_db) ):
    exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail='Token Inválido')
    try:
        email = token_provaider.verificar_acess_token(token)
    except JWTError:
        raise exception
    if not email:
        raise exception
    usuario = RepositorioUsuario(session).obter_por_email(email)
    if not usuario:
        raise exception
    return usuario