from fastapi import FastAPI

from app.todo.routes import router as TodoResource

app = FastAPI()

app.include_router(TodoResource, tags=['todo'], prefix='/todo')


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "FastAPI Exp"}
