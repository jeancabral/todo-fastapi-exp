from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from typing import List, Dict, Any

from app.data.database import (get_all_todos, create_todo)
from app.todo.model import TodoItem, TodoItemResponse, ResponseModel


router = APIRouter()


@router.get('/list', response_description="Todos retrieved")
async def list_todos():
    todos = await get_all_todos()
    if todos:
        return ResponseModel(todos, 'Data retrieved successfully')
    return ResponseModel(todos, 'Empty list returned')


@router.post("/create", response_description="Todo added into the db")
async def todo_create(todo: TodoItem = Body(...)):
    todo = jsonable_encoder(todo)
    new_todo = await create_todo(todo)
    return ResponseModel(new_todo, "Todo added successfully.")
