from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from sqlalchemy import select, update, delete


class RepositorioUsuario():
    def __init__(self, session: Session) -> None:
        self.session = session

    def criar(self, usuario: schemas.Usuario):
        usuario_bd = models.Usuario(nome=usuario.nome,
                                    senha=usuario.senha,
                                    email=usuario.email,
                                    ativo=usuario.ativo,
                                    admin=usuario.admin,
                                    dia_fatura=usuario.dia_fatura)

        self.session.add(usuario_bd)
        self.session.commit()
        self.session.refresh(usuario_bd)
        return usuario_bd

    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        return usuarios

    def obter_por_email(self, email):
        query = select(models.Usuario).where(
            models.Usuario.email == email)
        return self.session.execute(query).scalars().first()

    def obter_por_id(self, id):
        query = select(models.Usuario).where(
            models.Usuario.id == id)
        return self.session.execute(query).scalars().first()

    def editar(self, id: int, usuario: schemas.Usuario):
        update_stmt = update(models.Usuario).where(models.Usuario.id == id).values(nome=usuario.nome,
                                                                              senha=usuario.senha,
                                                                              email=usuario.email,
                                                                              ativo=usuario.ativo,
                                                                              admin=usuario.admin,
                                                                              dia_fatura=usuario.dia_fatura)
        self.session.execute(update_stmt)
        self.session.commit()
        return self.obter_por_id(id)

    def remover(self, id: int):        
        delete_stmt = delete(models.Usuario).where(models.Usuario.id == id)
        self.session.execute(delete_stmt)
        self.session.commit()
        
