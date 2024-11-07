""" 
Main API core file, This file will contain:
    - Routing for CRUD
"""

from fastapi import FastAPI, Depends, HTTPException
from app import database as db, models, schemas
from typing import List, Optional

app = FastAPI()

@app.get('/tasks', response_model=List[models.Task])
def list_tasks(status: Optional[models.TaskStatus] = None, priority: Optional[models.TaskPriority] = None):
    return db.get_tasks(status, priority)

@app.get('/tasks/{task_id}', response_model=models.Task)
def get_task(task_id: int):
    task = db.get_task(task_id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post('/tasks', response_model=models.Task)
def create_task(task: schemas.TaskCreate):
    new_task = models.Task(id=len(db.tasks_db) + 1, **task.dict())
    db.add_task(new_task)
    return new_task

@app.put('/tasks/{task_id}', response_model=models.Task)
def update_task(task_id: int, task: schemas.TaskUpdate):
    existing_task = db.get_task(task_id)

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    updated_task = models.Task(id=task_id, **task.dict(exclude_unset=True))
    db.update_task(task_id, updated_task)
    return updated_task

@app.delete('/tasks/{task_id}', status_code=404)
def delete_task(task_id: int):
    if not db.delete_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {'message': 'Task deleted'}