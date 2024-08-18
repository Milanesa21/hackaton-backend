from app.config import engine
from app.models import user_model

# Función para inicializar la base de datos y crear las tablas
def init_db():
    user_model.Base.metadata.create_all(bind=engine)
