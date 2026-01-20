from fastapi import FastAPI, APIRouter, Depends
from helpers.config import get_settings, Settings
# import os

app = FastAPI(title="mini-RAG Application")
router = APIRouter(
    prefix='/api/v1',
    tags=['api_v1']
)

# Can be used for Healthy Check (eg. by DevOps)
@router.get("/")
async def welcome(app_settings : Settings =Depends(get_settings)):
    # app_name = os.getenv("APP_NAME")
    # app_version = os.getenv("APP_VERSION")

    # app_settings = get_settings()
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "App": app_name,
        "Version": app_version,
        "Message": "Hello mini-RAG"
    }
