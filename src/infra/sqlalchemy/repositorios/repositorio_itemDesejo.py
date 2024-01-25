from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.models import models
from sqlalchemy import select, update, delete


class RepositorioItemDesejo():
    def __init__(self, session: Session) -> None:
        self.session = session

    def criar(self, itemDesejo: schemas.ItemDesejo):
        db_itemDesejo = models.ItemDesejo(nome=itemDesejo.nome,
                                          descricao=itemDesejo.descricao,
                                          prioridade=itemDesejo.prioridade,
                                          preco=itemDesejo.preco,
                                          adquirido=itemDesejo.adquirido,
                                          usuario_id=itemDesejo.usuario_id
                                          )

        self.session.add(db_itemDesejo)
        self.session.commit()
        self.session.refresh(db_itemDesejo)
        return db_itemDesejo

    def listar(self, id: int):
        query = self.session.query(models.ItemDesejo).where(
            models.ItemDesejo.usuario_id == id)
        return self.session.execute(query).scalars().all()

    def editar(self, id: int, itemDesejo: schemas.ItemDesejo):
        update_stmt = update(models.ItemDesejo).where(models.ItemDesejo.id == id).values(nome=itemDesejo.nome,
                                                                                         descricao=itemDesejo.descricao,
                                                                                         prioridade=itemDesejo.prioridade,
                                                                                         preco=itemDesejo.preco,
                                                                                         adquirido=itemDesejo.adquirido,
                                                                                         usuario_id=itemDesejo.usuario_id
                                                                                         )
        self.session.execute(update_stmt)
        self.session.commit()

    def obter_item_por_id(self, id: int):
        query = select(models.ItemDesejo).where(
            models.ItemDesejo.id == id)
        return self.session.execute(query).scalars().first()

    def obter_umItem_por_id(self, id: str, id_usuario: int = None):
        if id_usuario is None:
            item = self.obter_item_por_id(id)
        else:
            query = select(models.ItemDesejo).where(
                models.ItemDesejo.id == id and models.ItemDesejo.usuario_id == id_usuario)
            item = self.session.execute(query).scalars().first()
        return item

    def remover(self, id: int, id_usuario: int = None):
        itemDesejo = self.obter_item_por_id(id)
        if id_usuario is not None:
            delete_stmt = delete(models.ItemDesejo).where(
                models.ItemDesejo.id == id and models.ItemDesejo.usuario_id == id_usuario)
        else:
            delete_stmt = delete(models.ItemDesejo).where(
                models.ItemDesejo.id == id)
        self.session.execute(delete_stmt)
        self.session.commit()
        return itemDesejo
