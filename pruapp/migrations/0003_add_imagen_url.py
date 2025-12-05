# Generated migration to add imagen_url field
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('pruapp', '0002_alter_practica_options_practica_fecha_registro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='practica',
            name='imagen_url',
            field=models.URLField(max_length=500, null=True, blank=True),
        ),
    ]
