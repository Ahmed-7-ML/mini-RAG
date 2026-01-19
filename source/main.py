from routes import base
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv('.env')

app = FastAPI(title="mini-RAG Application")

app.include_router(base.router)