#Python
from typing import Optional
from uuid import UUID
from datetime import date, datetime

#Pydantic
from pydantic import BaseModel, EmailStr, FilePath, Field

class PersonBase(BaseModel):
    user_id: int = Field(...)
    streamer: Optional[bool] = Field(default=False)
    name: str = Field(
        ...,
        min_length=1,
        max_length=50,)
    birth_date: date = Field(...)
    Email: EmailStr = Field(...)
    videos:Optional[bool] = Field(default=False)

class PersonLogin(PersonBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        description="Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter and one number",
    )

class Video(BaseModel):
    video_id: UUID = Field(...)
    content: FilePath = Field(...)
    start_at: datetime = Field(default=datetime.now())
    finished_at: Optional[datetime] = Field(default=None)
    video_time: Optional[int] = Field(defaul=None)
    by:PersonBase = Field(...)

class Chat(BaseModel):
    chat_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
        )
    created_at: date = Field(default=date.today())
    by:PersonBase = Field(...)
    on_video: Video = Field(...)