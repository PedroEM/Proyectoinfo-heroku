# Generated by Django 3.2.5 on 2021-08-22 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juego', '0010_alter_repuesta_respuesta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='id_respuesta',
            field=models.IntegerField(),
        ),
    ]
