from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/main")
def read_main():
    return {"message": "This is the main API endpoint."}
