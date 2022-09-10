from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI"}

@app.get("/test")
def test():
    return {"test": "hello"}

# uvicorn main:app --reload --port 50010