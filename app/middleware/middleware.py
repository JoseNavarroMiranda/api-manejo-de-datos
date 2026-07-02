import os

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

FRONTEND_URL = os.getenv("FRONTEND_URL")


def setup_cors(app: FastAPI)-> None:
    origins = [
    FRONTEND_URL,]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )