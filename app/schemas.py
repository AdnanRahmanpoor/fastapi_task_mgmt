"""
Schema for Creating and Updating Tasks
"""

from pydantic import BaseModel
from typing import Optional
from app.models import TaskStatus, TaskPriority

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[TaskStatus] = TaskStatus.pending
    priority: Optional[TaskPriority] = TaskPriority.medium


class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str] 
    status: Optional[TaskStatus]
    priority: Optional[TaskPriority]
