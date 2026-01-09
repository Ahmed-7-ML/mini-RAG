from fastapi import FastAPI

app = FastAPI(title="mini-RAG Application")

@app.get("/home")
def welcome():
    return {
        "message": "Hello mini-RAG"
    }
