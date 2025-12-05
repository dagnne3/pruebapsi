from django.urls import path  # Importa la función path para definir rutas
from . import views  # Importa las vistas definidas en views.py

urlpatterns = [
    # Ruta para 'home/', ejecuta views.saludo y se llama 'home1' internamente
    path("home/", views.saludo, name="home1"),
    
    # Ruta para 'anime/', ejecuta views.anime
    path("anime/", views.anime, name="principal"),
    
    # Ruta para 'bye/', ejecuta views.despedida
    path("bye/", views.despedida, name="bye1"),
    
    # Ruta para 'plantilla/', ejecuta views.mundo
    path("plantilla/", views.mundo, name="plantilla"),
    
    # Ruta para el formulario de registro ('formulario/')
    path("formulario/", views.formulario, name="formulario"),
    
    # Ruta para el login ('login/')
    path("login/", views.login_view, name="login"),
    
    # Ruta para gestionar usuarios ('UserRegister/')
    path("UserRegister/", views.user_register, name="user_register"),
    
    # Ruta para cerrar sesión ('logout/')
    path("logout/", views.logout_view, name="logout"),
    
    # Ruta dinámica para editar usuario: captura un entero <int:user_id>
    path("editar/<int:user_id>/", views.editar_usuario, name="editar_usuario"),
]


