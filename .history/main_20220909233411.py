from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI"}

if __name__ == "__main__":
    uvicorn.run(app=app, host="192.168.1.1", port=8888)