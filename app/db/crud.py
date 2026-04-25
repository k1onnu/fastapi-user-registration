from sqlalchemy.orm import Session
from app.db.models import DataRecord, User
from typing import List

def create_records_bulk(db: Session, records: List[dict]):
    """Массовая вставка записей"""
    db_records = [DataRecord(**record) for record in records]
    db.add_all(db_records)
    db.commit()
    return len(db_records)

def delete_records_by_ids(db: Session, ids: List[int]):
    """Удаление записей по списку ID"""
    deleted = db.query(DataRecord).filter(DataRecord.id.in_(ids)).delete(synchronize_session=False)
    db.commit()
    return deleted

def get_all_records(db: Session):
    """Получение всех записей"""
    return db.query(DataRecord).all()

def create_user(db: Session, user_data: dict):
    """Создание пользователя в БД"""
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user