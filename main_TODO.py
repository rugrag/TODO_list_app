from fastapi import FastAPI
from models import Todo

app = FastAPI()

todos = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

# GET ALL TODOS
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# POST A TODO_
@app.post("/todos")
async def create_todo(todo: Todo):

    todos.append(todo)
    return {"message": "todo has been added"}

# GET A TODO_
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):

    for item in todos:
        if item.id == todo_id:
            return {"todo": item}

    return {"message": "todo not found"}

# DELETE A TODO_
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):

    for item in todos:
        if item.id == todo_id:
            todos.remove(item)
            
            return {"message": "todo correctly DELETED"}

    return {"message": "todo not found"}

# UPDATE A TODO_
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, new_item: Todo):

    for old_item in todos:
        if old_item.id == todo_id:
            old_item.id = todo_id
            old_item.item = new_item.item
            
            return {"message": "todo correctly UPDATED"}

    return {"message": "todo not found"}