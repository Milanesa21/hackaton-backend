from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.controllers import user_controller
from app.models.schemas import user_schemas
from app.config import SessionLocal

# Crear un enrutador
router = APIRouter(prefix="/users", tags=["Users"])

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para el registro de usuarios
@router.post("/register", response_model=user_schemas.UserResponse)
def register_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user_controller.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    
    return user_controller.create_user(db, user)

# Ruta para el login de usuarios
@router.post("/login")
def login_user(user: user_schemas.UserLogin, db: Session = Depends(get_db)):
    authenticated_user = user_controller.authenticate_user(db, user.username, user.password)
    return {"message": "Login successful", "user": authenticated_user.username}
