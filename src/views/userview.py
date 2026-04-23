import flet as ft

def UserView(page, auth_ctrl):
    
    user_data = page.session.get("user")


    if not user_data:
        page.go("/")
        return ft.View("/user", [ft.Text("Redirigiendo...")])

    
    nombre_input = ft.TextField(
        label="Nombre Completo", 
        value=user_data.get('nombre', ''),
        width=350
    )
    email_input = ft.TextField(
        label="Correo Electrónico", 
        value=user_data.get('email', ''),
        width=350,
        read_only=True 
    )

    def actualizar_perfil(e):
        
        datos = {
            "nombre": nombre_input.value,
            "id": user_data['id']
        }
        
        
        success = auth_ctrl.actualizar_datos(datos)
        
        if success:
            
            user_data['nombre'] = nombre_input.value
            page.session.set("user", user_data)
            
            page.snack_bar = ft.SnackBar(ft.Text("Perfil actualizado correctamente"), bgcolor="green")
            page.snack_bar.open = True
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error al actualizar"), bgcolor="red")
            page.snack_bar.open = True
            
        page.update()

    def cerrar_sesion(e):
        page.session.clear()
        page.go("/")

    return ft.View("/user", [
        ft.AppBar(
            title=ft.Text("Mi Perfil"),
            bgcolor=ft.colors.BLUE_GREY_900,
            color="white",
            leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: page.go("/dashboard"))
        ),
        ft.Column([
            ft.Container(
                content=ft.Icon(ft.icons.PERSON_CIRCLE_OUTLINED, size=80, color=ft.colors.BLUE),
                margin=ft.margin.only(top=20)
            ),
            ft.Text(f"Bienvenido, {user_data.get('nombre')}", size=20, weight="bold"),
            ft.Divider(height=20, color="transparent"),
            
            nombre_input,
            email_input,
            
            ft.ElevatedButton(
                "Actualizar Datos", 
                icon=ft.icons.EDIT, 
                on_click=actualizar_perfil, 
                width=350
            ),
            
            ft.OutlinedButton(
                "Cerrar Sesión", 
                icon=ft.icons.LOGOUT, 
                on_click=cerrar_sesion, 
                width=350,
                style=ft.ButtonStyle(color=ft.colors.RED)
            ),
            
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.START)
    ])