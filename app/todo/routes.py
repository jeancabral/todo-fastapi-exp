from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from typing import List, Dict, Any

from app.data.database import (get_all_todos, create_todo, get_todo_by_id, update_todo, delete_todo)
from app.todo.model import TodoItem, TodoItemResponse, ResponseModel, ErrorResponseModel, TodoItemUpdate


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


@router.get("/{id}", response_description="Todo data retrieved")
async def get_todo_data(id):
    todo = await get_todo_by_id(id)
    if todo:
        return ResponseModel(todo, "Todo data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Todo not found.")

@router.put("/{id}")
async def update_todo_data(id: str, req: TodoItemUpdate = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_todo = await update_todo(id, req)
    if updated_todo:
        return ResponseModel(
            "Todo with ID: {} name update is successful".format(id),
            "Todo name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the todo.",
    )


@router.delete("/{id}", response_description="Todo data deleted from the mongodb")
async def delete_todo_data(id: str):
    deleted_todo = await delete_todo(id)
    if deleted_todo:
        return ResponseModel(
            "Todo with ID: {} removed".format(id), "Todo deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Todo with id {0} doesn't exist".format(id)
    )