# Generated by Django 3.2.7 on 2021-11-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_ouvinte_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ouvinte',
            name='email',
        ),
        migrations.AlterField(
            model_name='ouvinte',
            name='cpf',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
