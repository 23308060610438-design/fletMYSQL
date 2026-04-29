import bcrypt
from mysql.connector import Error
# Importación relativa: el punto (.) significa "busca en esta misma carpeta"
from .database import Database
class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self, usuario_data):
        """Hashea la contraseña y registra un nuevo usuario."""
        
        # 1. Preparar la contraseña
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'), salt)
        
        conn = self.db.get_connection()
        if not conn:
            return False, "Error de conexión a la base de datos"

        try:
            cursor = conn.cursor()
            # Asegúrate de que tu tabla en MySQL se llame 'usuario' (singular)
            query = "INSERT INTO usuario (nombre, email, password) VALUES (%s, %s, %s)"
            values = (usuario_data.nombre, usuario_data.email, hashed_pw.decode('utf-8'))
            
            cursor.execute(query, values)
            conn.commit()
            return True, "Registro exitoso"
            
        except Error as e:
            # Error de entrada duplicada (email ya existe)
            if e.errno == 1062:
                return False, "El correo electrónico ya está registrado"
            return False, f"Error al registrar: {e}"
            
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def validar_login(self, email, password):
        """Verifica las credenciales del usuario."""
        conn = self.db.get_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT id, nombre, email, password FROM usuario WHERE email = %s"
            
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            
            if user:
                password_bytes = password.encode('utf-8')
                hash_bytes = user['password'].encode('utf-8')
                
                if bcrypt.checkpw(password_bytes, hash_bytes):
                    # Quitamos la contraseña del diccionario por seguridad antes de devolverlo
                    del user['password']
                    return user
                    
            return None

        except Error as e:
            print(f"Error en login: {e}")
            return None
            
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()