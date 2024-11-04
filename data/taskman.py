from model.model import Task
import sqlite3

def row_to_model(row:tuple) -> Task:
    return Task(id = row[0], description = row[1], priority = row[2])

def model_to_dict(task:Task) -> dict:
    return task.dict()

def get_task(id:int) -> Task:
    """todo 1. fetch the task by id provided"""
    qry = """select * from todo where id=:id"""
    con = sqlite3.connect("db/todo.db")
    curs = con.cursor()
    params = {"id":id}
    curs.execute(qry, params)
    return (row_to_model(curs.fetchone()))

def get_all_task() -> list[Task]:
    """todo 1. fetch the all tasks"""
    qry = """select * from todo"""
    con = sqlite3.connect("db/todo.db")
    curs = con.cursor()
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create_task(new_task:Task) -> Task:
    """todo 1. create a new task and save in db file"""
    qry = """insert into todo(id, description, priority)
    values(:id, :description, :priority)"""
    con = sqlite3.connect("db/todo.db")
    curs = con.cursor()
    params = model_to_dict(new_task)
    curs.execute(qry, params)
    con.commit()
    return get_task(new_task.id)

def delete_task(id:int) -> bool:
    """todo 1. delete the task by id provided"""
    qry = """delete from todo where id=:id"""
    con = sqlite3.connect("db/todo.db")
    curs = con.cursor()
    params = {"id": id}
    res = curs.execute(qry, params)
    con.commit()
    return bool(res)

def update_task(id:int, new_task:Task):
    """todo 1. update the task by id based on new task details"""
    qry = """update todo set id=:id, description=:description, priority=:priority where id=:id_orig"""
    con = sqlite3.connect("db/todo.db")
    curs = con.cursor()
    params = model_to_dict(new_task)
    params["id_orig"] = new_task.id
    _ = curs.execute(qry, params)
    con.commit()
    return get_task(new_task.id)
