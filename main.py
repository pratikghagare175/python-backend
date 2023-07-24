# from typing import Union
from fastapi import FastAPI
import app.config.mongo_config
from app.routes.library_route import router as library_router

app = FastAPI()

@app.get("/health")
async def read_root():
    return {"ok": True}

app.include_router(library_router)