from typing import Optional, Any
from pydantic import BaseModel, ConfigDict

class TreeNode(BaseModel):
    """Рекурсивная модель для дерева"""
    data: Any
    child: Optional['TreeNode'] = None
    
    model_config = ConfigDict(arbitrary_types_allowed = True)

TreeNode.model_rebuild()