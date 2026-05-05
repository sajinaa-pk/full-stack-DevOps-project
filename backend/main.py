from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Vue frontend to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fake database — just a list for now
todos = [
    {"id": 1, "title": "Learn Docker", "done": True},
    {"id": 2, "title": "Learn Kubernetes", "done": True},
    {"id": 3, "title": "Set up CI/CD", "done": False},
]

@app.get("/")
def root():
    return {"message": "Backend is alive!"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(todo: dict):
    new_todo = {
        "id": len(todos) + 1,
        "title": todo["title"],
        "done": False
    }
    todos.append(new_todo)
    return new_todo
