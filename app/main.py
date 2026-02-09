from fastapi import FastAPI

app = FastAPI(title="FastAPI Project created by David", version="1.0.0")

@app.get("/")
def home():
    return {"message":"Welcome to my first FastAPI project!"}

@app.get("/owner")
def owner_page():
    return {"message":"This project was created by David."}