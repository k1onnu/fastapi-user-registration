from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from app.db.database import Base

class DataRecord(Base):
    """Модель для данных из CSV файла"""
    __tablename__ = "data_records"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(Float)
    category = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class User(Base):
    """Модель пользователя (расширенная)"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)  # хешировать в реал project
    age = Column(Integer)
    full_name = Column(String)
    phone = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())