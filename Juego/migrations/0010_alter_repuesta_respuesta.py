# Generated by Django 3.2.5 on 2021-08-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juego', '0009_alter_pregunta_pregunta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repuesta',
            name='respuesta',
            field=models.CharField(max_length=50),
        ),
    ]
