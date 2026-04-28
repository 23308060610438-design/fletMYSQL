from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import date, time

# Cambié el nombre a UsuarioSchemas (con S) para que coincida con tu controlador
class UsuarioSchemas(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100, description="Nombre completo del usuario")
    email: EmailStr
    password: str = Field(..., min_length=8, description="Contraseña de al menos 8 caracteres")

    model_config = ConfigDict(from_attributes=True)

class TareaSchema(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200)
    descripcion: Optional[str] = Field(None, max_length=500)
    prioridad: str = Field(default="media", pattern="^(baja|media|alta)$")
    clasificacion: str = Field(default="personal") 
    
    fecha_limite: Optional[date] = None
    hora_recordatorio: Optional[time] = None

    model_config = ConfigDict(from_attributes=True)