# Generated by Django 3.2.7 on 2021-10-20 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_evento_descricao'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
