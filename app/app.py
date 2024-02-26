from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World1212331!"}

@app.get("/test")
def read_root():
    return {"message": "Test, World1212331!"}