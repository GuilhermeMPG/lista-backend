import sys
import os

# Obtém o caminho absoluto do diretório pai do diretório atual (onde está este script)
caminho_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona o caminho do projeto ao sys.path
sys.path.append(caminho_projeto)

from fastapi.security import  OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provaider
from jose import JWTError
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario

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