from pydantic import BaseModel
from typing import List, Optional, Any

class ErrorDetail(BaseModel):
    """Детали ошибки валидации"""
    field: str
    message: str

class ErrorResponse(BaseModel):
    """Ответ с ошибкой"""
    status: str = "error"
    message: str
    errors: Optional[List[ErrorDetail]] = None

class SuccessResponse(BaseModel):
    """Успешный ответ"""
    status: str = "success"
    message: str

class UserRegistrationResponse(SuccessResponse):
    """Ответ при успешной регистрации"""
    user: dict

class TreeResponse(BaseModel):
    """Ответ с древовидной структурой"""
    data: Any
    child: Optional['TreeResponse'] = None

TreeResponse.model_rebuild()