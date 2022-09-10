from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI"}

# uvicorn main:app --reload --host 0.0.0.0 --port 8000