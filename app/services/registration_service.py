from typing import Union
from app.models.user import UserRegistration
from app.schemas.responses import ErrorResponse, ErrorDetail

class RegistrationService:
    """Сервис для регистрации пользователей"""
    
    @staticmethod
    def register_user(data: dict) -> Union[UserRegistration, ErrorResponse]:
        """
        Валидация и регистрация пользователя
        
        Args:
            data: словарь с данными пользователя
        
        Returns:
            При успехе: объект UserRegistration
            При ошибке: ErrorResponse
        """
        try:
            user = UserRegistration(**data)
            return user
        except Exception as e:
            return RegistrationService._handle_validation_error(e)
    
    @staticmethod
    def _handle_validation_error(error: Exception) -> ErrorResponse:
        """Обработка ошибок валидации"""
        if hasattr(error, 'errors'):
            errors = []
            for err in error.errors():
                field = err['loc'][0] if err['loc'] else 'unknown'
                message = err['msg']
                errors.append(ErrorDetail(field=field, message=message))
            
            return ErrorResponse(
                message="Ошибка валидации данных",
                errors=errors
            )
        else:
            return ErrorResponse(message=str(error))