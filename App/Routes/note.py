from fastapi import APIRouter, Depends, HTTPException
from App.Models.note import NoteCreate,NoteResponse, NoteUpdate
from App.utils.authentication import get_current_user
from App.CRUD.note import create_note, delete_note, get_note,get_notes, update_note

router = APIRouter(prefix="/notes")
@router.post("/")
async def create_note_api(note:NoteCreate, current_user: dict = Depends(get_current_user)):
    note_json=note.model_dump()
    note_json["user_id"] = current_user["id"]
    new_note=NoteCreate(**note_json)
    await create_note(new_note)
    return {"message": "Note created successfully"}

@router.get("/{note_id}",response_model=NoteResponse)
async def get_note_api(note_id: str, current_user: dict = Depends(get_current_user)):
    note = await get_note(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteResponse(
        id=str(note["_id"]),
        user_id=note["user_id"],
        title=note["title"],
        content=note["content"],
        created_at=note["created_at"],
        updated_at=note["updated_at"]
    )
@router.get("/",response_model=list[NoteResponse])
async def get_notes_api():
    notes=await get_notes()
    return [NoteResponse(id=str(note["_id"]),**note) for note in notes]

@router.put("/{note_id}",response_model=NoteUpdate)
async def update_note_api(note_id:str, note:NoteUpdate, current_user: dict = Depends(get_current_user)):
    
    note_json=note.model_dump(exclude_unset=True)
    note_json["user_id"] = current_user["id"]
    updated_note_data={**note_json}
    updated_note=NoteCreate(**updated_note_data)
    await update_note(note_id, updated_note)
    if not update_note:
        raise HTTPException(status_code=500, detail="Failed to update note")
    return {"message": "Note updated successfully"}

@router.delete("/{note_id}")
async def delete_note_api(note_id:str, current_user: dict = Depends(get_current_user)):
    result=await delete_note(note_id)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to delete note")
    return {"message": "Note deleted successfully"}