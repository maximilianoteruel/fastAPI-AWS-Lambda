from typing import List, Optional

from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    description: str
    tags: Optional[str] = None


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int

    class Config:
        orm_mode = True
