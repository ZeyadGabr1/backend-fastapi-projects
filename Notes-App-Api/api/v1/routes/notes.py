from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from schemas.notes import DisplayNotes, AddNote, NotesCategories, UpdateNote
from typing import List
from services.notes_service import NotesServiceManager
from sqlalchemy.orm import Session
from databse_settings.settings import get_db
from typing import Optional
from auth.oauth2 import oauth2_schema
from auth.config import get_current_user
from databse_settings.models  import DbUsers
from core import exceptions



router = APIRouter(
    prefix="/notes",
    tags=["v1-notes"],
    default_response_class=JSONResponse,
    deprecated=False
    )


service_manager = NotesServiceManager()


@router.get('/', 
            response_model=List[DisplayNotes],
            description="endpoint return all notes that user record"
            )
def all_notes(user: DbUsers = Depends(get_current_user)):
    if not user:
        raise exceptions.UnauthorizedUser
    
    return service_manager.get_all_notes(user)

@router.post("/",
            response_model=DisplayNotes,
            description="endpoint that adding note "
             )
def add_note(request: AddNote, category: NotesCategories, db: Session = Depends(get_db), user: DbUsers = Depends(get_current_user)):
    if not user:
        raise exceptions.UnauthorizedUser
    
    new_note = service_manager.adding_note(request, category, db, user)
    return new_note
    


@router.put("/{id}",
            response_model=DisplayNotes,
            description="endpoint that allow user to edit note "
            )
def edit_note(request: UpdateNote, id: int, category: Optional[NotesCategories] = None, db: Session = Depends(get_db), 
              user: DbUsers = Depends(get_current_user)):
    if not user:
        raise exceptions.UnauthorizedUser
    
    note = service_manager.update_note(user, db, id, request, category)
    return note
    

@router.delete("/{id}")
def delete_note(id: int, db: Session = Depends(get_db), user: DbUsers = Depends(get_current_user)):
    if not user:
        raise exceptions.UnauthorizedUser
    
    reslut =  service_manager.remove_note(id, db, user)
    return reslut
    