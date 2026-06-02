from fastapi import FastAPI

from app.routers import health
from app.routers import users


app = FastAPI()

app.include_router(health.router)
app.include_router(users.router)



@app.get("/")
async def root():
    return {"message": "Aplicacion inicializada correctamente"}

