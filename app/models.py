from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    pending = 'Pending'
    in_progress = 'In Progress'
    completed = 'Completed'

class TaskPriority(int, Enum):
    low = 1
    medium = 2
    high = 3

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending # setting default value
    priority: TaskPriority = TaskPriority.medium # setting default value