from fastapi import FastAPI

from dotenv import load_dotenv
load_dotenv()

from app.routers import health, users, login, category
from app.middleware.middleware import setup_cors


app = FastAPI()

setup_cors(app)

app.include_router(health.router)
app.include_router(users.router)
app.include_router(login.router)
app.include_router(category.router)



@app.get("/")
async def root():
    return {"message": "Aplicacion inicializada correctamente"}

