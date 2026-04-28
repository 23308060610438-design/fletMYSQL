import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    # Quitamos el @staticmethod para que funcione con self.db = Database()
    # O simplemente lo dejamos así y lo llamamos directamente.
    
    def get_connection(self):
        """
        Establece y retorna una conexión a la base de datos MySQL.
        """
        try:
            connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                charset='utf8mb4',
                collation='utf8mb4_general_ci'
            )
            
            if connection.is_connected():
                return connection

        except Error as e:
            print(f"❌ Error al conectar a la base de datos: {e}")
            return None

    def close_connection(self, connection):
        """Cierra la conexión de forma segura."""
        if connection and connection.is_connected():
            connection.close()
            print("🔌 Conexión cerrada.")