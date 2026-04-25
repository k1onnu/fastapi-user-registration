from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from app.db.database import get_db
from app.tasks.background_tasks import load_csv_task

router = APIRouter(prefix="/load-csv", tags=["Загрузка данных"])

class CSVLoadRequest(BaseModel):
    file_path: str

class TaskResponse(BaseModel):
    message: str
    task_id: str
    status: str = "accepted"

@router.post("/", response_model=TaskResponse)
async def load_csv_from_file(
    request: CSVLoadRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """
    Загружает данные из CSV файла в БД как фоновая задача
    
    Ожидается CSV с колонками: name, value, category
    """
    background_tasks.add_task(load_csv_task, db, request.file_path)
    
    return TaskResponse(
        message="Задача загрузки CSV запущена",
        task_id=f"csv_load_{hash(request.file_path)}",
        status="accepted"
    )