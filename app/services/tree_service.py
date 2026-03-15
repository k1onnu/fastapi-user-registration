from app.models.tree import TreeNode

class TreeService:
    """Сервис для работы с древовидными структурами"""
    
    @staticmethod
    def create_nested_structure(depth: int, data_prefix: str = "any_data") -> TreeNode:
        """
        Создает вложенную структуру заданной глубины
        
        Args:
            depth: глубина вложенности
            data_prefix: префикс для данных
        
        Returns:
            TreeNode с указанной глубиной вложенности
        """
        if depth <= 0:
            return TreeNode(data=f"{data_prefix}_0")
        
        root = TreeNode(data=f"{data_prefix}_1")
        current = root
        
        for i in range(2, depth + 1):
            current.child = TreeNode(data = f"{data_prefix}_{i}")
            current = current.child
        
        return root