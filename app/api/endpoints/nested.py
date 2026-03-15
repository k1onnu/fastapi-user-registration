from fastapi import APIRouter, Query
from app.services.tree_service import TreeService

router = APIRouter(prefix="/nested", tags=["Вложенные структуры"])

@router.get("/")
async def get_nested_structure(
    depth: int = Query(5, ge = 1, le = 100, description="Глубина вложенности")
):
    """
    Возвращает JSON с произвольной вложенностью
    """
    service = TreeService()
    structure = service.create_nested_structure(depth)
    return structure.model_dump()