from fastapi import FastAPI
from app.api.endpoints import registration, nested
from app.api.endpoints import csv_loader, delete_records  # новые импорты
from app.db.database import engine, Base
from contextlib import asynccontextmanager

# Создаем таблицы БД
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Сервер запущен, Redis подключен")
    yield
    # Shutdown
    print("Сервер остановлен")

app = FastAPI(
    title="User Registration Service",
    description="Домашнее задание по FastAPI и Pydantic",
    version="1.0.0",
    lifespan=lifespan
)

# Подключаем роутеры
app.include_router(registration.router)
app.include_router(nested.router)
app.include_router(csv_loader.router)       # новый
app.include_router(delete_records.router)   # новый

@app.get("/")
async def root():
    return {
        "message": "Добро пожаловать в API регистрации пользователей",
        "docs": "/docs",
        "endpoints": [
            "/register/ - регистрация пользователя",
            "/nested/ - получение вложенной структуры (кешируется)",
            "/load-csv/ - загрузка CSV в БД (фоновая задача)",
            "/delete-records/ - удаление записей из БД (фоновая задача)"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)