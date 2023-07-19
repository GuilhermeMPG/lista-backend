from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from infra.sqlalchemy.config.database import get_db
from routers.auth_utils import obter_usuario_logado
from schemas.response_schemas import LoginSucesso
from schemas.schemas import LoginData, Usuario
from infra.providers import token_provaider, hash_provaider

from infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario


router = APIRouter()