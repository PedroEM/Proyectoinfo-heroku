# Generated by Django 3.2.5 on 2021-08-22 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juego', '0008_alter_pregunta_pregunta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='pregunta',
            field=models.CharField(max_length=200),
        ),
    ]
