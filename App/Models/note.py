from pydantic import BaseModel
from datetime import datetime
from typing import Optional 

class NoteCreate(BaseModel):
    user_id:Optional[str]=None
    title:str
    content:str
    created_at:Optional[datetime] = datetime.now()
    updated_at:Optional[datetime] = datetime.now()

class NoteUpdate(BaseModel):
    title:Optional[str]=None
    content:Optional[str]=None
    updated_at:Optional[datetime] = datetime.now()

class NoteResponse(BaseModel):
    id:str
    user_id:str
    title:str
    content:str
    created_at:datetime
    updated_at:datetime 
