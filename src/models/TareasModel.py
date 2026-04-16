from .database import Database
Class TareaModel:
    def __init__(self):
        self.db = DataBase()
        
    def listar_por_usuario(self, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        qury = "SELECT * FROM tareas WHERE id_usuario = %5 ORDER BY fecha_limite ASC"
        cursor.execute(query, (id_usuario,))
        resultado = cursor.fetchall()
        conn.close()
        return resultado
        