import pytest
from app.models.user import UserRegistration

def test_username_validation():
    """Тест валидации username"""
    with pytest.raises(ValueError, match="только латинские буквы"):
        UserRegistration(
            username="тест",
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
            password="password123",
            password_confirm="password123",
            age=25,
            full_name="Test User",
            phone="+7-999-123-45-67"
        )

def test_phone_validation():
    """Тест валидации телефона"""
    with pytest.raises(ValueError, match="формате"):
        UserRegistration(
            username="testuser",
            email="test@test.com",
            password="Password123",
            password_confirm="Password123",
            age=25,
            full_name="Test User",
            phone="89991234567"
        )

def test_age_validation():
    """Тест валидации возраста"""
    with pytest.raises(ValueError):
        UserRegistration(
            username="testuser",
            email="test@test.com",
            password="Password123",
            password_confirm="Password123",
            age=15,
            full_name="Test User",
            phone="+7-999-123-45-67"
        )

def test_full_name_validation():
    """Тест валидации полного имени"""
    with pytest.raises(ValueError, match="заглавной буквы"):
        UserRegistration(
            username="testuser",
            email="test@test.com",
            password="Password123",
            password_confirm="Password123",
            age=25,
            full_name="john doe",
            phone="+7-999-123-45-67"
        )

def test_password_match_validation():
    """Тест совпадения паролей"""
    with pytest.raises(ValueError, match="Пароли не совпадают"):
        UserRegistration(
            username="testuser",
            email="test@test.com",
            password="Password123",
            password_confirm="DifferentPassword123",
            age=25,
            full_name="John Doe",
            phone="+7-999-123-45-67"
        )

def test_email_validation():
    """Тест валидации email"""
    with pytest.raises(ValueError):
        UserRegistration(
            username="testuser",
            email="not-an-email",
            password="Password123",
            password_confirm="Password123",
            age=25,
            full_name="John Doe",
            phone="+7-999-123-45-67"
        )

def test_valid_user():
    """Тест успешного создания пользователя"""
    user = UserRegistration(
        username="john_doe",
        email="john@example.com",
        password="Password123",
        password_confirm="Password123",
        age=25,
        full_name="John Doe",
        phone="+7-999-123-45-67"
    )
    assert user.username == "john_doe"
    assert user.email == "john@example.com"
    assert user.age == 25
    assert user.full_name == "John Doe"