from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, ConfigDict
import re

class UserRegistration(BaseModel):
    """Модель пользователя для регистрации"""
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=8)
    password_confirm: str
    age: int = Field(..., ge=18, le=120)
    registration_date: datetime = Field(default_factory=datetime.now)
    full_name: str = Field(..., min_length=2)
    phone: str
    
    model_config = ConfigDict(
        json_schema_extra={
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
    )
    
    # Валидация username
    @field_validator('username')
    def validate_username(cls, v):
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('Username должен содержать только латинские буквы, цифры и символ подчеркивания')
        return v
    
    # Валидация сложности пароля
    @field_validator('password')
    def validate_password(cls, v):
        if not re.search(r'[A-Z]', v):
            raise ValueError('Пароль должен содержать хотя бы одну заглавную букву')
        if not re.search(r'[a-z]', v):
            raise ValueError('Пароль должен содержать хотя бы одну строчную букву')
        if not re.search(r'\d', v):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        return v
    
    # Валидация full_name
    @field_validator('full_name')
    def validate_full_name(cls, v):
        if not v or not v[0].isupper():
            raise ValueError('Полное имя должно начинаться с заглавной буквы')
        parts = v.split()
        for part in parts:
            if not part or not part[0].isupper():
                raise ValueError('Каждая часть полного имени должна начинаться с заглавной буквы')
        return v
    
    # Валидация телефона 
    @field_validator('phone')
    def validate_phone(cls, v):
        digits = v.replace('-', '')
        
        if not re.match(r'^\+\d+$', digits):
            raise ValueError('Телефон должен начинаться с + и содержать только цифры и дефисы')
        
        # Проверяем количество цифр
        digit_count = len(digits) - 1
        if digit_count < 10 or digit_count > 15:
            raise ValueError('Телефон должен содержать от 10 до 15 цифр')
        
        # Проверяем формат с дефисами
        if not re.match(r'^\+\d(-\d{1,4}){2,5}$', v):
            pass
            
        return v
    
    # Валидация совпадения паролей
    @model_validator(mode='after')
    def validate_passwords_match(self):
        if self.password != self.password_confirm:
            raise ValueError('Пароли не совпадают')
        return self
    
    def dict_without_password(self) -> dict:
        """Возвращает словарь без поля password_confirm"""
        return self.model_dump(exclude={'password_confirm'})