import flet as ft

def DashboardView(page, tarea_controller):
    user = page.session.get("user")
    lista_tareas = ft.column(scroll=ft.scrollMode.ALWAYS, expand=True)
    
    def refresh():
        lista_tareas.controls.clear()
        for t in tarea_controller.obtener_lista(user['id_usuario']):
            lista_tareas.controls.append(
                ft.card(
                    content=ft.container(
                        content=ft.ListTile(
                            title=ft.Text(t['titulo'], weight="bold"),
                            subtitle=ft.Text(f"{t['descripcion']}\nPrioridad: {t['prioridad']}"),
                            tralling=ft.Badge(content=ft.Text(t['estado']), bgcolor=ft.colors.ORANGE_300)
                            
                        ), padding=10
                    )
                )
            )
        page.update()
        