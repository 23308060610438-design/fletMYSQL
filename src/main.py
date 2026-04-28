import flet as ft 
from controllers.usercontroller import AuthController
from controllers.tareacontroller import TareaController
from Views.LoginView import LoginView
from Views.DashboardView import DashboardView

def start(page: ft.Page):
    page.title = "Sistema SIGE"
    page.window.width = 450      # Nota: En versiones nuevas de Flet se usa window.width
    page.window.height = 700
    
    # Inicialización de controladores
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(e):
        page.views.clear()
        
        # Ruta principal: Login
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        
        # Ruta de trabajo: Dashboard
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
            
        page.update()
            
    def view_pop(e):
        if len(page.views) > 1: 
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    # Configuración de eventos de navegación
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    # Navegación inicial
    page.go(page.route)

def main():
    # Ejecuta la app
    ft.app(target=start)
                        
if __name__ == "__main__":
    main()