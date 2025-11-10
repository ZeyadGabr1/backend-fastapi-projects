from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.connection import get_db
from routes.schemas import TaskBase, UpdateTask
from db.models import DbUser
from db.db_task import TaskManager
from auth.oath2 import oauth2_schema, get_current_user


router = APIRouter(
    prefix='/task',
    tags=['tasks']
)

task_manager = TaskManager()


@router.post('/add')
def add_task(request: TaskBase, db: Session = Depends(get_db), user: DbUser = Depends(get_current_user)):
    return task_manager.add_task(request, db, user)



@router.get('/{id}', response_model=TaskBase)
def show_task(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_schema)):
    return task_manager.show_task(id, db)


@router.put('/update/{id}')
def update_task(id: int, request: UpdateTask, db: Session = Depends(get_db), user: DbUser = Depends(get_current_user)):
    return task_manager.update_task(id, request, db, user)

@router.delete('/delete/{id}')
def delete_task(id: int, db: Session = Depends(get_db), user: DbUser = Depends(get_current_user)):
    return task_manager.delete_task(id, db, user)