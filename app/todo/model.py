from pydantic import BaseModel
from typing import Optional

class TodoItem(BaseModel):
  title: str
  description: str = None
  status: str = None

class TodoItemResponse(BaseModel):
  id: int
  title: str
  description: str = None
  status: str = None