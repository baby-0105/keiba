from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from routers.users import router as user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
