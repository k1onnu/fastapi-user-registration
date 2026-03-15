from fastapi import FastAPI
from app.api.endpoints import registration, nested

app = FastAPI(
    title="User Registration Service",
    description="Домашнее задание по FastAPI и Pydantic",
    version="1.0.0"
)

# Подключаем роутеры
app.include_router(registration.router)
app.include_router(nested.router)

@app.get("/")
async def root():
    return {
        "message": "Добро пожаловать в API регистрации пользователей",
        "docs": "/docs",
        "endpoints": [
            "/register/ - регистрация пользователя",
            "/nested/ - получение вложенной структуры"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port = 8000, reload = True)