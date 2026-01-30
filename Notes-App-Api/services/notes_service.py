from sqlalchemy.orm import Session
from schemas.notes import AddNote, NotesCategories, UpdateNote
from databse_settings.models import Notes, DbUsers
from core import exceptions
from typing import Optional




class NotesServiceManager:

    def get_all_notes(self, user: DbUsers):
        all_notes = user.notes
        return all_notes
        
    def adding_note(self, data: AddNote, category: NotesCategories, db: Session, user: DbUsers):

        new_note = Notes(user_id=user.id, title=data.title, category=category, content=data.content)
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
        return new_note
    
    
    def remove_note(self, id: int, db: Session, user: DbUsers):
        note = db.query(Notes).filter(Notes.id == id).one_or_none()

        if not note:
            raise exceptions.NoteIdNotFound(id)
        
        if note.user_id != user.id:
            raise exceptions.NoteIdNotFound(id)
        
        
        db.delete(note)
        db.commit()
        return note

    def update_note(self, user: DbUsers, db: Session, id: int, data: UpdateNote, new_category: Optional[NotesCategories] = None):
        note = db.query(Notes).filter(Notes.id == id).one_or_none()
        if not note:
            raise exceptions.NoteIdNotFound(id)
        
        if note.user_id != user.id:
            raise exceptions.NoteIdNotFound(id)
        
        if data.title:
            note.title = data.title
        
        elif data.content:
            note.content = data.content
        
        elif new_category:
            note.category = new_category
        
        db.commit()
        return note
        
        

        