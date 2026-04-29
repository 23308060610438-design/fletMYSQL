from ..models.UserModel import UsuarioModel
from models.schemasModel import UsuarioSchemas
from pydantic import ValidationError 

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def registrar_usuario(self, nombre, email, password):
        try:
            # 1. Validamos los datos con el Schema de Pydantic
            # Esto lanzará ValidationError si el nombre es corto, email inválido, etc.
            nuevo_usuario = UsuarioSchemas(nombre=nombre, email=email, password=password)
            
            # 2. Pasamos el objeto al modelo y capturamos la respuesta de la BD
            # Importante: el modelo ahora devuelve (True/False, "Mensaje")
            success, message = self.model.registrar(nuevo_usuario)
            
            return success, message
            
        except ValidationError as e:
            # 3. Errores de validación (Pydantic)
            # Extraemos solo el mensaje amigable, ej: "String should have at least 8 characters"
            error_msg = e.errors()[0]['msg']
            return False, f"Validación: {error_msg}"
            
        except Exception as e:
            # 4. Otros errores inesperados
            return False, f"Error inesperado: {str(e)}"
        