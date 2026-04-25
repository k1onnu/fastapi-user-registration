from fastapi import APIRouter, Query
from app.services.tree_service import TreeService

def cache_response(expire: int = 60):
    def decorator(func):
        return func
    return decorator

router = APIRouter(prefix="/nested", tags=["Вложенные структуры"])

@router.get("/")
@cache_response(expire=120)
async def get_nested_structure(
    depth: int = Query(5, ge=1, le=100, description="Глубина вложенности")
):
    """
    Возвращает JSON с произвольной вложенностью
    """
    service = TreeService()
    structure = service.create_nested_structure(depth)
    return structure.model_dump()