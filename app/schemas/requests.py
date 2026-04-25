from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserRegistrationRequest(BaseModel):
    """Схема запроса на регистрацию пользователя"""
    username: str = Field(..., min_length = 3, max_length = 20, 
                         description = "Имя пользователя (латиница, цифры, _)")
    email: EmailStr = Field(..., description = "Email пользователя")
    password: str = Field(..., min_length = 8, 
                         description = "Пароль (минимум 8 символов, заглавные, строчные, цифры)")
    password_confirm: str = Field(..., description = "Подтверждение пароля")
    age: int = Field(..., ge = 18, le = 120, description = "Возраст (18-120 лет)")
    full_name: str = Field(..., min_length = 2, description = "Полное имя (с заглавной буквы)")
    phone: str = Field(..., description = "Телефон в формате +X-XXX-XX-XX")
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "john@example.com",
                "password": "Password123",
                "password_confirm": "Password123",
                "age": 25,
                "full_name": "John Doe",
                "phone": "+7-999-123-45-67"
            }
        }

class NestedStructureRequest(BaseModel):
    """Схема запроса для создания вложенной структуры"""
    depth: int = Field(5, ge=1, le=100, description="Глубина вложенности")
    data_prefix: str = Field("any_data", description="Префикс для данных")