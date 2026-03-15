import pytest
from app.models.user import UserRegistration

def test_username_validation():
    """Тест валидации username"""
    with pytest.raises(ValueError, match="только латинские буквы"):
        UserRegistration(
            username="тест",  # русские буквы
            email="test@test.com",
            password="Password123",
            password_confirm="Password123",
            age=25,
            full_name="Test User",
            phone="+7-999-123-45-67"
        )

def test_password_validation():
    """Тест валидации пароля"""
    with pytest.raises(ValueError, match="хотя бы одну заглавную букву"):
        UserRegistration(
            username="testuser",
            email="test@test.com",
            password="password123",  # нет заглавной
            password_confirm="password123",
            age=25,
            full_name="Test User",
            phone="+7-999-123-45-67"
        )