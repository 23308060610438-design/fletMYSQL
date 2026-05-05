import bcrypt
from mysql.connector import Error

from .database import Database
class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self, usuario_data):
        """Hashea la contraseña y registra un nuevo usuario."""
        
        
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'), salt)
        
        conn = self.db.get_connection()
        if not conn:
            return False, "Error de conexión a la base de datos"

        try:
            cursor = conn.cursor()
            
            query = "INSERT INTO usuario (nombre, email, password) VALUES (%s, %s, %s)"
            values = (usuario_data.nombre, usuario_data.email, hashed_pw.decode('utf-8'))
            
            cursor.execute(query, values)
            conn.commit()
            return True, "Registro exitoso"
            
        except Error as e:
            
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