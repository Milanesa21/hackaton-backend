from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models import user_model
from app.models.schemas import user_schemas
from passlib.context import CryptContext

# Configuración del contexto de hashing para las contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para obtener un usuario por su nombre de usuario
def get_user_by_username(db: Session, username: str):
    return db.query(user_model.User).filter(user_model.User.username == username).first()

# Función para crear un nuevo usuario
def create_user(db: Session, user: user_schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = user_model.User(username=user.username, email=user.email, hashed_password=hashed_password)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

# Función para autenticar un usuario
def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user or not pwd_context.verify(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    return user

#Funcion para borrar un usuario
def delete_user(db: Session, username: str):
    user = get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    return user

#Funcion para actualizar un usuario
def update_user(db: Session, id: int, new_name: str):
  user = db.query(Users).filter(Users.id == id).first()
  if user:
      user.full_name = new_name
      db.commit()
      db.refresh(user)
      return True
  return False
