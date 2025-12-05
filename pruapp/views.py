from django.shortcuts import render, redirect  # Importa funciones para renderizar templates y redireccionar URLs
from django.http import HttpResponse  # Importa la clase para enviar respuestas HTTP directas (texto)
from django.contrib import messages  # Importa el sistema de mensajes flash
from .models import Practica  # Importa el modelo de base de datos 'Practica'
from .forms import LoginForm, RegistroForm, EditarUsuarioForm  # Importa los formularios definidos en forms.py

# Create your views here.

# Vista simple que devuelve "Hola mundo"
def saludo(request):
    return HttpResponse("Hola mundo")

# Vista simple que devuelve "Hasta luego"
def despedida(request):
    return HttpResponse("Hasta luego")

# Renderiza la plantilla anime.html
def anime(request):
    return render(request, "./anime.html")

# Renderiza la plantilla plantilla.html
def mundo(request):
    return render(request, "./plantilla.html")

# Renderiza la plantilla UserRegister.html (versión anterior/simple)
# Nota: Hay otra vista 'user_register' más completa abajo.
def UserRegister(request):
    return render(request, "./UserRegister.html")

# Vista para manejar el inicio de sesión
def login_view(request):
    """Vista mejorada para login con formulario y validación en BD"""
    if request.method == "POST":  # Si el usuario envió el formulario
        form = LoginForm(request.POST)  # Crea una instancia del formulario con los datos enviados
        if form.is_valid():  # Valida los datos
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Buscar usuario en la BD
            try:
                usuario = Practica.objects.get(username=username)  # Busca el usuario por nombre
                # Validar contraseña (nota: aquí se compara texto plano, idealmente usar hashing)
                if usuario.password == password:
                    # Login exitoso - guardar datos en sesión
                    request.session['user_id'] = usuario.id
                    request.session['username'] = usuario.username
                    messages.success(request, f'Bienvenido {username}!')  # Mensaje de éxito
                    # Redirigir por nombre de ruta ('user_register' está en urls.py)
                    print(f"[LOGIN] Usuario '{username}' autenticado. Redirigiendo a user_register")
                    return redirect('user_register')  # Redirige a vista de usuarios
                else:
                    form.add_error('password', 'Contraseña incorrecta')  # Error si password no coincide
            except Practica.DoesNotExist:
                form.add_error('username', 'Usuario no encontrado')  # Error si usuario no existe
    else:
        form = LoginForm()  # Si es GET, muestra formulario vacío
    
    context = {'form': form}  # Contexto para la plantilla
    return render(request, "login.html", context)  # Renderiza login.html

# Vista para listar y gestionar usuarios
def user_register(request):
    """Vista para listar y eliminar usuarios registrados"""
    # Verificar si el usuario está logueado comprobando la sesión
    if 'user_id' not in request.session:
        messages.warning(request, 'Debes iniciar sesión primero')
        return redirect("login")
    
    # Procesar eliminación de usuario si la solicitud es POST
    if request.method == "POST":
        user_id = request.POST.get("user_id")  # Obtiene el ID del usuario a eliminar
        try:
            usuario = Practica.objects.get(id=user_id)  # Busca el usuario
            username_deleted = usuario.username
            usuario.delete()  # Elimina el usuario de la BD
            messages.success(request, f'Usuario "{username_deleted}" eliminado correctamente')
        except Practica.DoesNotExist:
            messages.error(request, 'Usuario no encontrado')
        return redirect("user_register")  # Recarga la página
    
    # Obtener todos los usuarios de la base de datos ordenados por nombre
    usuarios = Practica.objects.all().order_by('username')
    usuario_actual_id = request.session.get('user_id')  # ID del usuario logueado actualmente
    
    context = {
        'usuarios': usuarios,
        'usuario_actual_id': usuario_actual_id,
        'total_usuarios': usuarios.count()
    }
    return render(request, "UserRegister.html", context)  # Renderiza la lista de usuarios

# Vista para editar un usuario específico
def editar_usuario(request, user_id):
    """Vista para editar datos de un usuario"""
    # Verificar si el usuario está logueado
    if 'user_id' not in request.session:
        messages.warning(request, 'Debes iniciar sesión primero')
        return redirect("login")
    
    try:
        usuario = Practica.objects.get(id=user_id)  # Busca el usuario por ID
    except Practica.DoesNotExist:
        messages.error(request, 'Usuario no encontrado')
        return redirect("user_register")
    
    if request.method == "POST":
        # Carga el formulario con los datos enviados y la instancia del usuario
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)  # Prepara el objeto pero no lo guarda aún
            # Si se ingresó una nueva contraseña, actualizar
            if form.cleaned_data.get('password1'):
                usuario.password = form.cleaned_data['password1']
            # Actualizar imagen_url si se proporcionó
            imagen_url = form.cleaned_data.get('imagen_url')
            if imagen_url:
                usuario.imagen_url = imagen_url
            usuario.save()  # Guarda los cambios en BD
            messages.success(request, f'Usuario "{usuario.username}" actualizado correctamente')
            return redirect("user_register")
    else:
        form = EditarUsuarioForm(instance=usuario)  # Carga el formulario con datos actuales
    
    context = {
        'form': form,
        'usuario': usuario,
        'es_edicion': True
    }
    return render(request, "editar_usuario.html", context)

# Vista para cerrar sesión
def logout_view(request):
    """Vista para cerrar sesión"""
    username = request.session.get('username', 'Usuario')
    request.session.flush()  # Limpia todos los datos de sesión (cookies, etc.)
    messages.success(request, f'{username}, has cerrado sesión correctamente')
    return redirect("login")  # Redirige al login

# Vista para el registro de nuevos usuarios
def formulario(request):
    if request.method == "POST":
        # Formulario de registro (sólo URL de imagen, no subidas de archivo)
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = form.cleaned_data['password1']  # Asigna password
            # Guardar imagen_url si se proporcionó
            imagen_url = form.cleaned_data.get('imagen_url')
            if imagen_url:
                usuario.imagen_url = imagen_url
            usuario.save()  # Crea el nuevo usuario en BD
            messages.success(request, 'Usuario registrado exitosamente. ¡Inicia sesión!')
            return redirect("login")  # Redirige al login tras registro exitoso
    else:
        form = RegistroForm()  # Formulario vacío
    
    context = {'form': form}
    return render(request, "formulario.html", context)


 

