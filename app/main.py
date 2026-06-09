from fastapi import FastAPI

from app.routers import health, users, login



app = FastAPI()

app.include_router(health.router)
app.include_router(users.router)
app.include_router(login.router)



@app.get("/")
async def root():
    return {"message": "Aplicacion inicializada correctamente"}

