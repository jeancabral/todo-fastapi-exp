from fastapi import APIRouter
from typing import List, Dict, Any

from app.data.todos import Todos
from app.todo.model import TodoItem, TodoItemResponse

todo = Todos()
router = APIRouter()

@router.get("/list", response_model=List[TodoItem])
async def todo_list():
    return todo.list_todo()

@router.post("/create", response_model=TodoItemResponse, status_code=201)
async def todo_create(item: TodoItem):
    return todo.create_todo(item.dict())
