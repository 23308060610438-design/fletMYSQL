import flet as ft

def TareaView(page, task_ctrl, tarea_seleccionada=None):

    titulo_input = ft.TextField(
        label="Título de la tarea", 
        width=350, 
        value=tarea_seleccionada['titulo'] if tarea_seleccionada else ""
    )
    descripcion_input = ft.TextField(
        label="Descripción", 
        multiline=True, 
        min_lines=3, 
        width=350,
        value=tarea_seleccionada['descripcion'] if tarea_seleccionada else ""
    )

    def guardar_click(e):
        
        user = page.session.get("user")
        if not user:
            page.go("/")
            return

        datos = {
            "titulo": titulo_input.value,
            "descripcion": descripcion_input.value,
            "id_usuario": user['id']
        }

        if tarea_seleccionada:
        
            id_tarea = tarea_seleccionada['id']
            success = task_ctrl.actualizar_tarea(id_tarea, datos)
            mensaje = "Tarea actualizada"
        else:
        
            success = task_ctrl.crear_tarea(datos)
            mensaje = "Tarea guardada con éxito"

        if success:
            page.snack_bar = ft.SnackBar(ft.Text(mensaje), bgcolor="green")
            page.snack_bar.open = True
            page.go("/dashboard") 
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error al procesar la tarea"), bgcolor="red")
            page.snack_bar.open = True
        
        page.update()

    
    texto_titulo = "Modificar Tarea" if tarea_seleccionada else "Nueva Tarea"

    return ft.View("/tarea", [
        ft.AppBar(
            title=ft.Text(texto_titulo),
            bgcolor=ft.colors.BLUE_GREY_900,
            color="white",
            leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/dashboard"))
        ),
        ft.Column([
            ft.Icon(ft.icons.ASSIGNMENT, size=50, color=ft.colors.BLUE),
            titulo_input,
            descripcion_input,
            ft.ElevatedButton(
                "Guardar Tarea", 
                icon=ft.icons.SAVE, 
                on_click=guardar_click, 
                width=350
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)
    ])