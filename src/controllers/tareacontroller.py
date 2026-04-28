from src.models.TareasModel import TareaModel

class TareaController: 
    def __init__(self):
        self.model = TareaModel()
        
    def obtener_lista(self, id_usuario):
        """Obtiene todas las tareas asociadas a un usuario."""
        try:
            # Corregido: se accede a través de self.model
            return self.model.obtener_por_usuario(id_usuario)
        except Exception as e:
            print(f"Error al obtener tareas: {e}")
            return []

    def guardar_nueva(self, id_usuario, titulo, desc, prio, clas):
        """Valida y guarda una nueva tarea."""
        # 1. Validaciones de negocio
        if not titulo or not titulo.strip():
            return False, "El título es obligatorio y no puede estar vacío"
        
        if not id_usuario:
            return False, "ID de usuario no proporcionado"

        try:
            # 2. Persistencia
            resultado = self.model.crear(id_usuario, titulo, desc, prio, clas)
            
            if resultado:
                return True, "Tarea guardada exitosamente"
            else:
                return False, "No se pudo guardar la tarea en la base de datos"
                
        except Exception as e:
            # 3. Manejo de excepciones
            return False, f"Error interno del servidor: {str(e)}"
            