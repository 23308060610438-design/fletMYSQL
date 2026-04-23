from src.models.UserModel import UsuarioModel
from src.models.schemasModel import UsuarioSchemas
from pydantic import ValidationError # Asegúrate de importar esto

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def registrar_usuario(self, nombre, email, password):
        try:
            # 1. Validamos los datos con el Schema
            nuevo_usuario = UsuarioSchemas(nombre=nombre, email=email, password=password)
            
            # 2. Pasamos el objeto validado al modelo
            success = self.model.registrar(nuevo_usuario)
            
            return success, "Usuario creado correctamente"
            
        except ValidationError as e:
            # 3. Corregimos el acceso al mensaje de error de Pydantic
            # e.errors() devuelve una lista de diccionarios
            error_msg = e.errors()[0]['msg']
            return False, error_msg
        except Exception as e:
            # 4. Manejo de errores inesperados (ej. base de datos)
            return False, str(e)
        