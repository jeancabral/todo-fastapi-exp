from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class StatusOptions(str, Enum):
    not_completed = "Não concluído"
    doing = "Fazendo"
    done = "Feito"


class TodoItem(BaseModel):
    title: str = Field(...)
    description: Optional[str]
    status: Optional[StatusOptions]

    class Config:
        schema_extra = {
            "example": {
                "title": "Some Title",
                "description": "Describe your todo",
                "status": "Feito",
            }
        }

class TodoItemUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[StatusOptions]

    class Config:
        schema_extra = {
            "example": {
                "title": "Some Title",
                "description": "Describe your todo",
                "status": "Feito",
            }
        }

class TodoItemResponse(BaseModel):
    id: int
    title: str
    description: str = None
    status: Optional[StatusOptions]


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
