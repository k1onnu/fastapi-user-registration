import sys
import os

# Добавляем путь к корню проекта
sys.path.insert(0, r"E:\vs_project\fastapi-user-registration")

print("Текущий sys.path:")
for p in sys.path:
    print(f"  {p}")

try:
    from app.services.tree_service import TreeService
    print("Импорт успешен!")
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    raise

def test_tree_creation():
    """Тест создания дерева"""
    service = TreeService()
    
    tree = service.create_nested_structure(3)
    
    assert tree.data == "any_data_1"
    assert tree.child is not None
    assert tree.child.data == "any_data_2"
    assert tree.child.child is not None
    assert tree.child.child.data == "any_data_3"
    assert tree.child.child.child is None


from app.services.tree_service import TreeService

def test_tree_creation():
    """Тест создания дерева"""
    service = TreeService()
    
    tree = service.create_nested_structure(3)
    
    assert tree.data == "any_data_1"
    assert tree.child is not None
    assert tree.child.data == "any_data_2"
    assert tree.child.child is not None
    assert tree.child.child.data == "any_data_3"
    assert tree.child.child.child is None

def test_tree_depth_zero():
    """Тест создания дерева с глубиной 0"""
    service = TreeService()
    
    tree = service.create_nested_structure(0)
    
    assert tree.data == "any_data_0"
    assert tree.child is None

def test_tree_custom_prefix():
    """Тест с кастомным префиксом"""
    service = TreeService()
    
    tree = service.create_nested_structure(2, "custom")
    
    assert tree.data == "custom_1"
    assert tree.child.data == "custom_2"