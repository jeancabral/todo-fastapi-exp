from pydantic import BaseModel

class TodoItem(BaseModel):
  id: int
  title: str
  description: str = None
  status: str = None