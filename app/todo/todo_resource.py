from fastapi import APIRouter
from typing import List, Dict, Any
from pydantic import BaseModel


router = APIRouter()

todo: List[Dict[str, Any]] = [
  {"id": 1, "title": "Estudar Python", "description": "Cap 3 do Fluente Python", "status": "a fazer"}
]

class TodoItem(BaseModel):
  id: int
  title: str
  description: str = None
  status: str = None


@router.get("/list", response_model=List[TodoItem])
async def todo_list():
    return todo
