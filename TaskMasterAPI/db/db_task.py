from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.connection import get_db
from routes.schemas import TaskBase, UpdateTask
from db.models import DbTask, DbUser


class TaskManager:


    def add_task(self, request: TaskBase, db: Session, user: DbUser):


        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'User With Id : {request.user_id} Not Found'
            )
    
        task = DbTask(
            title=request.title,
            description=request.description,
            deadline=request.deadline,
            user_id=user.id
        )

        db.add(task)
        db.commit()
        db.refresh(task)

        return {'msg': 'Task Added Done'}
    

    def show_task(self, id: int, db: Session):

        task = db.query(DbTask).filter(DbTask.id == id).one_or_none()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Task With Id : {id} Not Found'
            )
        
        return task
    

    def update_task(self, id: int, request: UpdateTask, db: Session, user: DbUser):
    
        task = db.query(DbTask).filter(DbTask.id == id).one_or_none()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Task With Id : {id} Not Found'
            )
        
        elif task.user_id != user.id:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='You Are Not The Creator!')
        
        task.title = request.title
        task.description = request.description
        task.deadline = request.deadline

        db.commit()
        return {
            'msg': 'Task Updated Done'
        }
    
    def delete_task(self, id: int, db: Session, user: DbUser):
    
        task = db.query(DbTask).filter(DbTask.id == id).one_or_none()

        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Task With Id : {id} Not Found'
            )
        
        elif task.user_id != user.id:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail='You Are Not The Creator!')
        
        db.delete(task)
        db.commit()
        
        return {
            'msg': 'Task Removed Done'
        }