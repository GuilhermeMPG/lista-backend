from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.routers.auth_utils import obter_usuario_logado

from src.schemas.schemas import LoginData, Usuario
from src.infra.providers import token_provaider, hash_provaider

from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario


router = APIRouter()


@router.post('/usuarios', status_code=status.HTTP_201_CREATED)
def criar_usuarios(usuario: Usuario, session: Session = Depends(get_db)):
    # verifiar se o usuario ja existe para o telefone
    usuario_localizado = RepositorioUsuario(
        session).obter_por_email(usuario.email)
    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Já existe um usuário para este email!")
# criar usiario novo
    usuario.senha = hash_provaider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return {'detail': 'Usuário criado com sucesso!', 'usuario': usuario_criado}


@router.get('/usuarios', status_code=status.HTTP_200_OK, response_model=List[Usuario])
def listar_usuarios(session: Session = Depends(get_db)):
    listaDeUsuarios = RepositorioUsuario(session).listar()
    if not listaDeUsuarios:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Não existe usuarios cadastrados!")
    return listaDeUsuarios


@router.post('/token')
def login(login_data: LoginData, session: Session = Depends(get_db)):
    senha = login_data.senha
    email = login_data.email
    usuario = RepositorioUsuario(session).obter_por_email(email)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Email ou senha estão incorretas!')
    senha_valida = hash_provaider.verificar_hash(senha, usuario.senha)
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Email ou senha estão incorretas!')

# Gerar Token JWT
    token = token_provaider.criar_acess_token({'sub': usuario.email})
    return {'usuario':usuario,'access_token': token, 'token_type': 'bearer'}


@router.patch('/usuarios/{id}', status_code=status.HTTP_200_OK)
def atualizar_usuario(id: int, usuario:Usuario, session: Session = Depends(get_db)):

    usuario_bd: Usuario= RepositorioUsuario(session).obter_por_id(id)

    if not usuario_bd:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Usuário não encontrado!')
    
    usuario_bd.nome = usuario.nome if usuario.nome  else usuario_bd.nome
    usuario_bd.email = usuario.email if usuario.email else usuario_bd.email
    usuario_bd.senha = hash_provaider.gerar_hash(usuario.senha) if usuario.senha else usuario_bd.senha
    usuario_bd.ativo = usuario.ativo if usuario.ativo else usuario_bd.ativo
    usuario_bd.admin = usuario.admin   if usuario.admin else usuario_bd.admin
    usuario_bd.dia_fatura = usuario.dia_fatura if usuario.dia_fatura else usuario_bd.dia_fatura
    
    usuario_bd=RepositorioUsuario(session).editar(id,usuario_bd)        
    
    return {'message': 'Usuário atualizado com sucesso!','usuario_atualizado': usuario_bd}  


@router.delete('/usuarios/{id}', status_code=status.HTTP_200_OK)
def remover_usuario(id: int, session: Session = Depends(get_db)):
    usuario_bd:Usuario = RepositorioUsuario(session).obter_por_id(id)
    if not usuario_bd:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Usuário não encontrado!')
    RepositorioUsuario(session).remover(id)
    return {'message': 'Usuário removido com sucesso!','usuario_removido': usuario_bd }


@router.get('/me')
def me(ususario: Usuario = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
        return {'usuario': ususario}

@router.get("/")
def read_root():
    return {"Hello": "World"}