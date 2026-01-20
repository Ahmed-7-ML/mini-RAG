from routes import base, data
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI(title="mini-RAG Application")

app.include_router(base.router)
app.include_router(data.data_router)
