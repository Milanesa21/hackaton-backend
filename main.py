from fastapi import FastAPI
from app.rutas import user_routes
from app.init_db import init_db

# Crear la instancia de FastAPI
app = FastAPI()

# Inicializar la base de datos al iniciar la aplicación
@app.on_event("startup")
def on_startup():
    init_db()

# Incluir las rutas
app.include_router(user_routes.router)

# Ruta principal
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app"}