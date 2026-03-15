from fastapi import APIRouter, HTTPException
from app.services.registration_service import RegistrationService
from app.schemas.responses import UserRegistrationResponse, ErrorResponse

router = APIRouter(prefix = "/register", tags = ["Регистрация"])

@router.post("/", response_model = UserRegistrationResponse, responses = {400: {"model": ErrorResponse}})
async def register(user_data: dict):
    """
    Эндпоинт для регистрации нового пользователя
    """
    service = RegistrationService()
    result = service.register_user(user_data)
    
    if isinstance(result, ErrorResponse):
        raise HTTPException(status_code = 400, detail = result.model_dump())
    
    return UserRegistrationResponse(
        message="Пользователь успешно зарегистрирован",
        user=result.dict_without_password()
    )