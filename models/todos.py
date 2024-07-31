from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    title: str
    description: str
    complete: Optional[bool] = False