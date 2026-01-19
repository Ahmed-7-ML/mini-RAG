from fastapi import FastAPI, APIRouter
import os

app = FastAPI(title="mini-RAG Application")
router = APIRouter(
    prefix='/api/v1',
    tags=['api_v1']
)

# Can be used for Healthy Check (eg. by DevOps)
@router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {
        "App": app_name,
        "Version": app_version,
        "Message": "Hello mini-RAG"
    }
