from fastapi import BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
import csv
from typing import List
import os

def load_csv_task(db: Session, file_path: str):
    """Фоновая задача загрузки CSV в БД"""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл {file_path} не найден")
        
        records = []
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Преобразуем value в float
                if 'value' in row:
                    row['value'] = float(row['value'])
                records.append(row)
        
        from app.db.crud import create_records_bulk
        count = create_records_bulk(db, records)
        
        # Здесь можно добавить логирование или уведомление
        print(f"Загружено {count} записей из {file_path}")
        return {"status": "success", "loaded": count, "file": file_path}
    
    except Exception as e:
        print(f"Ошибка загрузки CSV: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Ошибка загрузки: {str(e)}")

def delete_records_task(db: Session, ids: List[int]):
    """Фоновая задача удаления записей"""
    try:
        from app.db.crud import delete_records_by_ids
        deleted_count = delete_records_by_ids(db, ids)
        
        print(f"Удалено {deleted_count} записей с ID: {ids}")
        return {"status": "success", "deleted": deleted_count, "ids": ids}
    
    except Exception as e:
        print(f"Ошибка удаления: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Ошибка удаления: {str(e)}")