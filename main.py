from fastapi import FastAPI, Body
from model.model import Task
import data.taskman as data
import uvicorn

app = FastAPI()

@app.get("/api/tasks/{id}")
def get_task(id:int):
    """todo fetch the task by id"""
    return data.get_task(id)

@app.get("/api/tasks")
def get_all() -> list[Task]:
    return data.get_all_task()

@app.post("/api/tasks/create")
def create(task:Task):
    """todo 1. create a new task and 2. return the details of task"""
    return data.create_task(task)

@app.put("/api/tasks/{id}/update")
def update(id:int, task:Task):
    return data.update_task(id, task)

@app.delete("/api/tasks/{id}/delete")
def delete_task(id:int):
    """todo 1.delete the task by id 2. return a condirmation of deletion"""
    data.delete_task(id)

if __name__ == "__main__":
    uvicorn.run("main:app", reload = True)
