# Generated by Django 3.2.7 on 2021-11-25 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_ouvinte_cpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ouvinte',
            name='nome',
        ),
    ]
