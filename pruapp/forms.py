from django import forms  # Importa la librería de formularios de Django
from .models import Practica  # Importa el modelo 'Practica' desde models.py para usarlo en formularios

# Formulario para el inicio de sesión
class LoginForm(forms.Form):
    username = forms.CharField(  # Campo de texto para el nombre de usuario
        max_length=150,  # Longitud máxima permitida
        widget=forms.TextInput(attrs={  # Configuración del widget HTML (input type="text")
            'class': 'form-control',  # Clase CSS para estilos (ej. Bootstrap)
            'placeholder': 'Nombre de usuario',  # Texto de ayuda dentro del campo
            'autocomplete': 'username'  # Ayuda al navegador a autocompletar este campo
        })
    )
    password = forms.CharField(  # Campo de texto para la contraseña
        widget=forms.PasswordInput(attrs={  # Configuración para que se vea como password (puntos/asteriscos)
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password'
        })
    )


# Formulario para el registro de usuarios, basado en el modelo Practica
class RegistroForm(forms.ModelForm):
    # Campo extra para contraseña (no está en el modelo directamente, se procesa después)
    password1 = forms.CharField(
        label='Contraseña',  # Etiqueta visible
        required=True,  # Campo obligatorio
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa tu contraseña',
        })
    )
    # Campo extra para confirmar la contraseña
    password2 = forms.CharField(
        label='Confirmar contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirma tu contraseña',
        })
    )

    class Meta:  # Clase interna para configurar el ModelForm
        model = Practica  # Enlaza este formulario con el modelo Practica
        fields = ['username', 'imagen_url']  # Campos del modelo que se incluirán en el formulario
        widgets = {  # Personalización de los widgets HTML para cada campo
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario',
            }),
            'imagen_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Pega la URL de la imagen (opcional)'
            })
        }

    # Método de limpieza y validación personalizada
    def clean(self):
        cleaned_data = super().clean()  # Obtiene los datos limpios por defecto
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        imagen_url = cleaned_data.get('imagen_url')

        # Valida que ambas contraseñas coincidan
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')  # Lanza error si son diferentes

        return cleaned_data  # Devuelve los datos validados


# Formulario para editar un usuario existente
class EditarUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña (opcional)',
        required=False,  # No es obligatorio cambiar la contraseña al editar
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Déjalo en blanco para mantener la actual',
        })
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirma tu contraseña',
        })
    )

    class Meta:
        model = Practica  # Enlaza con el modelo Practica
        fields = ['username', 'imagen_url']  # Permite editar usuario y URL de imagen
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de usuario',
            }),
            'imagen_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Pega la URL de la imagen (opcional)'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        # Si se introduce alguna contraseña, verificar que coincidan
        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError('Las contraseñas no coinciden')

        return cleaned_data
