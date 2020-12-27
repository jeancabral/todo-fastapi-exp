from fastapi import APIRouter
from typing import List, Dict, Any

from app.data.todos import Todos
from app.todo.model import TodoItem


router = APIRouter()

@router.get("/list", response_model=List[TodoItem])
async def todo_list():
    return Todos.list_todo()
