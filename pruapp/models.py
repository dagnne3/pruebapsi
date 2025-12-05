from django.db import models  # Importa el módulo de modelos de Django para interactuar con la base de datos

class Practica(models.Model):  # Define una clase 'Practica' que hereda de models.Model, convirtiéndola en una tabla de base de datos
    username = models.CharField(max_length=150, unique=True)  # Campo de texto para el nombre de usuario, máximo 150 caracteres, debe ser único
    password = models.CharField(max_length=128)  # Campo de texto para la contraseña, máximo 128 caracteres
    imagen_url = models.URLField(max_length=500, blank=True, null=True)  # Campo para guardar una URL de imagen; es opcional (blank=True) y puede ser nulo en BD (null=True)

    def __str__(self):  # Método especial para definir cómo se representa este objeto como texto
        return self.username  # Devuelve el nombre de usuario cuando se imprime el objeto