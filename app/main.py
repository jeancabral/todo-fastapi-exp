from fastapi import FastAPI
from app.todo import todo_resource

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

def build_api():
    """Build API"""
    app.include_router(todo_resource.router, prefix="/todo", tags=["todo"])

    return app
