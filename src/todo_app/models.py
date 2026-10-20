from pydantic import BaseModel

class Todo(BaseModel):
    id: int = None
    title: str = None
    description: str = None
    isDone: bool = False