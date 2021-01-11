import os

import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

try:
    MONGO_URL = config('MONGO_URL')
except:
    MONGO_URL = os.getenv('MONGO_URL')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

database = client.todo

todo_collection = database.get_collection('tasks')


def todo_helper(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "status": todo["status"],
    }

# Retrieve all todos


async def get_all_todos():
    todos = []
    async for todo in todo_collection.find():
        todos.append(todo_helper(todo))
    return todos


# Add a new todo into to the database
async def create_todo(todo_data: dict) -> dict:
    todo = await todo_collection.insert_one(todo_data)
    new_todo = await todo_collection.find_one({"_id": todo.inserted_id})
    return todo_helper(new_todo)


# Retrieve a todo with a matching ID
async def get_todo_by_id(id: str) -> dict:
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    if todo:
        return todo_helper(todo)


# Update a todo with a matching ID
async def update_todo(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    if todo:
        updated_todo = await todo_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_todo:
            return True
        return False


# Delete a todo from the database
async def delete_todo(id: str):
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    if todo:
        await todo_collection.delete_one({"_id": ObjectId(id)})
        return True
