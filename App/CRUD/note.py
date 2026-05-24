from App.Routes.db import db
from App.Models.note import NoteCreate
from bson import ObjectId

note_collection=db["ReviNotes"]

async def create_note(note:NoteCreate):
    note_json=note.model_dump()
    result=await note_collection.insert_one(note_json)
    return True

async def get_note(note_id:str):
    return await note_collection.find_one({"_id":ObjectId(note_id)})

"""nc def get_note(note_id: str):
    print(note_id)
    note = await note_collection.find_one(
        {"_id": ObjectId(note_id)}
    )
    print(note)
    return note"""

async def get_notes():
    return await note_collection.find().to_list()

async def update_note(note_id:str, note:NoteCreate):
    note_json=note.model_dump()
    result=await note_collection.update_one({"_id":ObjectId(note_id)},{"$set":note_json})
    return result.modified_count > 0

async def delete_note(note_id:str):
    result=await note_collection.delete_one({"_id":ObjectId(note_id)})
    return result.deleted_count > 0