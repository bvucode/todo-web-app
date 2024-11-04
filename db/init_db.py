import sqlite3

con = sqlite3.connect("todo.db")
cur = con.cursor()
cur.execute(
        "create table if not exists todo(id, description, priority); ")

def get_db():
    print("Done!")
get_db()
