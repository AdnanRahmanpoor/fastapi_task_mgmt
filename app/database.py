"""
A in-memory database will be created to simulate how the API will perform CRUD on it.
"""

from typing import List, Optional
from app.models import Task, TaskStatus, TaskPriority

# in-memory database
tasks_db: List[Task] = []

def get_tasks(status: Optional[TaskStatus] = None, priority: Optional[TaskPriority] = None) -> List[Task]:
    filtered_tasks = tasks_db

    if status:
        filtered_tasks = [task for task in filtered_tasks if task.status == status]
    if priority:
        filtered_tasks = [task for task in filtered_tasks if task.priority == priority]
    return filtered_tasks

def get_task(task_id: int) -> Optional[Task]:
    return next((task for task in tasks_db if task.id == task_id), None)

def add_task(task: Task):
    tasks_db.append(task)

def update_task(task_id: int, updated_task:Task) -> Optional[Task]:
    task = get_task()

    if task:
        task.title = updated_task.title
        task.description = updated_task.description
        task.status = updated_task.status
        task.priority = updated_task.priority
    return task

def delete_task(task_id: int) -> bool:
    global tasks_db
    tasks_db = [task for task in tasks_db if task.id != task_id]
    return True