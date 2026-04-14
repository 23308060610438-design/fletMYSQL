from src.models.UserModel import UsuarioModel
from src.models.schemasModel import UsuarioSchemas

class AuthController:
    def __init__(self):
        self.model=UsuarioModel()
        def registrar-ususario(self, nombre, email, password):
        try:
                nuevo_usuario = UsuarioSchemas(nombre=nombre, email=email, password=password)
                succes = self.model.registrar(nuevo_usuario)
                return succes, "Usuario creado correctamente"
            except ValidationError as e:
                return False, e,error()[0]['msg']
                