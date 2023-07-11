from pydantic import BaseModel


class Task(BaseModel):
    name: str
    priority: str
    complete: bool