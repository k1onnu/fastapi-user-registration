import pytest
from app.services.registration_service import RegistrationService
from app.schemas.responses import ErrorResponse

def test_successful_registration():
    """Тест успешной регистрации"""
    service = RegistrationService()
    
    valid_data = {
        "username": "john_doe",
        "email": "john@example.com",
        "password": "Password123",
        "password_confirm": "Password123",
        "age": 25,
        "full_name": "John Doe",
        "phone": "+7-999-123-45-67"
    }
    
    result = service.register_user(valid_data)
    
    assert not isinstance(result, ErrorResponse)
    assert result.username == "john_doe"
    assert result.email == "john@example.com"

def test_failed_registration():
    """Тест неуспешной регистрации"""
    service = RegistrationService()
    
    invalid_data = {
        "username": "john@doe",
        "email": "not-an-email",
        "password": "weak",
        "password_confirm": "different",
        "age": 15,
        "full_name": "john doe",
        "phone": "89991234567"
    }
    
    result = service.register_user(invalid_data)
    
    assert isinstance(result, ErrorResponse)
    assert result.errors is not None
    assert len(result.errors) > 0

def test_registration_with_missing_field():
    """Тест регистрации с отсутствующим полем"""
    service = RegistrationService()
    
    incomplete_data = {
        "username": "john_doe",
        "email": "john@example.com",
        "password": "Password123",
        "password_confirm": "Password123",
        # age отсутствует
        "full_name": "John Doe",
        "phone": "+7-999-123-45-67"
    }
    
    result = service.register_user(incomplete_data)
    assert isinstance(result, ErrorResponse)
    assert result.errors is not None