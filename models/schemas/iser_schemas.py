from pydantic import BaseModel, EmailStr

# Esquema de solicitud para la creación de usuarios
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Esquema de solicitud para el login de usuarios
class UserLogin(BaseModel):
    username: str
    password: str

# Esquema de respuesta para mostrar los datos del usuario
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
