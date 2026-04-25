from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from app.db.database import get_db
from app.tasks.background_tasks import delete_records_task

router = APIRouter(prefix="/delete-records", tags=["Удаление данных"])

class DeleteRequest(BaseModel):
    ids: List[int]

class DeleteResponse(BaseModel):
    message: str
    task_id: str
    status: str = "accepted"

@router.post("/", response_model=DeleteResponse)
async def delete_records(
    request: DeleteRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Удаляет записи из БД по переданному списку ID как фоновая задача
    """
    if not request.ids:
        raise HTTPException(status_code=400, detail="Список ID не может быть пустым")
    
    background_tasks.add_task(delete_records_task, db, request.ids)
    
    return DeleteResponse(
        message=f"Задача удаления {len(request.ids)} записей запущена",
        task_id=f"delete_{hash(str(request.ids))}",
        status="accepted"
    )