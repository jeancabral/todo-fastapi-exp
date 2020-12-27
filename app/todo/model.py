from pydantic import BaseModel
from typing import Optional
from app.data.todos import StatusOptions

class TodoItem(BaseModel):
  title: str
  description: str = None
  status: Optional[StatusOptions]

class TodoItemResponse(BaseModel):
  id: int
  title: str
  description: str = None
  status: Optional[StatusOptions]