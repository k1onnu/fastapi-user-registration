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