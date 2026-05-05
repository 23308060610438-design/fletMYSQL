from src.models.UserModel import UsuarioModel
from src.models.schemasModel import UsuarioSchemas  
from pydantic import ValidationError
class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def registrar_usuario(self, nombre, email, password):
        try:
            nuevo_usuario = UsuarioSchemas(nombre=nombre, email=email, password=password)
            
            
            success, message = self.model.registrar(nuevo_usuario)
            
            return success, message
            
        except ValidationError as e:
            
            error_msg = e.errors()[0]['msg']
            return False, f"Validación: {error_msg}"
            
        except Exception as e:
            
            return False, f"Error inesperado: {str(e)}"
        