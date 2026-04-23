import flet as ft 

def LoginView(page, auth_controller):
    email_input = ft.TextField(label="correo electronico", width=350, border_radius=10)
    # Corregido: pass_input para usarlo en la lógica
    pass_input = ft.TextField(label="contraseña", password=True, can_reveal_password=True, width=350, border_radius=10)
    
    def login_click(e):
        # Corregido: Tenías 'pass_input,value' (con coma) en lugar de '.value' (con punto)
        user, msg = auth_controller.login(email_input.value, pass_input.value)
        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
            
    return ft.View("/", [
        
        ft.AppBar(title=ft.Text("SIGE - Login"), bgcolor=ft.colors.BLUE_GREY_900, color="white"),
        
        
        ft.Column([
            ft.Icon(ft.icons.LOCK_PERSON, size=100, color=ft.colors.BLUE), # 'ft.icons' en minúscula para el catálogo
            ft.Text("Acceso al sistema", size=20, weight="bold"),
            email_input,
            pass_input, 
            ft.ElevatedButton("Entrar", on_click=login_click, width=350),
            ft.TextButton("Crear una cuenta nueva", on_click=lambda _: page.go("/registro"))
            
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)
            
    ])