import flet as ft 
from controllers.usercontroller import AuthController
from controllers.tareacontroller import TareaController
from Views.LoginView import LoginView
from Views.DashboardView import DashboardView

def start(page: ft.Page):
    
    page.title = "Sistema SIGE"
    page.window_width = 450 
    page.window_height = 700
    
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(e):
    
        page.views.clear()
        
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
            
        page.update()
            
    def view_pop(e):
        if len(page.views) > 1: 
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    print("Iniciando navegación...")
    
    
    if page.route == "/":
        route_change(None)
    else:
        page.go("/")


def main():
    ft.app(target=start)
                        
if __name__ == "__main__":
    main()